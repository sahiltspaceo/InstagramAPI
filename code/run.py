from flask import Flask, render_template,request
app = Flask(__name__)

from igapi import IGAPI
ig = IGAPI()


@app.route("/")
def template_test():
    return render_template('index2.html')

@app.route("/login",methods=['POST'])
def login():
	if request.method == 'POST':
		print(request.form)
		username = request.form['uname']
		password = request.form['psw']
		try:
			ig.login(username=username,password=password)
			
			profile = ig.get_profile_data()
			userid = profile['user']['pk']
			full_name = profile['user']['full_name']
			posts = ig.get_user_post_count()
			followers = ig.get_followers_count()
			followings = ig.get_following_count()

			likes = 0
			comments = 0

			user_posts = ig.get_user_posts()
			for i in range(0,len(user_posts)):
				likes = likes + user_posts[i]['like_count']
				comments = comments + user_posts[i]['comment_count']
			
			avg_likes = int(likes/posts)
			avg_comments = int(comments/posts)

			photos,videos,albums = ig.filter_user_post_type()
				
			return render_template('index2.html', userid = userid,full_name = full_name,
									posts = posts,followers = followers,followings = followings,
									likes = likes,comments = comments,avg_likes = avg_likes,avg_comments=avg_comments,
									photos= photos,videos=videos,albums=albums,username=username,password=password)

		except:
			return "Error"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)