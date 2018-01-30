from app import make_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.model import db


app = make_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
