#!/usr/bin/python3
from models import base_model, state, city
from models.engine import file_storage


BaseModel = base_model.BaseModel
State = state.State
storage = file_storage.FileStorage()
storage.reload()
City = city.City
