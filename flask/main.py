from flask import Flask # min import is important

app = Flask(__name__) # Creating an object

if __name__ == '__main__': # True(auto)
    app.run()
