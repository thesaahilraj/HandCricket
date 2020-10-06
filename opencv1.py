import cv2

vid = cv2.VideoCapture(0)

while(True):
    keypress = input("Enter C to capture next frame:")
    if(keypress == 'C' or keypress == 'c'):
        ret, frame = vid.read()
        dsize = (224, 224)
        cv2.resize(frame, dsize)
        image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite('User-image-Run.jpg', frame)
        vid.release()
        break
