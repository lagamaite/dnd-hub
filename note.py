from datetime import date
from base import db
class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True) # note title 
    description = db.Column(db.String(500), nullable=False, unique=True) # body text of note 
    note_date = None # will always auto fill with current date 

    # constructor function    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.note_date = date.today()