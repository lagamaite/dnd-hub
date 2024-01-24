from base import db
class Stats(db.Model):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(100), nullable=False, unique=True) # character name 
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)

    # constructor function    
    def __init__(self, character, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.character = character
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


    def as_dict(self):

        return {
            "character": self.character,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }

    @staticmethod
    def get_all_stats():
        #returns stats of every character
        return Stats.query.all()
    
    #TODO: get stats of specific character