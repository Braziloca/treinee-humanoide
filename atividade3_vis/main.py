import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import preprocessing
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from sklearn.metrics import confusion_matrix
from conf_matrix import plot_confusion_matrix
import matplotlib.pyplot as plt
import os
import numpy as  np
import shutil
import random

physical_devices = tf.config.experimental.list_physical_devices("GPU")
print("Num GPUs Available: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)


#organizar os arquivos nas pastas de train, test e valid
os.chdir("soccer-balls-dataset/")
if os.path.isdir("valid") is False:
    os.mkdir("valid")
    os.mkdir("valid/ball")
    os.mkdir("valid/no-ball")
    os.mkdir("test")
    os.mkdir("test/ball")
    os.mkdir("test/no-ball")

    valid_samples_ball = random.sample(os.listdir(f'train/ball'),40)
    for i in valid_samples_ball:
        shutil.move(f'train/ball/{i}', f'valid/ball')
    
    valid_samples_noball = random.sample(os.listdir(f'train/no-ball'),20)
    for j in valid_samples_noball:
        shutil.move(f'train/no-ball/{j}', f'valid/no-ball')

    test_samples_ball = random.sample(os.listdir(f'train/ball'),40)
    for k in test_samples_ball:
        shutil.move(f'train/ball/{k}', f'test/ball')

    test_samples_noball = random.sample(os.listdir(f'train/no-ball'),20)
    for l in test_samples_noball:
        shutil.move(f'train/no-ball/{l}', f'test/no-ball')

os.chdir("../..")

train_path = "atividade3_vis/soccer-balls-dataset/train"
valid_path = "atividade3_vis/soccer-balls-dataset/valid"
test_path = "atividade3_vis/soccer-balls-dataset/test"

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(directory=train_path, target_size=(224,224), classes=["ball", "no-ball"], batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(directory=valid_path, target_size=(224,224), classes=["ball", "no-ball"], batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(directory=test_path, target_size=(224,224), classes=["ball", "no-ball"], batch_size=10, shuffle=False)

mobile = tf.keras.applications.mobilenet.MobileNet() #import de um modelo de rede neural ja estruturada e pré treinada (MobileNet)

#edits na rede neural importada  
x = mobile.layers[-2].output
output = Dense(units=2, activation="softmax")(x)

model = Model(inputs=mobile.input, outputs=output)                  

for layer in model.layers[:-23]:
    layer.trainable = False


#treinando o novo modelo
model.compile(optimizer=Adam(lr=0.0001), loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x=train_batches, validation_data=valid_batches, epochs=30, verbose=2)


#plot dos dados de teste em uma matriz (Confusion Matrix)
test_labels = test_batches.classes
predictions = model.predict(x=test_batches, verbose=0)
cm = confusion_matrix(y_true=test_labels, y_pred=np.argmax(predictions, axis=-1))
'''print(test_batches.class_indices)'''
cm_plot_labels = ["ball", "no-ball"]
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title = "Confusion Matrix")
plt.show()