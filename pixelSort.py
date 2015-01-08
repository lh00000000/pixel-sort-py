import numpy as np
import cv2
from enum import Enum
import colorsys

class pixelSortMode(Enum):
	blackmode = 0
	brightmode = 1
	whitemode = 2

blackValue = -10000000
brigthnessValue = 60
whiteValue = -6000000

def getNextBlackX(img,_x,_y):
	x = _x+1
	y = _y

	width = img.shape[1]

	for x in range(width):
		rgb = img[y][x]
		#hsv = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
		if (rgb < 80):
			return x
	return x-1 


def getLeftMostRed(img,_x,_y):
	x = _x+5
	y = _y

	width = img.shape[1]

	for i in range(width):
		rgb = img[y][i]
		#hsv = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
		if (rgb > 200):
			return i
	return x



def getLeftMostGreen(img,_x,_y):
	x = _x+5
	y = _y

	width = img.shape[1]

	for i in range(width):
		rgb = img[y][i]
		#hsv = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
		if (rgb < 60):
			return i
	return x


def sortRow(img, row, pixel_sort_mode):
	y = row
	
	x=0
	x = getLeftMostGreen(img,x,y)
	xend = getLeftMostRed(img,x,y)

	print "x: %d xend: %d" %(x,xend)
	px_unsorted_row = img[row][x:xend]
	px_sorted_row = np.sort(px_unsorted_row, axis=0)

	img[row][x:xend] = px_sorted_row

	return img


def sortColumn(img, column, pixel_sort_mode):
	x = column

	y = 0
	yend  = 0



def pixelSort(img, pixel_sort_mode=pixelSortMode.blackmode):

	for x in range(img.shape[1]-1):
		sortColumn(img,x,pixel_sort_mode)
	for y in range(img.shape[0]-1):
		img = sortRow(img,y,pixel_sort_mode)

	
	return img

if __name__ == '__main__':
	
	cap = cv2.VideoCapture(0)

	while(True):
		ret, frame = cap.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cray = pixelSort(gray)

		cv2.imshow('frame',cray)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()