from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.userModel import User

class userSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password',)

user_schema = userSchema()