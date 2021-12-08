import numpy as np


def main():
    train_data = list(np.load("gta_train_data_2.npy", allow_pickle=True))
    
    train_data = np.asarray(train_data)

    print(train_data.shape)

    i = 0

    for image, action in train_data:
        if i > 900:
            print(image)
            print(action)
        i +=1
    
if __name__ == '__main__':
    main()