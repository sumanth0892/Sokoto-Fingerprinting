import os 
import cv2
import numpy as np
dataPath = '/Volumes/DATASETS/SOCOFing/Real' 

def getData(w,path = dataPath):
	labels = []; i = 0
	images = np.ndarray(shape = (len(os.listdir(dataPath)),w,w,1),dtype = np.float32)
	for file in sorted(os.listdir(dataPath)):
		img = cv2.imread(path + '/' + file,0)
		img = cv2.resize(img,(w,w),interpolation = cv2.INTER_AREA)
		img = np.reshape(img,(w,w,1))
		images[i] = img 
		i += 1
		if '_M_' in file:
			if '_Right_' in file:
				if 'little' in file:
					labels.append(0)
					continue
				if 'ring' in file:
					labels.append(1)
					continue
				if 'middle' in file:
					labels.append(2)
					continue
				if 'index' in file:
					labels.append(3)
					continue
				if 'thumb' in file:
					labels.append(4)
					continue
			if '_Left_' in file:
				if 'little' in file:
					labels.append(9)
					continue
				if 'ring' in file:
					labels.append(8)
					continue
				if 'middle' in file:
					labels.append(7)
					continue
				if 'index' in file:
					labels.append(6)
					continue
				if 'thumb' in file:
					labels.append(5)
					continue
		if '_F_' in file:
			if '_Right_' in file:
				if 'little' in file:
					labels.append(10)
					continue
				if 'ring' in file:
					labels.append(11)
					continue
				if 'middle' in file:
					labels.append(12)
					continue
				if 'index' in file:
					labels.append(13)
					continue
				if 'thumb' in file:
					labels.append(14)
					continue
			if '_Left_' in file:
				if 'little' in file:
					labels.append(19)
					continue
				if 'ring' in file:
					labels.append(18)
					continue
				if 'middle' in file:
					labels.append(17)
					continue
				if 'index' in file:
					labels.append(16)
					continue
				if 'thumb' in file:
					labels.append(15)
					continue
	print(set(labels)) #Make sure we have all the labels from 0 to 19
	print(max(set(labels)))
	return images,labels 




