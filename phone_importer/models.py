from mongoengine import Document, StringField

class PhoneNumber(Document):
    phone_number = StringField(required=True)
