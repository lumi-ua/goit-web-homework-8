from mongoengine import *

connect(host='mongodb+srv://goitlearn:<password>@cluster0.gud02oa.mongodb.net/?retryWrites=true&w=majority')

class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent_email = BooleanField(default=False)
