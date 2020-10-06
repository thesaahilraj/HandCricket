import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open('User-image-Run.jpg')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

# turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
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
    print(" 5 Runs ")

if maxi == four:
    print(" 4 Runs ")

if maxi == three:
    print(" 3 Runs ")

if maxi == two:
    print(" 2 Runs ")

if maxi == one:
    print(" 1 Runs ")

if maxi == duck:
    print(" 0 Runs - Duck ")

if maxi == six:
    print(" 6 Runs ")
