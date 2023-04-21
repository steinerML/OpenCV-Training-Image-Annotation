import cv2

# Read Images
img = cv2.imread('sample.jpg')

# Print error message if image is null
if img is None:
    print('Could not read image')
else:
    print('Image displaying correctly.')
#We make a copy of the image so changes don't affect the original
imageEllipse = img.copy()
#define the center of the ellipse
center = (400, 200)
# define the major and minor axies of the ellipse
axis1 =(150,75)
# draw the ellipses
#Horizontal with Antialiasing
cv2.ellipse(imageEllipse, center, axis1, 0, 180, 360, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
#Vertical w/o AA
cv2.ellipse(imageEllipse, center, axis1, 0, 0, 180, (0, 0, 255), thickness=-1)
# Display Images
cv2.imshow('Original Image',img)
cv2.imshow('Half-Ellipse Image', imageEllipse)
#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()