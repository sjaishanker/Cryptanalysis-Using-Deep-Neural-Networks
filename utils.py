import random
from keras.models import load_model
import numpy as np


def makePrediction(tokens):
    """Takes in the tokens generated and returns the output string"""
    output = ""
    model = load_model('model.h5')
    for x in tokens:
        temp = []
        for i in range(64):
            if x[i] == '1':
                temp.append(1)
            else:
                temp.append(0)
        array = np.array([temp])
        prediction = model.predict(array)
        for i in range(8):
            temp = prediction[0][128 * i:(128 * i) + 128].tolist()
            index = np.argmax(temp)
            if index%128 < 31:
                index = random.randint(48,122)
                output += chr(index+1)
            else:
                output += chr((index%128) + 1)

    return output