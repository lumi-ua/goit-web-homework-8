from mongoengine import *

connect(host='mongodb+srv://goitlearn:<password>@cluster0.gud02oa.mongodb.net/?retryWrites=true&w=majority')

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()

