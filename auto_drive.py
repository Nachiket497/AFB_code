import numpy as np
from capture_video import capture_video
from drive import drive
from image_processing import process_image


class auto_drive :
    def __init__(self):
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

        self.cap = capture_video()

        self.cap.setup_webcam()


    def drive():
        while True:
            frame = self.cap.webcam_input()
            img = cv2.resize(frame, (640, 480))
            img2,err = process_image(img)
            if err == 0:
                self.drive.forward()
            elif err > 0 :
                self.drive.adjust_left()
            elif err < 0 :
                self.drive.adjust_right()
            else :
                self.drive.stop()
            cv2.imshow("frame", img2)
            cv2.waitKey(1)
        

if __name__ == "__main__":
    ad = auto_drive()
    ad.drive()