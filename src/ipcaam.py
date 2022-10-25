import cv2
import numpy as np
import urllib.request

url = "http://192.168.94.144:8080/shot.jpg?rnd=946321" # paste your url here 
while True :
	imgResp = urllib.request.urlopen(url)	
	imgNp = np.array( bytearray( imgResp.read() ), dtype=np.uint8 )
	img = cv2.imdecode( imgNp , -1 )
	img = cv2.resize(img, (540, 340)) 
	cv2.imshow( 'test' , img )
	cv2.waitKey(10)