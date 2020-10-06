import cv2
vid = cv2.VideoCapture(0)
ret, frame = vid.read()
cv2.imshow('frame', frame)
if cv2.waitKey(33) == ord('a'):
    cv2.imwrite('image/imgae.jpg', frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
