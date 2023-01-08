from extensions import *
from os import path
from model.models import User, Post, Comment, Like
from routes.views import views
from routes.auth import auth



# basedir=os.path.dirname(os.path.realpath(__file__))


DB_NAME = "database.db"



def create_app():
    
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'user.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = "helloworld"
    db.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    with app.app_context():
        db.create_all()
        
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    # create_database(app)

    return app


# def create_database(app):
#     if not path.exists("blogapp/" + DB_NAME):
#         with app.app_context():
#          db.create_all(app)
#         print("Created database!")