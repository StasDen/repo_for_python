from crypt import methods
import re
from main import app # From main.py we're using an object 'app'

@app.route("/") # '@' to use 'app'("when '/' use 'index'")

def index():
    return "Hooray"

@app.route('/fish/<id>') # Without 'env'
def get_fish(id):
    print(id)
    return "My fish is gorgeous!"

@app.route("/fish") # "Def inquiry"
def get_all_fishes():
    return "all fishes"

@app.route("/fish", methods=["POST"]) # 'Return' is important 
def create_fish():
    print("Fish created")
    return "Created fish"
