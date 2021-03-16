import random
import pandas as pd
import numpy as np
import csv
import copy
import sys

# data: first val row index, 2nd value col index


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    train_data = copy.deepcopy(data)
    row, col = data.shape
    for i in range(0, row):
        object_to_classify = train_data[i, 1:]
        label_object_to_classify = train_data[i, 0]
        nearest_neighbor_distance = sys.maxsize
        nearest_neighbor_location = sys.maxsize
        for k in range(0, row):
            if i != k:
                print("Ask if " + str(i) + " is nearest neighbor with " + str(k))
        # print(object_to_classify)
        # print("Looping over i, at the " + str(i) + " location.")
        # print("The " + str(i) + "th object is in class " + str(label_object_to_classify))
    return random.random()


def feature_search_demo(data):
    row, col = data.shape
    currSetFeatures = set()
    # print(type(currSetFeatures))
    # for i in range(1, row):
    for i in range(1, col):
        print("On the " + str(i) + " th level of the search tree")
        global featureToAdd
        featureToAdd = set()
        bestAccuracySoFar = 0
        for k in range(1, col):
            if k not in currSetFeatures:
                print("Consider expanding the " + str(k) + " feature.")
                accuracy = leave_one_out_cross_validation(data, currSetFeatures, k+1)
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
    # data = csv.reader(fileName, delimiter=' ', skipinitialspace=True)

    data = pd.read_csv(fileName, delim_whitespace=True, header=None).values

    feature_search_demo(data)
    print(type(data))
    # print(data)


main()
