# OpenCV Image Annotation.
Image annotation using OpenCV.
## Contents :
I have used the following functions/methods:

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.imread()     |We read the image                                                             |
|cv2.line()       |We draw a line                                                                |
|cv2.circle()     |We draw a circle                                                              |
|cv2.rectangle()  |We draw a rectangle                                                           |
|cv2.ellipse()    |We draw an ellipse                                                            |
|cv2.putText()    |We write some text                                                            |

## Test Image used: 
I have used sample.jpg that can be found in the repository.

![Source Image Sequence](sample.jpg)
![Source Image Sequence](https://learnopencv.com/wp-content/uploads/2021/06/Lined-Img.jpg)
![Source Image Sequence](https://learnopencv.com/wp-content/uploads/2021/06/ImageCircle.jpg) 
![Source Image Sequence](https://learnopencv.com/wp-content/uploads/2021/06/FilledCircle.jpg) 
![Source Image Sequence](https://learnopencv.com/wp-content/uploads/2021/06/ImageRectangle.jpg)
## Summary:

```python
#We draw a line
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
```
```python
#Implement the circle() function
cv2.circle(imageCircle, circle_center, radius, color = (255,255,0) ,thickness=2,lineType=cv2.LINE_AA)
```
```python
# Draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8)
```
```python
#Ellipse Horizontal with Antialiasing
cv2.ellipse(imageEllipse, center, axis1, 0, 0, 360, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
```
```python
#Insert Text Horizontal with Antialiasing
cv2.putText(imageText, text, origin, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color = (255,255,0), thickness=0, lineType=cv2.LINE_AA)
```
