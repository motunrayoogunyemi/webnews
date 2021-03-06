import json
import math
from pydoc import text
from re import S
from turtle import title
from flask import jsonify, render_template,request, session
from flask_restx import Resource
from flask_restx import fields
from sqlalchemy import or_

from projectapp import api
from projectapp.mymodels import Job, Comment, Order, Poll, Polloption, Story, db

# @api.route('/alljobs/')
# class Jobs(Resource):
#     def get(self):
#         data = db.session.query(Job).all()
#         if data:
#             alljobs = []
#             for i in data:
#                 comments = db.session.query(Comment).filter(Comment.parent_id==i.job_id)
#                 a={}
#                 a['id']=i.id
#                 a['jobID']=i.job_id
#                 a['postType']=i.post_type
#                 a['author']=i.by
#                 a['postText']=i.text
#                 a['postUrl']=i.url
#                 a['postTitle']=i.title
#                 a['postDate']=i.date
#                 alljobs.append(a)
#             res ={alljobs}
#         else:
#             res ={"No Data found"}
#         return jsonify(res)

# @api.route('/addjob/')
# class Postjob(Resource):
#     def post(self):
#         if request.is_json:
#             data = request.get_json()
#             records = Job(post_type=data.get('postType'), by=data.get('author'), text=data.get('postText'), url=data.get('postUrl'), title=data.get('postTitle'))
#             db.session.add(records)
#             db.session.commit()
#             posttitle = records.title
#             res = {f"Successully made post {posttitle}"}
#         else:
#             res = {'Bad format, supply JSON data'}
#         return jsonify(res)

# @api.route('/onejob/<int:id>')
# class Onejob(Resource):
#     def get(self, id):
#         data = db.session.query(Job).get(id)
#         res = {'id':data.id,'jobID':data.job_id,'postType':data.post_type,'author':data.by,'postText':data.text,'postUrl':data.url,'postTitle':data.title,'postDate':data.date}
#         return jsonify(res)

#     def put(self, id):
#         record = db.session.query(Job).get(id)
#         data = request.get_json()
#         record.post_type = data['postType']
#         record.by = data['author']
#         record.text = data['postText']
#         record.url = data['postUrl']
#         record.title = data['postTitle']
#         db.session.commit()
#         res = {record}
#         return jsonify(res)

#     def delete(self, id):
#         record = db.session.query(Job).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return {'data':'Empty record'}

# @api.route('/allstories/')
# class Stories(Resource):
#     def get(self):
#         data = db.session.query(Story).all()
#         if data:
#             allstories = []
#             for m in data:
#                 a={}
#                 a['id']=m.id
#                 a['storyID']=m.story_id
#                 a['postType']=m.post_type
#                 a['author']=m.by
#                 a['postScore']=m.score
#                 a['postdescendants']=m.descendants
#                 a['postUrl']=m.url
#                 a['postTitle']=m.title
#                 a['postDate']=m.date
#                 allstories.append(a)
#             res ={allstories}
#         else:
#             res ={"No Data found"}
#         return jsonify(res)

# @api.route('/addstory/')
# class Postjob(Resource):
#     def post(self):
#         if request.is_json:
#             data = request.get_json()
#             records = Story(post_type=data.get('postType'), by=data.get('author'), url=data.get('postUrl'), title=data.get('postTitle'))
#             db.session.add(records)
#             db.session.commit()
#             posttitle = records.title
#             res = {f"Successully made post {posttitle}"}
#         else:
#             res = {'Bad format, supply JSON data'}
#         return jsonify(res)

# @api.route('/onestory/<int:id>')
# class Onestory(Resource):
#     def get(self, id):
#         data = db.session.query(Story).get(id)
#         res = {'id':data.id,'storyID':data.job_id,'postType':data.post_type,'author':data.by,'postScore':data.score,'postdescendants':data.descendants,'postUrl':data.url,'postTitle':data.title,'postDate':data.date}
#         return jsonify(res)

