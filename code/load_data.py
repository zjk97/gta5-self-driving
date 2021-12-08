# from typing import final
# from matplotlib.pyplot import axis
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

# from commandlist import left, right

def load_data():
    BALANCE_FACTOR = 5
    num_data = 5
    final_data = []

    for i in range(1, num_data):
        train_data = list(np.load("gta_train_data_{}.npy".format(i), allow_pickle=True))
        df = pd.DataFrame(train_data)
        print(df.head())
        print(Counter(df[1].apply(str)))

        lefts = []
        rights = []
        forwards = []
        backs =[]

        print(len(train_data))
        shuffle(train_data)

        for data in train_data:
            img = data[0]
            choice = data[1]

            if choice == [1,0,0,0]:
                lefts.append([img,choice])
            elif choice == [0,1,0,0]:
                forwards.append([img,choice])
            elif choice == [0,0,1,0]:
                rights.append([img,choice])
            elif choice == [0,0,0,1]:
                backs.append([img,choice])
            else:
                print("no data")


        balanced_length = BALANCE_FACTOR * (len(lefts) + len(rights))

        forwards = forwards[:balanced_length]

        final_data = final_data + forwards + lefts + rights + backs
    print(len(final_data))
    shuffle(final_data)

    return final_data
