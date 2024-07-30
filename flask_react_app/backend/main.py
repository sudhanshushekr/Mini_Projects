# create
# -first name 
# last name 
# email
# password
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from config import app, db
from models import Contact


@app.route('/contacts', methods=['GET'])
def get_contacts():
    # uses flask sqlalchemy to query all contacts
    contacts = Contact.query.all() 
    json_contacts = map(lambda x: x.to_json(), contacts)
    return jsonify({"contacts ": json_contacts})


@app.route('/create_contacts', methods=['POST'])
def create_contact():   
   first_name = request.json['first_name']
   last_name = request.json['last_name']
   email = request.json['email']
   

   if not first_name or not last_name or not email:
       return (jsonify({'error': 'Missing information'}) ,
       400,
       )

    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'success': True}), 201
    
    












if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

# app.run(debug=True) # run the app in debug mode