#     def put(self, id):
#         record = db.session.query(Story).get(id)
#         data = request.get_json()
#         record.post_type = data['postType']
#         record.by = data['author']
#         record.url = data['postUrl']
#         record.title = data['postTitle']
#         db.session.commit()
#         res = {record}
#         return jsonify(res)

#     def delete(self, id):
#         record = db.session.query(Story).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return {'data':'Empty record'}

# @api.route('/allcomments/')
# class Commentss(Resource):
#     def get(self):
#         data = db.session.query(Comment).all()
#         if data:
#             allcomments = []
#             for d in data:
#                 a={}
#                 a['id']=d.id
#                 a['commentID']=d.job_id
#                 a['postType']=d.post_type
#                 a['author']=d.by
#                 a['postText']=d.text
#                 a['postParent']=d.parent_id
#                 a['postDate']=d.date
#                 allcomments.append(a)
#             res ={allcomments}
#         else:
#             res ={"No Data found"}
#         return jsonify(res)

# @api.route('/addcomment/')
# class Postcomment(Resource):
#     def post(self):
#         if request.is_json:
#             data = request.get_json()
#             records = Comment(post_type=data.get('postType'), by=data.get('author'), text=data.get('postText'))
#             db.session.add(records)
#             db.session.commit()
#             postparent = records.parent_id
#             res = {f"Successully made comment to post with id {postparent}"}
#         else:
#             res = {'Bad format, supply JSON data'}
#         return jsonify(res)

# @api.route('/onecomment/<int:id>')
# class Onecomment(Resource):
#     def get(self, id):
#         data = db.session.query(Comment).get(id)
#         res = {'id':data.id,'commentID':data.job_id,'postType':data.post_type,'author':data.by,'postText':data.text,'postParent':data.parent_id,'postDate':data.date}
#         return jsonify(res)

#     def put(self, id):
#         record = db.session.query(Comment).get(id)
#         data = request.get_json()
#         record.post_type = data['postType']
#         record.by = data['author']
#         record.text = data['postText']
#         db.session.commit()
#         res = {record}
#         return jsonify(res)

#     def delete(self, id):
#         record = db.session.query(Comment).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return {'data':'Empty record'}

# Thought process
# app.route('/?username=<username>&password=<password>')
# @api.route('/resources/?type=story&text=hoe')
# class Getitems(Resource):
#     def get(self):
#         # if ID is specified in the query params, return a single item with that matches the ID
#         # else, return a list of items, retrieved from the Order table, then populated by type, paginated
#         params = request.args
#         {"type":"story", "text":"hoe"}
#         pass

#     def post(self):
#         body = request.get_json()
#         pass

#     def put(self):
#         params = request.args
#         id = params["id"]
#         body = request.get_json()
#         #item = getstuff(id)
#         # if item is distinguish, exit
#         pass

#     def delete(self):
#         params = request.args
#         id = params["id"]
#         body = request.get_json()
#         #item = getstuff(id)
#         # if item is distinguish, exit
#         pass


