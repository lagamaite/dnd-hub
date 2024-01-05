from flask import Flask, render_template    
import jinja2  
import json
from note import Note 
app = Flask(__name__)

@app.route("/")
def home():
    # Test Note object
    n = Note("Title", "Description")
    print(n.title) # prints "Title" in terminal
    print(str(n.note_date)) # prints current date in terminal
    return render_template("index.html")
    
@app.route("/test")
def test():
    return "Test"
    
if __name__ == "__main__":
    app.run(debug=True)