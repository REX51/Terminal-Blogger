import uuid
import datetime
from models.post import Post
from database import Database


class Blog(object):
    def __init__(self, author, title, description, b_id = None):
        self.author = author
        self.title = title
        self.description = description
        self.b_id = uuid.uuid4().hex

    def new_post(self):
        title = input("Enter post title:")
        content = input("Enter post content:")
        date = input("Enter date, or leave blank for today(DDMMYY):")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.b_id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.b_id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author':self.author,
            'title': self.title,
            'description': self.description,
            'b_id': self.b_id
        }

    @classmethod
    def from_mongo(cls, b_id):
        blog_data = Database.find_one(collection='blogs', query={'b_id':b_id})
        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    b_id=blog_data['b_id'])

