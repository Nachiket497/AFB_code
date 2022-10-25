import numpy as np
import cv2
import urllib.request

class capture_video:
    def __init__(self, mode=0):
        self.mode = mode

    def setup_webcam(self):
        self.cap = cv2.VideoCapture(0)

    def webcam_input(self):
        ret, frame = self.cap.read()
        return frame

    def destroy_webcam(self):
        self.cap.release()
        cv2.destroyAllWindows()


    def setup_ipcam(self, ip):
        self.url = "http://"+ip+":8080/shot.jpg?rnd=946321" 
        print("setup done successfully")

    def ipcam_input(self):
        try :
            self.imgResp = urllib.request.urlopen(self.url)
            self.imgNp = np.array(bytearray(self.imgResp.read()),dtype=np.uint8)
            self.frame = cv2.imdecode(self.imgNp,-1)
            print("capturing frame")
            return cv2.resize(self.frame, (640, 480))
        except Exception as e:
            print("Error in capturing frame")
            print(e)
            return np.zeros((640,480)) 

    def setup_video(self, filename):
        self.cap = cv2.VideoCapture(filename)

    def video_input(self):
        return self.webcam_input()

        

if __name__ =="__main__":
    cap = capture_video()
    # cap.setup_ipcam("192.168.94.144")

    # while True :
    #     try :
    #         img = cap.ipcam_input()
    #         cv2.imshow( 'test' , img )
    #         cv2.waitKey(10)
    #     except KeyboardInterrupt:
    #         cv2.destroyAllWindows()
    #         break

    cap.setup_webcam()

    while True :
        try :
            img = cap.webcam_input()
            cv2.imshow( 'test' , img )
            cv2.waitKey(10)
        except KeyboardInterrupt:
            cap.destroy_webcam()
            break
