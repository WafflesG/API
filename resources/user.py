# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:07:56 2020

@author: benny
"""

from flask_restful import Resource, reqparse
from models.user import UserModel

    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', 
        type=str, 
        required=True, 
        help="this field cannot be left blank")
    parser.add_argument(
        'password', 
        type=str, 
        required=True, 
        help="this field cannot be left blank")
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']): #if is not None
            return {"message": "username already exists"},400        
               
        user = UserModel(**data) #(data['username'], data['password'])
        user.save_to_db()
        
        return {'message': 'User has been created'}, 201
 