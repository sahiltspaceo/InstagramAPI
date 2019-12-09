from InstagramAPI import InstagramAPI
import time
import json
import csv
from urllib import request


### First time login 'challenge' issue
# api.login()
# time.sleep(15)
# api.login()


class IGAPI:

	def login(self,username=None,password=None,sig=None,uuid=None):
		if username and password:
			self.api = InstagramAPI(str(username),str(password))
			self.api.login()
		elif sig and uuid:
			self.api = InstagramAPI()
			self.api.login(sig=sig,uuid=uuid)
		else:
			print("Invalid params")

	def get_profile_data(self):
		self.api.getProfileData()  # get self user feed
		return self.api.LastJson

	def get_user_id(self):
		self.api.getProfileData()  # get self user feed
		return self.api.LastJson['user']['pk']
	
	def get_user_feed(self):
		self.api.getSelfUserFeed()
		return self.api.LastJson

	def get_json(self):
		return self.api.LastJson

	def get_followers_json(self):
		userid = self.get_user_id()

		followers   = []
		next_max_id = True
		while next_max_id:
			#first iteration hack
			if next_max_id == True: next_max_id=''
			_ = self.api.getUserFollowers(userid,maxid=next_max_id)
			followers.extend (self.api.LastJson.get('users',[]))
			next_max_id = self.api.LastJson.get('next_max_id','')
			time.sleep(1) 
		    
		return followers

	def get_followers_count(self):
		followers = self.get_followers_json()
		user_list = map(lambda x: x['username'] , followers)
		followers_set= set(user_list)
		return len(followers_set)

	def get_following_json(self):
		userid = self.get_user_id()

		followers   = []
		next_max_id = True
		while next_max_id:
			#first iteration hack
			if next_max_id == True: next_max_id=''
			_ = self.api.getUserFollowings(userid,maxid=next_max_id)
			followers.extend (self.api.LastJson.get('users',[]))
			next_max_id = self.api.LastJson.get('next_max_id','')
			time.sleep(1) 
		    
		return followers

	def get_following_count(self):
		followers = self.get_following_json()
		user_list = map(lambda x: x['username'] , followers)
		followers_set= set(user_list)
		return len(followers_set)

	def get_timeline(self):
		self.api.timelineFeed()
		return self.api.LastJson

	def get_user_posts(self):
		myposts=[]
		has_more_posts = True
		max_id=""
		
		while has_more_posts:
			self.api.getSelfUserFeed(maxid=max_id)
			if self.api.LastJson['more_available'] is not True:
				has_more_posts = False #stop condition
				print("stopped")
		    
			max_id = self.api.LastJson.get('next_max_id','')
			myposts.extend(self.api.LastJson['items']) #merge lists
			time.sleep(2) # Slows the script down to avoid flooding the servers 
		    
		return myposts

	def get_user_post_count(self):
		self.api.getUsernameInfo(self.get_user_id())
		return self.api.LastJson['user']['media_count']

	def filter_user_post_type(self):
		myposts_photos= list(filter(lambda k: k['media_type']==1, self.get_user_posts()))
		myposts_vids= list(filter(lambda k: k['media_type']==2, self.get_user_posts()))
		myposts_carousel= list(filter(lambda k: k['media_type']==8, self.get_user_posts()))

		return len(myposts_photos),len(myposts_vids),len(myposts_carousel)

	def get_user_posts_id(self):
		n_media = self.get_user_post_count()
		media_ids = []
		max_id = ''

		print("nmedia ",n_media)
		for i in range(n_media//19): 
			self.api.getUserFeed(usernameId=userid, maxid = max_id)
			media_ids += self.api.LastJson['items'] 
			if self.api.LastJson['more_available']==False:
				print("no more avaliable")
				break
			max_id = self.api.LastJson['next_max_id'] 
			print(i, "   next media id = ", max_id, "  ", len(media_ids))
			time.sleep(3)
		return media_ids
		
	def get_notifications_json(self):
		self.api.getRecentActivity()
		return self.api.LastJson

	def get_notifications_text_list(self):
		notifcation_list = []
		get_recent_activity_response = self.get_notifications_json() 
		for notifcation in get_recent_activity_response['old_stories']:
			notifcation_list.append(notifcation['args']['text'])
		return notifcation_list

	def get_notification_by_user(self,username):
		notifcation_list = []
		get_recent_activity_response = self.get_notifications_json() 
		for notifcation in get_recent_activity_response['old_stories']:
		    text = notifcation['args']['text']
		    if username  in text:
		       notifcation_list.append(text)

		return notifcation_list

	def direct_message(self,recipients=[],mediaID="",text=""):
		self.api.direct_share(mediaID, recipients, text='demo')

	def get_threads_json(self):### Get all threads
		self.api.USER_AGENT = 'Instagram 10.34.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'
		self.api.getv2Inbox()
		return self.api.LastJson

	def get_story_json(self):
		self.api.getStory(self.get_user_id)
		return self.api.LastJson

	def search_users(self,query):
		self.api.searchUsers(query)
		return self.api.LastJson

	def feed_by_location(self,locationid):
		self.api.getLocationFeed(locationid)
		return self.api.LastJson

	def feed_by_location_name(self,query):
		self.api.searchLocation(query)
		return self.api.LastJson

	def follow(self,userid):
		self.api.follow(userid)

	def unfollow(self,userid):
		self.api.unfollow(userid)

	def friendship(self,userid):
		self.api.userFriendship(userid)
		return self.api.LastJson