from flask import Flask, render_template, request    
from flask_sqlalchemy import SQLAlchemy
import jinja2  
import json
from base import db
from note import Note 
# Creating Flask app
app = Flask(__name__)

# Manually create schema named "dndhub_db" in mysql workbench, change pin/password if needed
user = "root"
pin = "testpass"
host = "localhost"
db_name = "dndhub_db"

# Configuring database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{pin}@{host}/{db_name}"
 
# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing Flask app with SQLAlchemy
db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()

@app.route("/")
def home():
    # Test Note object
    # n = Note("Title", "Description")
    # print(n.title) # prints "Title" in terminal
    # print(str(n.note_date)) # prints current date in terminal

    #notes_list = Note.query.all()
    return render_template("index.html")
    
@app.route("/create", methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        note_title = request.form.get('title')
        note_description = request.form.get('description')
 
        new_note = Note(
            title=note_title,
            description=note_description
        )
        db.session.add(new_note)
        db.session.commit()
        #return redirect(url_for('home'))
        print(request.json)
 
    return render_template("index.html")
    
if __name__ == "__main__":
    create_db()
    app.run(debug=True)