from flask_app.controllers import burgers
#connecting our controllers file
#no need to cneect models file since it already connected through the controllers file
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)