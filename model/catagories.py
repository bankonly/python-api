from config.db import db
from time import time
from helper.defaultfunc import DefaultFunc

class CatagoryModel(db.Model):
    __tablename__ = 'catagories'

    catId = db.Column(db.String(80),primary_key=True,nullable=False,default=DefaultFunc.generateId)
    catName = db.Column(db.String(50),nullable=False)
    
    createDate = db.Column(db.BigInteger,default=time)
    updateDate = db.Column(db.BigInteger,onupdate=time)

    product = db.relationship('ProductModel',lazy="dynamic")

    @classmethod
    def fetchAll(cls):
        return cls.query.all()

    @classmethod
    def findById(cls,catid):
        return cls.query.filter_by(catId=catid).first()

    @classmethod
    def findByName(cls,name):
        return cls.query.filter_by(catName=name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    





