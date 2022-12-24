import numpy as np
import cv2
from capture_video import capture_video
from image_processing import process_image
from drive import drive


class control_bot:
    def __init__(self):
        self.actions = ['Stop', 'Forward', 'Backward','Turn Left', 'Turn Right', 'Adjust Left', 'Adjust Right']
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
    def set_action(self, key):
        self.actions_func[int(key)]()
    
    def select_action(self, err):
        if abs(err) <= 10 :
            print( self.actions[1])
            self.set_action(1)
        elif err > 0 :
            print( self.actions[5])
            self.set_action(5)
        else :
            print( self.actions[6])
            self.set_action(6)

def test_from_video():
    result = cv2.VideoWriter('./results/test1-op.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10, (640,480))
    cap = capture_video()
    cap.setup_video("./test_files/test1.mp4")
    while True:
        try :
            img = cap.video_input()
            img = cv2.resize(img, (640, 480))
            img2,err = process_image(img)
            cv2.imshow("test1-ip",img)
            cv2.imshow("test1-op",img2)
            result.write(img2)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
    
    result.release()
    print("video saved successfully")

def test_from_ipweb(write_video=False):
    print("here")
    if write_video :
        result = cv2.VideoWriter('./results/test2-op.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10, (640,480))
    cap = capture_video()
    cap.setup_ipcam("192.168.238.208")
    while True:
        try :
            img = cap.ipcam_input()
            img = cv2.resize(img, (640, 480))
            img2,err = process_image(img)
            cv2.imshow("test1-ip",img)
            cv2.imshow("test1-op",img2)
            cb.select_action(err)
            if write_video:
                result.write(img2)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
    if write_video:
        result.release()
        print("video saved successfully")

def test_from_web(write_video=False):
    print("here")
    if write_video :
        result = cv2.VideoWriter('./results/test2-op.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10, (640,480))
    cap = capture_video()
    cap.setup_webcam()
    cb = control_bot()
    while True:
        try :
            img = cap.webcam_input()
            img = cv2.resize(img, (640, 480))
            img2,err = process_image(img)
            cv2.imshow("test1-ip",img)
            cv2.imshow("test1-op",img2)
            cb.select_action(err)
            if write_video:
                result.write(img2)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
    if write_video:
        result.release()
        print("video saved successfully")
if __name__ == '__main__': 
    # test_from_video()
    test_from_web()
