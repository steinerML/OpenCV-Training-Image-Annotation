import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Print error message if image is null
if img is None:
    print('Could not read image')
else:
    print('Image displaying correctly.')
#We make a copy of the image so changes don't affect the original
imageRectangle = img.copy()
# define the starting and end points of the rectangle
start_point =(300,115)
end_point =(475,225)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8)
# Display Images
cv2.imshow('Original Image',img)
cv2.imshow('Rectangle Image', imageRectangle)
#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()