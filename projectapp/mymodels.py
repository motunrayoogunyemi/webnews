import datetime

from projectapp import db

class Job(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    job_id = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    post_type = db.Column(db.String(30),nullable=False)
    by = db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    dead = db.Column(db.Boolean, default=False, nullable=False)
    text = db.Column(db.String(5000),nullable=True)
    url = db.Column(db.String(150),nullable=True)
    title = db.Column(db.String(150),nullable=True)
    distinguish = db.Column(db.Boolean, default=False, nullable=False)

class Story(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    story_id = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    post_type = db.Column(db.String(30),nullable=False)
    by = db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    dead = db.Column(db.Boolean, default=False, nullable=False)
    descendants = db.Column(db.Integer(), nullable=True)
    score = db.Column(db.Integer(), nullable=True)
    url = db.Column(db.String(150),nullable=True)
    title = db.Column(db.String(150),nullable=True)
    distinguish = db.Column(db.Boolean, default=False, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    comment_id = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    post_type = db.Column(db.String(30),nullable=False)
    by = db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    dead = db.Column(db.Boolean, default=False, nullable=False)
    parent_id = db.Column(db.Integer(), nullable=True)
    text = db.Column(db.String(5000),nullable=True)
    distinguish = db.Column(db.Boolean, default=False, nullable=False)
    comment_index = db.Column(db.Integer(), nullable=False)

class Poll(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    poll_id = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    post_type = db.Column(db.String(30),nullable=False)
    by = db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    dead = db.Column(db.Boolean, default=False, nullable=False)
    descendants = db.Column(db.Integer(), nullable=True)
    score = db.Column(db.Integer(), nullable=True)
    text = db.Column(db.String(5000),nullable=True)
    title = db.Column(db.String(150),nullable=True)
    distinguish = db.Column(db.Boolean, default=False, nullable=False)

class Polloption(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    polloption_id = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    post_type = db.Column(db.String(30),nullable=False)
    by = db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    dead = db.Column(db.Boolean, default=False, nullable=False)
    parents = db.Column(db.Integer(), nullable=True)
    score = db.Column(db.Integer(), nullable=True)
    distinguish = db.Column(db.Boolean, default=False, nullable=False)
    poll_position = db.Column(db.Integer(), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    item_id = db.Column(db.String(30), nullable=False)
    item_type = db.Column(db.String(30),nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)