import cv2

#google colab here: shorturl.at/agnU6
# Read Images
img = cv2.imread('sample.jpg')

# Print error message if image is null
if img is None:
    print('Could not read image')
else:
    print('Image displaying correctly.')
#We make a copy of the image so changes don't affect the original
imageText = img.copy()
#define text
text = 'Hello World! I\'m here!'
# define the origin
origin =(50,75)
#Call the putText() function
#Horizontal with Antialiasing
cv2.putText(imageText, text, origin, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color = (255,255,0), thickness=0, lineType=cv2.LINE_AA)
# Display Images
cv2.imshow('Original Image',img)
cv2.imshow('Annotated Image', imageText)
#wait for input and destroy windows
cv2.waitKey(0)
cv2.destroyAllWindows()