import numpy as np
import cv2
from capture_video import capture_video
from image_processing import process_image

    
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

def test_from_ipweb():
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
            result.write(img2)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
    
    result.release()
    print("video saved successfully")

if __name__ == '__main__': 
    # test_from_video()
    test_from_ipweb()