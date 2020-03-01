from firebase import firebase 
import config

# gets the firebase project
firebase = firebase.FirebaseApplication(config.firebase_endpoint, None)

# the hard coded data I want to post
data = {
    'name': 'Hello world',
}

# POST request to the database
result = firebase.post(config.endpoint, data)