'''
everybody, type, text, toplevel
{title, url, by, date, type, id}
parent_id, type
[{text, parent_id, date, by, comments}]
id, everything
'''
@api.route('/resources/')
@api.doc(get={'params':{
    'id':'',
    'type':'',
    'text':'',
    'parent_id':'',
    'page':'',
    'per_page':'',
}})
class Getitems(Resource):
    def get(self):
            # if ID is specified in the query params, return a single item with that matches the ID
            # else, return a list of items, retrieved from the Order table, then populated by type, paginated
            # params = request.args
            id = request.args.get('id', default = None)
            type = request.args.get('type', default = None)
            text = request.args.get('text', default = None)
            parent_id = request.args.get('parent_id', default = None)
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=20, type=int)
            if id:
                if type:
                    if type == 'story':
                        story = db.session.query(Story).get(id)
                        return jsonify({'num_comments':story.num_comments, 'title':story.title, 'url':story.url, 'author':story.by, 'date':story.date, 'type':story.post_type, 'id':story.id, 'score':story.score})

                    elif type == 'job':
                        job = db.session.query(Job).get(id)
                        return jsonify({'num_comments':job.num_comments, 'title':job.title, 'url':job.url, 'author':job.by, 'date':job.date, 'type':job.post_type, 'id':job.id, 'text':job.text})

                    elif type == 'poll':
                        poll = db.session.query(Poll).get(id)
                        return jsonify({'num_comments':poll.num_comments, 'title':poll.title, 'author':poll.by, 'date':poll.date, 'type':poll.post_type, 'id':poll.id, 'score':poll.score, 'text':poll.text})

                    elif type == 'polloption':
                        polloption = db.session.query(Polloption).get(id)
                        return jsonify({'num_comments':polloption.num_comments, 'author':polloption.by, 'date':polloption.date, 'type':polloption.post_type, 'id':polloption.id, 'score':polloption.score})

                    elif type == 'comment':
                        comment = db.session.query(Comment).get(id)
                        return jsonify({'num_comments':comment.num_comments,'text':comment.text, 'parent_item_id':comment.parent_id, 'author':comment.by, 'date':comment.date, 'type':comment.post_type, 'id':comment.id})

                    else:
                        return "Type not found", 400
                else:
                    return "Type not found", 400

            elif parent_id and type:
                returnval = []
                if type == 'story':
                    story = db.session.query(Story).get(parent_id)
                    comments = db.session.query(Comment).filter(Comment.parent_id == story.story_id).order_by(Comment.comment_index).all()
                    for c in comments:
                        entry = {'text':c.text, 'parent':parent_id, 'date':c.date, 'author':c.by, 'num_comments':c.num_comments}
                        returnval.insert(c.comment_index, entry)
                    return jsonify(returnval)

                elif type == 'job':
                    job = db.session.query(Job).get(parent_id)
                    comments = db.session.query(Comment).filter(Comment.parent_id == job.job_id).order_by(Comment.comment_index).all()
                    for c in comments:
                        entry = {'text':c.text, 'parent':parent_id, 'date':c.date, 'author':c.by, 'num_comments':c.num_comments}
                        returnval.insert(c.comment_index, entry)
                    return jsonify(returnval)

                elif type == 'poll':
                    poll = db.session.query(Poll).get(parent_id)
                    comments = db.session.query(Comment).filter(Comment.parent_id == poll.poll_id).order_by(Comment.comment_index).all()
                    for c in comments:
                        entry = {'text':c.text, 'parent':parent_id, 'date':c.date, 'author':c.by, 'num_comments':c.num_comments}
                        returnval.insert(c.comment_index, entry)
                    return jsonify(returnval)

                elif type == 'polloption':
                    polloption = db.session.query(Polloption).get(parent_id)
                    comments = db.session.query(Comment).filter(Comment.parent_id == polloption.polloption_id).order_by(Comment.comment_index).all()
                    for c in comments:
                        entry = {'text':c.text, 'parent':parent_id, 'date':c.date, 'author':c.by, 'num_comments':c.num_comments}
                        returnval.insert(c.comment_index, entry)
                    return jsonify(returnval)

                elif type == 'comment':
                    comment = db.session.query(Comment).get(parent_id)
                    comments = db.session.query(Comment).filter(Comment.parent_id == comment.comment_id).order_by(Comment.comment_index).all()
                    for c in comments:
                        entry = {'text':c.text, 'parent':parent_id, 'date':c.date, 'author':c.by, 'num_comments':c.num_comments}
                        returnval.insert(c.comment_index, entry)
                    return jsonify(returnval)

                else:
                    return jsonify(returnval)

            elif type and text:
                returnval = []
                if type == 'story':
                    story_pages = db.session.query(Story).filter(or_(Story.title.ilike(f'%{text}%'), Story.url.ilike(f'%{text}%'))).order_by(Story.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    story = story_pages.items
                    for i in story:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':story_pages.pages})

                elif type == 'job':
                    job_pages = db.session.query(Job).filter(or_(Job.title.ilike(f'%{text}%'), Job.url.ilike(f'%{text}%'), Job.text.ilike(f'%{text}%'))).order_by(Job.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    job = job_pages.items
                    for i in job:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':job_pages.pages})

                elif type == 'poll':
                    poll_pages = db.session.query(Poll).filter(or_(Poll.title.ilike(f'%{text}%'), Poll.text.ilike(f'%{text}%'))).order_by(Poll.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    poll = poll_pages.items
                    for i in poll:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':poll_pages.pages})

                else:
                    return jsonify({'data':returnval, 'total_pages':1})
                
            elif type:
                returnval = []
                if type == 'story':
                    story_pages = db.session.query(Story).order_by(Story.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    story = story_pages.items
                    for i in story:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':story_pages.pages})

                elif type == 'job':
                    job_pages = db.session.query(Job).order_by(Job.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    job = job_pages.items
                    for i in job:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':job_pages.pages})

                elif type == 'poll':
                    poll_pages = db.session.query(Poll).order_by(Poll.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                    poll = poll_pages.items
                    for i in poll:
                        entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                        returnval.append(entry)
                    return jsonify({'data':returnval, 'total_pages':poll_pages.pages})

                else:
                    return jsonify({'data':returnval, 'total_pages':1})
                
            elif text:
                returnval = []
                story = db.session.query(Story).filter(or_(Story.title.ilike(f'%{text}%'), Story.url.ilike(f'%{text}%'))).all()
                for i in story:
                    entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                    returnval.append(entry) 

                job = db.session.query(Job).filter(or_(Job.title.ilike(f'%{text}%'), Job.url.ilike(f'%{text}%'), Job.text.ilike(f'%{text}%'))).all()
                for i in job:
                    entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                    returnval.append(entry) 

                poll = db.session.query(Poll).filter(or_(Poll.title.ilike(f'%{text}%'), Poll.text.ilike(f'%{text}%'))).all()
                for i in poll:
                    entry = {'num_comments':i.num_comments, 'title':i.title, 'url':i.url, 'author':i.by, 'date':i.date, 'type':i.post_type, 'id':i.id}
                    returnval.append(entry)   
                
                returnval.sort(key=lambda c:c['date'], reverse=True)
                total = math.ceil(len(returnval)/per_page)
                start = (page - 1) * per_page
                stop = start + per_page + 1
                returnval = returnval[start:stop]
            
                return jsonify({'data':returnval,'total_pages':total})

            else:
                orders_pages = db.session.query(Order).order_by(Order.date.desc()).paginate(page=page, per_page=per_page,error_out=False)
                orders = orders_pages.items
                returnval = []
                for i in orders:
                    index = orders.index(i)
                    if i.item_type == 'story':
                        story = db.session.query(Story).filter(Story.story_id == i.item_id).first()
                        returnval.insert(index, {'num_comments':story.num_comments, 'title':story.title, 'url':story.url, 'author':story.by, 'date':story.date, 'type':story.post_type, 'id':story.id})

                    elif i.item_type == 'job':
                        job = db.session.query(Job).filter(Job.job_id == i.item_id).first()
                        returnval.insert(index, {'num_comments':job.num_comments, 'title':job.title, 'url':job.url, 'author':job.by, 'date':job.date, 'type':job.post_type, 'id':job.id})

                    elif i.item_type == 'poll':
                        poll = db.session.query(Poll).filter(Poll.poll_id == i.item_id).first()
                        returnval.insert(index, {'num_comments':poll.num_comments, 'title':poll.title, 'author':poll.by, 'date':poll.date, 'type':poll.post_type, 'id':poll.id})
                
                return jsonify({'data':returnval, 'total_pages':orders_pages.pages})


    def post(self):
        data = request.get_json()
        check = data.get('type')
        if check == 'job': 
            records = Job(post_type=check, by=data.get('author'), text=data.get('text'), url=data.get('url'), title=data.get('title'))
            db.session.add(records)
            db.session.commit()
            res = {'status':'success','type':records.post_type,'author':records.by,'title':records.title,'url':records.url,'text':records.text}
        elif check == 'story':
            records = Story(post_type=check, by=data.get('author'), url=data.get('url'), title=data.get('title'))
            db.session.add(records)
            db.session.commit()
            res = {'status':'success','type':records.post_type,'author':records.by,'title':records.title,'url':records.url}
        elif check == 'comment':
            records = Comment(post_type=check, by=data.get('author'), text=data.get('text'), title=data.get('title'))
            db.session.add(records)
            db.session.commit()
            res = {'status':'success','type':records.post_type,'author':records.by,'title':records.title,'text':records.text}
        elif check == 'poll':
            records = Poll(post_type=check, by=data.get('author'), text=data.get('text'), title=data.get('title'))
            db.session.add(records)
            db.session.commit()
            res = {'status':'success','type':records.post_type,'author':records.by,'title':records.title,'text':records.text}
        else:
            res = {'type': 'none'}
        return jsonify(res)

    def put(self):
        data_id = request.args.get('id')
        data_type = request.args.get('type')
        body = request.get_json()
        if data_type == 'job':
            jobs = db.session.query(Job).get(data_id)
            if not jobs.distinguish:
                jobs.by == body['author']
                jobs.title = body['title']
                jobs.text = body['text']
                jobs.url = body['url']
                db.session.commit()
                return jsonify({'status':'success'})
            return jsonify({'error': 'You are unauthorized to edit this data'})
        elif data_type == 'story':
            stories = db.session.query(Story).get(data_id)
            if not stories.distinguish:
                stories.by == body['author']
                stories.title = body['title']
                stories.url = body['url']
                db.session.commit()
                return jsonify({'status':'success'})
            return jsonify({'error': 'unauthorized to edit data'})
        elif data_type == 'comment':
            comments = db.session.query(Comment).get(data_id)  
            if not comments.distinguish:
                comments.by == body['author']
                comments.title = body['title']
                comments.text = body['text']
                db.session.commit()
                return jsonify({'status':'success'})
            return jsonify({'error': 'unauthorized to edit data'})
        elif data_type == 'poll':
            comments = db.session.query(Poll).get(data_id)
            if not comments.distinguish:
                comments.by == body['author']
                comments.title = body['title']
                comments.text = body['text']
                db.session.commit()
                return jsonify({'status':'success'})
            return jsonify({'error': 'unauthorized to edit data'})
        else:
            return jsonify({'supply type'}) 

    def delete(self):
        data_id = request.args.get('id')
        data_type = request.args.get('type')
        if data_type == 'job':
            jobs = db.session.query(Job).get(data_id)
            if not jobs.distinguish:
                db.session.delete(jobs)
                db.session.commit()
                return jsonify({'status':'Deleted successfully'})
            return jsonify({'error':'unauthorized to delete data'}) 
        elif data_type == 'story':
            stories = db.session.query(Story).get(data_id)
            if not stories.distinguish:
                db.session.delete(stories)
                db.session.commit()
                return jsonify({'status':'Deleted successfully'})
            return jsonify({'error':'unauthorized to delete data'})
        elif data_type == 'comment':
            comments = db.session.query(Comment).get(data_id)
            if not comments.distinguish:
                db.session.delete(comments)
                db.session.commit()
                return jsonify({'status':'Deleted successfully'})
            return jsonify({'error':'unauthorized to delete data'})
        elif data_type == 'poll':
            polls = db.session.query(Poll).get(data_id)
            if not polls.distinguish:
                db.session.delete(polls)
                db.session.commit()
                return jsonify({'status':'Deleted successfully'})
            return jsonify({'error':'unauthorized to delete data'})
        else:
            return jsonify({'supply type'})

