# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:23:13 2020

@author: benny
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user is not None and safe_str_cmp(user.password, password):
        return user
    
    #user.password is getting the password attribute from the object user.
    #user was pointed at (based on the criteria in authentcate) to a matching object 
    #inside a composition created by username_mapping
    #this composition is key'd with username and its value is an object
    #the object in this comp was acq from the users list, where all items in this list
    #are the objects created in the user.py module
    
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


#users = [
 #   User(1,'bob', 'asdf')]

#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}
#users = [
 #   {'id':1,
  #  'username':'bob',
   # 'password':'asdf'      
    #}]

#username_mapping = {'bob':
 #   {'id':1,
  #  'username':'bob',
   # 'password':'asdf'      
    #}}

#userid_mapping = {1:
 #   {'id':1,
  #  'username':'bob',
   # 'password':'asdf'      
    #}}