from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from sqlalchemy.exc import OperationalError
from config.app import app
from helper.handleexception import HandleExcetion
from sqlalchemy.orm.exc import UnmappedInstanceError

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


metaconvention = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metaconvention)

migrate = Migrate(app,db,render_as_batch=True)



@app.errorhandler(OperationalError)
def handle_http_exception(error):
    return HandleExcetion.output(error),500

@app.errorhandler(UnmappedInstanceError)
def handle_http_exception(error):
    return HandleExcetion.output(error),500