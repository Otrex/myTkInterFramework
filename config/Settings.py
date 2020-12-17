import os
import hashlib

# The is the root directory of our project
BASE_DIR = os.path.abspath(os.getcwd())

# This is where onts would be specified
LARGE_FONT = ("Verdana", 12)
OTHER_FONTS = {
	# FONT_ID : (FONT, SIZE)
}

# This is the Logo section of the project
LOGO = 'logo.png'

# This is the intial title
TITLE = 'CREATE A BOOK'

# Password Hasher
HASHER = hashlib.sha256

# DataBase Settings
DB_NAME = 'myDB.db'
DB_HOST = 'sqlite:///' + BASE_DIR + '//' + DB_NAME

