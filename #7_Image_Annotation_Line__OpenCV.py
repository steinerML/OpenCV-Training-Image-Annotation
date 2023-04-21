import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Print error message if image is null
if img is None:
    print('Could not read image')
else:
    print('Image displaying correctly.')
#We make a copy of the image so changes don't affect the original
imageLine = img.copy()
#Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
#Call line() function
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
# Display Images
cv2.imshow('Original Image',img)
cv2.imshow('Image Line', imageLine)
#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows() 