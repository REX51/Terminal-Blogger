from models.post import Post
from database import Database
from models.blog import Blog
from menu import Menu

_author_ = "Rahul Singha"

Database.initialise()

menu = Menu()

menu.run_menu()

