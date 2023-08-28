from flask import Flask
from firebase import firebase
app = Flask(__name__)

# Initialize Firebase
firebase = firebase.FirebaseApplication(
    'https://chatbot-395213-default-rtdb.asia-southeast1.firebasedatabase.app', None)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/<string:username>/account")
def get_accounts(username):
    # Get accounts from the Firebase Realtime Database
    return firebase.get('/{username}/account', None)

if __name__ == "__main__":
    app.run()
