from flask import Flask, request
from firebase import firebase
import random
import bcrypt  # Import the bcrypt library
app = Flask(__name__)

# Initialize Firebase
firebase = firebase.FirebaseApplication(
    'https://chatbot-395213-default-rtdb.asia-southeast1.firebasedatabase.app', None)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/get_all")
def get_all():
    # Get all details from the Firebase Realtime Database
    return firebase.get('', None)

@app.route("/<string:username>/<string:password>")
def get_customer_password(username, password):
    # Get customer password from the Firebase Realtime Database
    stored_password_hash = firebase.get(f'/{username}/password', None)
    
    if stored_password_hash is not None and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
        return {"status": "success"}
    else:
        return {"status": "failure"}

@app.route("/<string:username>/account")
def get_accounts(username):
    # Get accounts from the Firebase Realtime Database
    return firebase.get(f'/{username}/account', None)

@app.route("/<string:username>/apply_loan", methods=['POST'])
def apply_loan(username):
    # Assuming you receive loan type in the request JSON
    data = request.get_json()
    loan_type = data.get('loan_type')

    # Generate a random 3-digit number for the loan status
    loan_number = random.randint(100, 999)

    # Add loan type and status to the Firebase Realtime Database
    loan_data = {
        loan_number: {
            'loan_type': loan_type,
            'loan_status': 0
        }
    }

    firebase.patch(f'/{username}/loan', loan_data)

    return {"status": "success"}

if __name__ == "__main__":
    app.run()
