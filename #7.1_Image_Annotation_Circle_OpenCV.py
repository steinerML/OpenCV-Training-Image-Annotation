import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Print error message if image is null
if img is None:
    print('Could not read image')
else:
    print('Image displaying correctly.')
#We make a copy of the image so changes don't affect the original
imageCircle = img.copy()
#Define circle center
circle_center = (420,200)
#Define the radius
radius = 100
#Implement the circle() function
cv2.circle(imageCircle, circle_center, radius, color = (255,255,0) ,thickness=2,lineType=cv2.LINE_AA)
#A thickness value of -1 gives us a solid circle. We use the circle center with an offset.
offset = 50
solid_center = (circle_center[0]+offset,circle_center[1]+offset)
cv2.circle(imageCircle, solid_center, radius, color = (255,255,0) ,thickness=-1,lineType=cv2.LINE_AA)
# Display Images
cv2.imshow('Original Image',img)
cv2.imshow('Circle Image', imageCircle)
#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()