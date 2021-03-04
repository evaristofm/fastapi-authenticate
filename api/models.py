from tortoise.models import Model
from passlib.hash import bcrypt
from tortoise import Tortoise, fields 


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)

    items = fields.ReverseRelation['Item']

    @classmethod
    async def get_user(cls, username):
        return cls.get(username=username)
    
    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)


class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(150)

    user_id: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="items"
    )

Tortoise.init_models(['api.models'], 'models')
