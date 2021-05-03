from src.model.model import *

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hola mundo"})

@app.route('/person', methods=['GET'])
def get_persons():
    all_persons = Person.query.all()
    result = persons_schema.dump(all_persons)
    return jsonify(result)

@app.route('/person/<id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    return person_schema.jsonify(person)

@app.route('/person', methods=['POST'])
def create_person():
    name = request.json['name']
    person = Person(name)

    database.session.add(person)
    database.session.commit()
    return person_schema.jsonify(person)

@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    name = request.json['name']
    person.name = name
    database.session.commit()
    return person_schema.jsonify(person)

@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    database.session.delete(person)
    database.session.commit()
    return person_schema.jsonify(person)

if __name__ == "__main__":
    app.run(debug=True)