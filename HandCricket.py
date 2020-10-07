import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import random
import cv2

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
sum = 0

# Load the Image onto the disk using OpenCV
while True:
    vid = cv2.VideoCapture(0)
    ball = random.randint(0, 6)
    while(True):
        keypress = input("Enter C to capture next frame:")
        if(keypress == 'C' or keypress == 'c'):
            ret, frame = vid.read()
            dsize = (224, 224)
            cv2.resize(frame, dsize)
            image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite('User-image-Run.jpg', frame)
            image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            vid.release()
            break
    # Use Pillow to Resize the Image
    image = Image.open('User-image-Run.jpg')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # print(type(normalized_image_array))
    data[0] = normalized_image_array
    prediction = model.predict(data)
    # print(prediction)

    # Deploy the Label of Prediction Array
    five = prediction[0, 0]
    four = prediction[0, 1]
    three = prediction[0, 2]
    two = prediction[0, 3]
    one = prediction[0, 4]
    duck = prediction[0, 5]
    six = prediction[0, 6]

    # find the max of all labels from the Predicted Array
    maxi = max(five, four, three, two, one, duck, six)
    # print(maxi)
    run = 0
    if maxi == five:
        bat = 5
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == four:
        bat = 4
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == three:
        bat = 3
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == two:
        bat = 2
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == one:
        bat = 1
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == duck:
        bat = 0
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    if maxi == six:
        bat = 6
        print("Batsmen = ", bat)
        print("Bowler = ", ball)
        if bat == ball:
            print("You are Out! , Total Runs Scored = ", run)
            break
        run = run + bat
        # print(run)
    print("Total Run Score = ", run)
# Will Add a tkinter file in Future Update
