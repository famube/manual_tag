from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import mantag, db
mantag.config.from_object('config')
migrate = Migrate(mantag, db)
manager = Manager(mantag)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
