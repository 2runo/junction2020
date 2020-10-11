import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('credential/askkey-b0a35-firebase-adminsdk-ool7x-8a6a38d4a2.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://askkey-b0a35.firebaseio.com/'
})

#ref = db.reference('menus')
#print(ref.get())


def get_menu_idx(restaurant_name):
    n = restaurant_name.upper().encode()[0]
    if n <= 65+8:
        return 0
    elif n <= 65+8+8:
        return 1
    else:
        return 2

def get_menu(restaurant_name):
    idx = get_menu_idx(restaurant_name)
    path = 'menus' + str(idx)
    if idx == 0:
        path = 'menus'
    ref = db.reference(path)
    return ref.get()

