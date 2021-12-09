# from typing import final
# from matplotlib.pyplot import axis
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

# from commandlist import left, right

def load_data():
    BALANCE_FACTOR = 3
    num_data = 5
    final_data = []

    limit = 10000

    for i in range(2, 3):
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
                for i in range(10):
                    lefts.append([img,choice])
            elif choice == [0,1,0,0]:
                forwards.append([img,choice])
            elif choice == [0,0,1,0]:
                for i in range(20):
                    rights.append([img,choice])
            elif choice == [0,0,0,1]:
                backs.append([img,choice])
            else:
                print("no data")

        print("before duping:")
        print(len(lefts))
        print(len(rights))
        print("duping...")
        while len(lefts) > 0 and len(lefts) < limit:
            lefts = lefts + lefts
            # print("new left" + str(len(lefts)))
        while len(rights) > 0 and len(rights) < limit:
            rights = rights + rights
            # print("new right" + str(len(rights)))
        shuffle(lefts)
        shuffle(rights)
        if len(lefts) >= limit:
            lefts = lefts[:limit]
        if len(rights) >= limit:
            rights = rights[:limit]
        print("after duping:")
        print(len(lefts))
        print(len(rights))

        while len(forwards) < limit:
            forwards = forwards + forwards
        forwards = forwards[:limit]

        # balanced_length = BALANCE_FACTOR * (len(lefts) + len(rights))

        # forwards = forwards[:balanced_length]
        print(len(forwards))

        final_data = final_data + forwards + lefts + rights + backs
    print(len(final_data))
    shuffle(final_data)

    return final_data
