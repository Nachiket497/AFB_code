import numpy as np
import cv2
from capture_video import capture_video
from image_processing import process_image
import time
    
def test_from_video():
    result = cv2.VideoWriter('./results/test1-op.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10, (1280,480))
    cap = capture_video()
    cap.setup_video("./test_files/test3.mp4")
    total_time, total_frames = 0, 0
    while True:
        try :
            img = cap.video_input()
            img = cv2.resize(img, (640, 480))
            start = time.time()
            img2,err = process_image(img)
            end = time.time()
            print("frames: ", total_frames, "time taken: ",end-start)
            op_img = np.concatenate((img, img2), axis=1)
            cv2.imshow("test1-op",op_img)
            result.write(op_img)
            cv2.waitKey(1)
            total_time += end-start
            total_frames += 1
        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break
        except :
            cv2.destroyAllWindows()
            break
    
    result.release()
    print("video saved successfully")
    print("total frames: ",total_frames)
    print("total time taken: ",total_time)
    print("average time taken: ",total_time/total_frames)
    print("average fps: ",total_frames/total_time)

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
    test_from_video()
    # test_from_ipweb()