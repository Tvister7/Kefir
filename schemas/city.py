from tortoise.contrib.pydantic import pydantic_model_creator
from models.city import City

CitiesHintModelPydantic = pydantic_model_creator(City, name="CitiesHintModel")
