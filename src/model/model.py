from src.config.database import *

ma = Marshmallow(app)

class Person(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64))

    def __init__(self, name):
        self.name = name

database.create_all()

class PersonSchema(ma.Schema):

    class Meta:
        fields = ('id','name')

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)