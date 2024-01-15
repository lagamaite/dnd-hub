from datetime import date
from base import db
from sqlalchemy.dialects.mysql import LONGTEXT
#TODO: figure out how to store large text
class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True) # note title 
    description = db.Column(db.String(100), nullable=False, unique=True) # body text of note 
    note_date = db.Column(db.String(100)) # will always auto fill with current date 

    # constructor function    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.note_date = date.today()