from database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, title, content, author, blog_id, date=datetime.datetime.utcnow(), p_id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.p_id = uuid.uuid4().hex if p_id is None else p_id
        self.create_date = date

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'blog_id': self.blog_id,
            'p_id': self.p_id,
            'create_date': self.create_date,

        }

    @classmethod
    def from_mongo(cls, p_id):
        post_data = Database.find_one(collection='posts', query={'p_id': p_id})
        return cls(title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   blog_id=post_data['blog_id'],
                   date=post_data['create_date'],
                   p_id=post_data['p_id'])

    @staticmethod
    def from_blog(p_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': p_id})]
