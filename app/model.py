#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

from pydantic import BaseModel
from enum import Enum

class RegisterObject(BaseModel):
    name : str 
    age : int
    phone_number : str

class Genre(str, Enum):
    action = "action"
    sci_fi = "sci-fi"
    romantic = "romantic"
    musical = "musical"
    horror = "horror"
    drama = "drama"
    adult = "adult"

class MoviesObject(BaseModel):
    name : str 
    genre : Genre

class RemoveMoviesObject(BaseModel):
    name : str
    movie_id : str
 