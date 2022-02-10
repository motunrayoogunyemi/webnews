import requests
# from projectapp import create_app
from projectapp.mymodels import Job, Comment, Poll, Polloption, Story, db, Order

from projectapp import app, db

# db.init_app(app=create_app())

def ProcessListOfItems(rel_list):
    if type(rel_list) is not list:
        return

    for i in rel_list:
        AssignIntoTables(i)
    return

def GetLatestHundredItems():
    url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    latest_id = int(response.text)
    last_100 = latest_id - 100
    return range(last_100, latest_id)
            
def AssignIntoTables(i):
    # if item exists in any table, skip, to avoid duplicates
    if ItemExists(i) :
        return

    # retrive item if it doesn't exist
    the_item = GetItem(i)
    if(the_item.get("type") == "story"):
        #save in db, Order table and Story table
        
        # add to story
        records = Story(
            story_id = str(i), 
            deleted = the_item.get("deleted"),
            post_type = the_item.get("type"),
            by = the_item.get("by"),
            date = the_item.get("time"),
            dead = the_item.get("dead"),
            descendants = the_item.get("descendants"),
            score = the_item.get("score"),
            url = the_item.get("url"),
            title = the_item.get("title"),
            distinguish = True
            )
        db.session.add(records)
        
        # add to Order
        orderRecord = Order(
            item_id = str(i),
            item_type = the_item.get("type"),
            date = the_item.get("time")
            )
        db.session.add(orderRecord)

        db.session.commit()
        # retrieve all kids and add to comments
        ShareIntoTable(the_item.get("kids"), the_item.get("type"), the_item.get("id"))
        
    elif(the_item.get("type") == "job"):
        #save in db, Order table and Job table
        # add to job
        records = Job(
            job_id = str(i),
            deleted = the_item.get("deleted"),
            post_type = the_item.get("type"),
            by = the_item.get("by"),
            date = the_item.get("time"),
            dead = the_item.get("dead"),
            text = the_item.get("text"),
            url = the_item.get("url"),
            title = the_item.get("title"),
            distinguish = True
        )
        db.session.add(records)

        # add to order
        orderRecord = Order(
            item_id = str(i),
            item_type = the_item.get("type"),
            date = the_item.get("time")
            )
        db.session.add(orderRecord)

        db.session.commit()
        # retrieve all kids and add to comments
        ShareIntoTable(the_item.get("kids"), the_item["type"], the_item["id"])
        
    elif(the_item.get("type") == "poll"):
        #save in db, Order table and Poll table
        # add to Poll
        records = Poll(
            poll_id = str(i),
            deleted = the_item.get("deleted"),
            post_type = the_item.get("type"),
            by =the_item.get("by"),
            date = the_item.get("time"),
            dead = the_item.get("dead"),
            descendants = the_item.get("descendants"),
            score = the_item.get("score"),
            text = the_item.get("text"),
            title = the_item.get("title"),
            distinguish = True
        )

        db.session.add(records)

        # add to order
        orderRecord = Order(
            item_id = str(i),
            item_type = the_item.get("type"),
            date = the_item.get("time")
            )
        db.session.add(orderRecord)

        db.session.commit()
        # retrieve all kids and add to comments
        ShareIntoTable(the_item.get("kids"), the_item["type"], the_item["id"])
        # retrieve all pollopts and add to pollopts
        ShareIntoTable(the_item["parts"], the_item["type"], the_item["id"])
        
    elif(the_item.get("type") == "pollopt"):
        #save in db, Pollopt table
        # add to Pollopt
        parentItem = GetItem(the_item.get("parent"))
        polloptRecord = Polloption(
            polloption_id = str(i),
            deleted = the_item.get("deleted"),
            post_type = the_item.get("type"),
            by = the_item.get("by"),
            date = the_item.get("time"),
            dead = the_item.get("dead"),
            parents = the_item.get("parent"),
            score = the_item.get("score"),
            distinguish = True,
            poll_position = parentItem["kids"].index(i)
        )

        db.session.add(polloptRecord)

        db.session.commit()
        # retrieve all kids and add to comments
        ShareIntoTable(the_item.get("kids"), the_item["type"], the_item["id"])
        
    elif(the_item.get("type") == "comment"):
        #save in db, Comment table
        # add to Comment
        parentItem = GetItem(the_item.get("parent"))
        commentRecord = Comment(
            comment_id = str(i),
            deleted = the_item.get("deleted"),
            post_type = the_item.get("type"),
            by = the_item.get("by"),
            date = the_item.get("time"),
            dead = the_item.get("dead"),
            parent_id = the_item.get("parent"),
            text = the_item.get("text"),
            distinguish = True,
            comment_index = parentItem["kids"].index(i)
        )

        db.session.add(commentRecord)

        db.session.commit()
        # retrieve all kids and add to comments
        ShareIntoTable(the_item.get("kids"), the_item["type"], the_item["id"])

    return
    
