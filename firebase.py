# import pyrebase
# import os

# filelist = [f for f in os.listdir("/") if f.endswith(".jpg")]
# for f in filelist:
#     os.remove(os.path.join("/",f))
# config = {
#   "apiKey": "AIzaSyAJHxR4GOId3JF1Cy7qtLIavRnMNES1Qcc",
#   "authDomain": "gender-c5370.firebaseapp.com",
#   "projectId": "gender-c5370",
#   "storageBucket": "gender-c5370.appspot.com",
#   "serviceaccount":"serviceaccountkey.json",
#   "databaseURL" : ""
# };
# # cred = credentials.Certificate("./serviceaccountkey.json")
# firebase_storage=pyrebase.initialize_app(config)
# storage=firebase_storage.storage()
# # storage.child("images/me.jpg").put("me.jpg")
# # storage.child("myself.jpg").download("me.jpg",filename=os.getcwd)
# storage.child("images/me.jpg").get_url()
# # import firebase_admin
# # from firebase_admin import credentials

# # cred = credentials.Certificate("serviceaccountkey.json")
# # firebase_admin.initialize_app(cred)