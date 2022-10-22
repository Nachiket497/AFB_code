import RPi.GPIO as gpio
import time
from drive import drive
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

"""
0 = stop
1 = forward
2 = backward
3 = turn left
4 = turn right
5 = adjust left
6 = adjust right
"""


class manual_control:
    # connect to firebase
    def __init__(self, path, databaseURL):
        self.actions = ['Stop', 'Forward', 'Backward',
                        'Turn Left', 'Turn Right', 'Adjust Left', 'Adjust Right']
        self.drive = drive()
        self.actions_func = {
            0: self.drive.stop,
            1: self.drive.forward,
            2: self.drive.backward,
            3: self.drive.turn_left,
            4: self.drive.turn_right,
            5: self.drive.adjust_left,
            6: self.drive.adjust_right
        }
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred, {'databaseURL': databaseURL})
        self.ref = db.reference("/manual_mode")
        initial_dict = {"InputKey": 0}
        self.ref.set(initial_dict)
        self.ref.listen(self.listener)

    def get_input(self):
        return self.ref.get()["InputKey"]

    def set_input(self, input):
        self.ref.update({"InputKey": input})
    def listener(self, event):

        if event.data is None:
            print("Erorr: No data")
        else:
            if type(event.data) is dict:
                print("Initial data ", event.data)
            else:
                print(event.data)
                print(self.actions[event.data])
                self.actions_func[event.data]()


if __name__ == "__main__":
    url = "https://afb-1-3a64c-default-rtdb.firebaseio.com/"
    manual_control("./FirebaseKey.json", url)
