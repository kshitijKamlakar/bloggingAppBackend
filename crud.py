from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Blog, Base

DATABASE_URI = 'postgres+psycopg2://postgres:kshitij.in@localhost:5432/postgres'
engine = create_engine(DATABASE_URI)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)


def getAllBlogs():
    s = session()
    blogs = s.query(Blog).all()
    s.close()
    return blogs


def getBlogById(id):
    s = session()
    blog = s.query(Blog).filter(Blog.blog_id == id).one()
    s.close()
    return blog


def addBlog(blog):
    s = session()
    s.add(blog)
    s.commit()
    new_id = blog.blog_id
    s.close()
    return new_id


def updateBlog(blogJson):
    s = session()
    existing_blog = s.query(Blog).filter(Blog.blog_id == blogJson['blogId']).one()
    existing_blog.blog_title = blogJson['blogTitle']
    existing_blog.blog_content = blogJson['blogContent']
    s.add(existing_blog)
    s.commit()
    s.close()
    return True


def deleteBlog(id):
    s = session()
    blog = s.query(Blog).filter(Blog.blog_id == id).one()
    s.delete(blog)
    s.commit()
    s.close()
    return True
