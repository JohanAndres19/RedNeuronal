import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: Anguis")
  elif answer == 1:
    print("pred: Anolis")
  elif answer == 2:
    print("pred: Chlamidosaurus")
  elif answer == 3:
    print("pred: Draco")
  elif answer == 4:
    print("pred: Lacerta")
  elif answer == 5:
    print("pred: Phrynosoma")
  elif answer == 6:
    print("pred: Sphenodon")

  return answer

