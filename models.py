import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, VARCHAR, BIGINT, DATE
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()


class Blog(Base):
    __tablename__ = 'BlogDetail'

    blog_id = Column(BIGINT, autoincrement=True, primary_key=True)
    blog_title = Column(VARCHAR)
    blog_content = Column(VARCHAR)
    added_at_date = Column(DATE, default=datetime.date.today().strftime('%m/%d/%Y'))

    def __init__(self, blog_title, blog_content):
        self.blog_title = blog_title
        self.blog_content = blog_content
