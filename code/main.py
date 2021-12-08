from imp import load_compiled
import numpy as np
from tensorflow.python.keras.backend import dtype
import gta
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tqdm import tqdm
from load_data import load_data




def main():
    epoch = 4
    width = 80
    height = 60
    lr = 0.01
    MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-400K-data.model'.format(lr, 'alexnetv2',epoch)

    train_data = load_data()

    train = train_data[:-100]
    test = train_data[-100:]
    
    X = np.asarray([i[0] for i in train]).reshape(-1,width,height,1)
    Y = [i[1] for i in train]
    Y = np.asarray(Y)


    X = tf.convert_to_tensor(X, dtype=tf.float64)
    Y = tf.convert_to_tensor(Y, dtype=tf.float64)

    test_x = np.asarray([i[0] for i in test]).reshape(-1,width,height,1)
    test_y = [i[1] for i in test]
    test_y = np.asarray(test_y)

    test_x = tf.convert_to_tensor(test_x, dtype= tf.float64)
    test_y = tf.convert_to_tensor(test_y, dtype= tf.float64)


    model = gta.GTA(width, height)
    
    opt = Adam(learning_rate=lr)

    model.compile(loss="categorical_crossentropy", optimizer=opt)
    
    model.fit(X, Y, epochs=epoch, validation_data=(test_x, test_y))

    model.save(MODEL_NAME)

if __name__ == "__main__":
    main()