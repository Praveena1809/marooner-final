import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1],1)
img2 = cv2.imread(sys.argv[2],1)

h = img.shape[0]
w = img.shape[1]

check = 0

L = 0
L1 = 0

for j in range(img.shape[1]):
	for i in range(img.shape[0]):
		if(img[i][j][0] != img[0][0][0] or img[i][j][1] != img[0][0][1] or img[i][j][2] != img[0][0][2]):
			L = j
			check=1
			break
	if (check!=0):
		break
check=0
for j in range(img2.shape[1]):
	for i in range(img2.shape[0]):
		if(img2[i][j][0] != img2[0][0][0] or img2[i][j][1] != img2[0][0][1] or img2[i][j][2] != img2[0][0][2]):
			L2 = j
			check=1
			break
	if (check!=0):
		break
start = [0 for i in range(img.shape[1])]
start2= [0 for i in range(img2.shape[1])]
end = [0 for i in range(img.shape[1])]
end2= [0 for i in range(img2.shape[1])]
for j in range(L,img.shape[1]):
	check=0
	for i in range(img.shape[0]):
		if(check==0 and (img[i][j][0] != img[0][0][0] or img[i][j][1] != img[0][0][1] or img[i][j][2] != img[0][0][2])):
			start[j]=i
			check=1
		elif(check==1 and (img[i][j][0] == img[0][0][0] and img[i][j][1] == img[0][0][1] and img[i][j][2] == img[0][0][2])):
			end[j]=i
			break
for j in range(L2,img2.shape[1]):
	check=0
	for i in range(img2.shape[0]):
		if(check==0 and (img2[i][j][0] != img2[0][0][0] or img2[i][j][1] != img2[0][0][1] or img2[i][j][2] != img2[0][0][2])):
			start2[j]=i
			check=1
		elif(check==1 and (img2[i][j][0] == img2[0][0][0] and img2[i][j][1] == img2[0][0][1] and img2[i][j][2] == img2[0][0][2])):
			end2[j]=i
			break

pp = [0,0,0]
for j in range(L,img.shape[1]):
	for i in range(start[j],end[j]+1):
		try:
			if(img2[start2[j+L2-L]+i-start[j]][j+L2-L][0]!=0 or img2[start2[j+L2-L]+i-start[j]][j+L2-L][1]!=0 or img2[start2[j+L2-L]+i-start[j]][j+L2-L][2]!=0):
				img[i][j]=img2[start2[j+L2-L]+i-start[j]][j+L2-L]
		except:
			pass

cv2.imwrite("tempsaved.png",img)