def GetItem(id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def ShareIntoTable(item_array, item_type, parent_id):
    if type(item_array) is not list:
        return

    # assign by type
    if item_type == "comment":
        # loop through array
        # make sure to insert parent_id
        if len(item_array) > 0:
            for i in item_array:
                if ItemExists(i):
                    continue

                commentItem = GetItem(i)
                commentRecord = Comment(
                    comment_id = str(i),
                    deleted = commentItem.get("deleted"),
                    post_type = commentItem.get("type"),
                    by = commentItem.get("by"),
                    date = commentItem.get("time"),
                    dead = commentItem.get("dead"),
                    parent_id = parent_id,
                    text = commentItem.get("text"),
                    distinguish = True,
                    comment_index = item_array.index(i)
                )

                db.session.add(commentRecord)
                db.session.commit()

                ShareIntoTable(commentItem.get("kids"), commentItem.get("type"), str(i))        
            
    elif item_type == "pollopt":
        # loop through array
        # make sure to insert parent_id
        if len(item_array) > 0:
            for i in item_array:
                if ItemExists(i):
                    continue

                polloptItem = GetItem(i)
                polloptRecord = Polloption(
                    polloption_id = str(i),
                    deleted = polloptItem.get("deleted"),
                    post_type = polloptItem.get("type"),
                    by = polloptItem.get("by"),
                    date = polloptItem.get("time"),
                    dead = polloptItem.get("dead"),
                    parents = parent_id,
                    score = polloptItem.get("score"),
                    distinguish = True,
                    poll_position = item_array.index(i)
                )

                db.session.add(polloptRecord)
                db.session.commit()

                ShareIntoTable(polloptRecord.get("kids"), polloptRecord.get("type"), str(i))

    return

def ItemExists(id):
    item_in_jobs = db.session.query(Job.id).filter(Job.job_id == str(id))
    bool_item_in_jobs = db.session.query(item_in_jobs.exists()).scalar()

    item_in_comments = db.session.query(Comment.id).filter(Comment.comment_id == str(id))
    bool_item_in_comments = db.session.query(item_in_comments.exists()).scalar()

    item_in_stories = db.session.query(Story).filter(Story.story_id == str(id))
    bool_item_in_stories = db.session.query(item_in_stories.exists()).scalar()

    item_in_polls = db.session.query(Poll).filter(Poll.poll_id == str(id))
    bool_item_in_polls = db.session.query(item_in_polls.exists()).scalar()

    item_in_polloptions = db.session.query(Polloption).filter(Polloption.polloption_id == str(id))
    bool_item_in_polloptions = db.session.query(item_in_polloptions.exists()).scalar()

    return bool_item_in_comments or bool_item_in_jobs or bool_item_in_polloptions or bool_item_in_polls or bool_item_in_stories

def GetUser(id):
    url = f"https://hacker-news.firebaseio.com/v0/user/{id}.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetTopStories():
    url = f"https://hacker-news.firebaseio.com/v0/topstories.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetNewStories():
    url = f"https://hacker-news.firebaseio.com/v0/newstories.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetAskStories():
    url = f"https://hacker-news.firebaseio.com/v0/askstories.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetShowStories():
    url = f"https://hacker-news.firebaseio.com/v0/showstories.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetJobStories():
    url = f"https://hacker-news.firebaseio.com/v0/jobstories.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

def GetUpdates():
    url = f"https://hacker-news.firebaseio.com/v0/updates.json"
    params = {"print":"pretty"}
    response = requests.get(url,params)
    return response.json()

ProcessListOfItems(GetLatestHundredItems())
ProcessListOfItems(GetJobStories())
ProcessListOfItems(GetShowStories())
ProcessListOfItems(GetAskStories())
ProcessListOfItems(GetNewStories())
ProcessListOfItems(GetTopStories())
