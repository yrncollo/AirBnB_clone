#!/usr/bin/python4
from models import base_model, state, city, amenity, place, review, user
from models.engine import file_storage


BaseModel = base_model.BaseModel
State = state.State
storage = file_storage.FileStorage()
storage.reload()
City = city.City
User = user.User
Amenity = amenity.Amenity
Place = place.Place
Review = review.Review
classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}
