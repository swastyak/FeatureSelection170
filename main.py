import random
import pandas as pd
import numpy as np
# df: first val row index, 2nd value col index


def leave_one_out_cross_validation(df, current_set, feature_to_add):
    return random.random()


def feature_search_demo(df):
    row, col = df.shape
    currSetFeatures = set()
    # print(type(currSetFeatures))
    for i in range(1, row):
        print("On the " + str(i) + " th level of the search tree")
        global featureToAdd
        featureToAdd = set()
        bestAccuracySoFar = 0
        for k in range(1, col):
            if k not in currSetFeatures:
                print("Consider expanding the " + str(k) + " feature.")
                accuracy = leave_one_out_cross_validation(df, currSetFeatures, k+1)
                if accuracy > bestAccuracySoFar:
                    bestAccuracySoFar = accuracy
                    featureToAdd = k
        # currSetFeatures[i] = featureToAdd
        currSetFeatures.add(featureToAdd)
        print("On level " + str(i) + " i added feature " + str(featureToAdd) + " to current set")
    return


def main():
    print("Welcome to Swastyak's Feature Search Algorithm.")
    fileName = input(
        "Type in the name of file to test (1 for small, 2 for large): \n")
    typeAlgorithm = input("Type the number of the algo you want to run: \n")
    defaultSmall = "CS170_SMALLtestdata__13.txt"
    defaultLarge = "CS170_largetestdata__66.txt"
    if fileName == "1":
        fileName = defaultSmall
    if fileName == "2":
        fileName = defaultLarge
    df = pd.read_csv(fileName, delim_whitespace=True, header=None)
    feature_search_demo(df)


main()
