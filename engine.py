import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
creddict = {
  # Your Credentials dictionary for your firebase database!
}

cred = credentials.Certificate(creddict)
firebase_admin.initialize_app(cred,{
    'databaseURL': 'Your Database link'
})

class Engine:

    def __init__(self, code):
        self.ref = db.reference("/"+code)
        self.database = self.ref.get()
    def change_code(self, code):
        self.ref = db.reference("/"+code)
        self.database = self.ref.get()
    def send_message(self, username:str, message:str):
        self.ref.push((username,message))
        self.database = self.ref.get()

    def get_all_messages(self):
        self.database = self.ref.get()
        if self.database:
            return self.database.values()
        return [("","")]

