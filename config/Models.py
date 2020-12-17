# Import all your models here
from models.User import User
from models.Person import Person


# This Creates all the database
from core.Database import create_all
create_all()
