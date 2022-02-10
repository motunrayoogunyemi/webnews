import json,requests
from turtle import pos
from xml.dom.minidom import Comment
from flask import flash, render_template, request, redirect, session,url_for

from projectapp import app
from projectapp.mymodels import Job, Comment, Poll, Polloption, Story, db, Order

@app.route('/home')
def home():
    #connect to api endpoint
    response = requests.get('http://localhost:8080/resources/')
    resp = response.json()
    return render_template('index.html', resp=resp)      

@app.route('/submitpost', methods=['GET', 'POST'])
def submitpost():
    if request.method == 'GET':
        return render_template('submitpost.html')
    postType = request.form.get('type')
    postTitle = request.form.get('title')
    author = request.form.get('author')
    postUrl = request.form.get('url')
    postText = request.form.get('text')
    headers = {"Content-Type": "application/json"}
    data = {"type": postType, "title": postTitle, "by": author, "url":postUrl, "text":postText}
    response = requests.post('/resources/?id={}&type={}&text={}', to_json = json.dumps(data), headers=headers)
    r = response.json()
    return r
    
# @app.route('/comments/<int:id>', methods=['GET', 'POST'])
# def comments(id):
#     if request.method == 'GET':
#         post_comment = db.session.query(Comment).filter(Comment.comment_id==id)
#         return render_template('comments.html', post_comment=post_comment) 
#     #get form data
#     pass 
 
# @app.route('/replycomments/<int:id>', methods=['GET', 'POST'])
# def replycomments(id):
#     if request.method == 'GET':
#         post_comment = db.session.query(Comment).filter(Comment.comment_id==id)
#         return render_template('comments.html', post_comment=post_comment) 
#     #get form data
#     pass     

@app.route('/comments',methods=['GET', 'POST'])
def comments():
    return render_template('comments.html')      

@app.route('/replycomments', methods=['GET', 'POST'])
def replycomments():
    return render_template('replycomments.html')  