from datetime import date
class Note:
    title = "" # note title 
    description = "" # body text of note 
    note_date = None # will always auto fill with current date 

    # constructor function    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.note_date = date.today()