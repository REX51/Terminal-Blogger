from database import Database
from models.blog import Blog
from models.post import Post


class Menu(object):
    def __init__(self):
        self.user = input("Enter your Name:")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['b_id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter your blog title:")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_write = input("Do you want to read (R) or write (W) blog? ")
        if read_write == 'R' or read_write == 'r':
            self._list_blogs()
            self._view_blog()
        elif read_write == 'W' or read_write == 'w':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging.")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {},Title: {}, Author: {}".format(blog['b_id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the Id of the blog you would like to read:")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("Date: {}, Title: {}\n\n{}".format(post['create_date'], post['title']. post['content']))

