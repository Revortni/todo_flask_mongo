from mongoengine import StringField, Document, BooleanField, DateTimeField
from datetime import datetime
from db import mongo_db

mongo_db.db_manager.connect("default")


class Todo(Document):
    meta = {'collection': 'todos'}
    title = StringField(required=True)
    description = StringField()
    completed = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
