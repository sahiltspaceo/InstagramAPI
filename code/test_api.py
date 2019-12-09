#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
import json
import csv
from urllib import request

from igapi import IGAPI
ig = IGAPI()


def write_file(filename,data):
	filename = "/home/sotsys-056/projects/igapi/data/" + filename + ".json"
	with open(filename, 'w') as outfile:
		json.dump(data, outfile)

"""First time login 'challenge' issue """
# api.login()
# time.sleep(10)
# api.login()


"""Login with username password"""
# username = "sahilt1234"
# password = "sahil@1511"
# ig.login(username=username,password=password)


"""Login with token"""
sig = "ig_sig_key_version=4&signed_body=9a9886082fd8e3e86ab955860bdf751e794f262814d5f281fd2e9179fe257e24.%7B%22guid%22%3A%20%2254cd3f12-eb8c-4fa9-bdb7-ebb8a9ed5d22%22%2C%20%22username%22%3A%20%22sahilt1234%22%2C%20%22password%22%3A%20%22sahil%401511%22%2C%20%22device_id%22%3A%20%22android-2079ee7c73abd7a7%22%2C%20%22login_attempt_count%22%3A%20%220%22%2C%20%22phone_id%22%3A%20%22f3d33e58-d1fe-4f60-b1ed-69eedf84dcf0%22%2C%20%22_csrftoken%22%3A%20%22eyjOUnnDYtjTx0dGcVwuXz8jgQkIGc6F%22%7D"
uuid = "945aba3c-8c3f-4f0a-83df-29ccf290006e"
ig.login(sig=sig,uuid=uuid)

# print("profile data: ",ig.get_profile_data())
# print("---------------------------------------------------------------------------")
# print("user id: ",ig.get_user_id())
# print("---------------------------------------------------------------------------")
# print("user feed: ",ig.get_user_feed())
# print("---------------------------------------------------------------------------")
# print("followers json: ",ig.get_followers_json())
# print("---------------------------------------------------------------------------")
# print("followers count: ",ig.get_followers_count())
# print("---------------------------------------------------------------------------")
# print("following json: ",ig.get_following_json())
# print("---------------------------------------------------------------------------")
# print("following count: ",ig.get_following_count())
# print("---------------------------------------------------------------------------")
# print("timeline feed: ",ig.get_timeline())
# print("---------------------------------------------------------------------------")
# print("user posts: ",ig.get_user_posts())
# print("---------------------------------------------------------------------------")
# print("user posts count: ",ig.get_user_post_count())
# print("---------------------------------------------------------------------------")
# print("user posts filter: ",ig.filter_user_post_type())
# print("---------------------------------------------------------------------------")
# print("notifcation json: ",ig.get_notifications_json())
# print("---------------------------------------------------------------------------")
# print("notifcation list: ",ig.get_notifications_text_list())
# print("---------------------------------------------------------------------------")
# print("notifcation by username: ",ig.get_notification_by_user("saahilthakkar"))
# print("---------------------------------------------------------------------------")
# print("all posts ID list: ",ig.get_user_posts_id())
# print("---------------------------------------------------------------------------")
# print("all threads json: ",ig.get_threads_json())
# print("---------------------------------------------------------------------------")
# print("story json: ",ig.get_story_json())
# print("---------------------------------------------------------------------------")
# print("search users json: ",ig.search_users("sahil thakkar"))
# print("---------------------------------------------------------------------------")
print("get feed by location id: ",ig.feed_by_location("222050525045057"))
data = ig.feed_by_location("222050525045057")
write_file("location_by_id",data)
# print("---------------------------------------------------------------------------")
# print("get feed by location name: ",ig.feed_by_location_name("rajmachi"))
# print("---------------------------------------------------------------------------")
# ig.follow("1221745224")
# ig.unfollow("1221745224")
# print(ig.friendship("1221745224"))

print("Done")

