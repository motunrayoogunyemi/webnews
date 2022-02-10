import json,requests
from turtle import pos
from xml.dom.minidom import Comment
from flask import flash, render_template, request, redirect, session,url_for

from projectapp import app
from projectapp.mymodels import Job, Comment, Poll, Polloption, Story, db, Order   

@app.route('/home', methods=['GET','POST'])
def home():
    #connect to api endpoint
    # response = requests.get('http://localhost:8080/resources/')
    type_filter = request.args.get('type')
    text_filter = request.args.get('text')
    page = request.args.get('page',default=1)
    params = {"type": type_filter,"text":text_filter,"page":page}
    response = requests.get('http://localhost:8080/resources/', params=params)
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
    data = {"type": postType, "title": postTitle, "author": author, "url":postUrl, "text":postText}
    response = requests.post('http://localhost:8080/resources/', headers=headers, data=json.dumps(data))
    res = response.json()
    return res  

@app.route('/editpost/<id>/<type>',methods=['GET', 'POST']) 
def editpost(id, type):
    if request.method == 'GET':
        return render_template('editpost.html')
    else:   
        postTitle = request.form.get('title')
        author = request.form.get('author')
        postUrl = request.form.get('url')
        postText = request.form.get('text')
        params = {"type": type, "id": id}
        data = {"title": postTitle, "author": author, "url":postUrl, "text":postText}
        response = requests.put('http://localhost:8080/resources/', params=params, data=json.dumps(data))
        res = response.json()
        return res  


@app.route('/deletepost/', methods=['GET','DELETE', 'POST'])
def deletepost():
    response = requests.delete('http://localhost:8080/resources/', params=request.args)
    res = response.json()
    return res
     

# postID = request.form.get('id')
#         postType = request.form.get('type')
#         data = {"id": postID, "type": postType}
#         headers = {"Content-Type": "application/json"}
#         response = requests.delete('http://localhost:8080/resources/', headers=headers, data=json.dumps(data))
#         res = response.json()
#         return res    
    
@app.route('/comments/<id>/<type>')
def comments(id, type):
    params = {"type": type, "parent_id": id}
    response = requests.get('http://localhost:8080/resources/', params=params)
    res = response.json()
    #print(res)
    return render_template('comments.html', res=res)
    
 
# @app.route('/replycomments/<int:id>', methods=['GET', 'POST'])
# def replycomments(id):
#     if request.method == 'GET':
#         post_comment = db.session.query(Comment).filter(Comment.comment_id==id)
#         return render_template('comments.html', post_comment=post_comment) 
#     #get form data
#     pass     

# @app.route('/comments',methods=['GET', 'POST'])
# def comments():
#     return render_template('comments.html')      

# @app.route('/replycomments', methods=['GET', 'POST'])
# def replycomments():
#     return render_template('replycomments.html')  