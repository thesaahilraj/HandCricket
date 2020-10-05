import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import random

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
sum = 0
while True:
    comp = random.randint(0, 6)
    image = Image.open('images/3.jpg')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)

    # Working Part
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    print(prediction)

    five = prediction[0, 0]
    four = prediction[0, 1]
    three = prediction[0, 2]
    two = prediction[0, 3]
    one = prediction[0, 4]
    duck = prediction[0, 5]
    six = prediction[0, 6]

    maxi = max(five, four, three, two, one, duck, six)
    print(maxi)
    if maxi == five:
        ans = 5
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == four:
        ans = 4
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == three:
        ans = 3
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == two:
        ans = 2
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == one:
        ans = 1
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == duck:
        ans = 0
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    if maxi == six:
        ans = 6
        print("Batsmen = ", ans)
        print("Bowler = ", comp)
        if comp == ans:
            break
        sum = sum+ans
        print(sum)
    print("Total Score = ", sum)
