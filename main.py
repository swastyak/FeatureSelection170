import random
import pandas as pd
import numpy as np
import csv
import copy
import sys
import math
import time

# data: first val row index, 2nd value col index


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    temp_data = copy.deepcopy(data)
    row, col = data.shape
    number_correctly_classified = 0
    # print("Printing current set." + str(current_set))
    # print("Printing current feature to add." + str(feature_to_add))

    for iter in range(1, col):
        if iter not in current_set and iter != feature_to_add:
            temp_data[:, iter] = 0

    for i in range(0, row):
        object_to_classify = temp_data[i, 1:]
        label_object_to_classify = temp_data[i, 0]
        nearest_neighbor_distance = sys.maxsize
        nearest_neighbor_location = sys.maxsize
        nearest_neighbor_label = 0
        for k in range(0, row):
            if i != k:
                distance = math.sqrt(sum(pow(object_to_classify - temp_data[k, 1:], 2)))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = temp_data[nearest_neighbor_location, 0]
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1
    accuracy = number_correctly_classified / row
    return accuracy


def feature_search_demo(data):
    row, col = data.shape
    currSetFeatures = set()
    bestAccTotal = 0
    global bestSet
    for i in range(0, col-1):
        print("On the " + str(i) + " th level of the search tree")
        global featureToAdd
        featureToAdd = set()
        bestAccuracySoFar = 0
        for k in range(0, col-1):
            if k + 1 not in currSetFeatures:
                print("Consider expanding the " + str(k + 1) + " feature.")
                accuracy = leave_one_out_cross_validation(data, currSetFeatures, k+1)
                if accuracy > bestAccuracySoFar:
                    bestAccuracySoFar = accuracy
                    featureToAdd = k + 1
        currSetFeatures.add(featureToAdd)
        print("On level " + str(i + 1) + " i added feature " + str(featureToAdd) + " to current set")
        print(bestAccuracySoFar)
        # print("This means my current set of features is: " + str(currSetFeatures))
        # print("This is best accuracy so far:" + str(bestAccuracySoFar))
        if bestAccuracySoFar > bestAccTotal:
            bestAccTotal = bestAccuracySoFar
            bestSet = copy.deepcopy(currSetFeatures)

    print("Best set overall: " + str(bestSet))
    print("This set had an accuracy of: " + str(bestAccTotal))
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
    if fileName == "3":
        fileName = "CS170_small_special_testdata__95.txt"
    # data = csv.reader(fileName, delimiter=' ', skipinitialspace=True)

    data = pd.read_csv(fileName, delim_whitespace=True, header=None).values
    print("Timer will be turned on now.")
    start_time = time.time()
    feature_search_demo(data)
    print("Total runtime was " + str(time.time() - start_time) + " seconds.")

    # print(data)


main()


# def leave_one_out_cross_validation(data, current_set, feature_to_add):
#     temp_data = copy.deepcopy(data)
#     row, col = data.shape
#     number_correctly_classified = 0
#     for iter in range(1, col):
#         if iter not in current_set and iter != feature_to_add:
#             temp_data[:, iter] = 0
#
#     for i in range(0, row):
#         object_to_classify = temp_data[i, 1:]
#         label_object_to_classify = temp_data[i, 0]
#         nearest_neighbor_distance = sys.maxsize
#         nearest_neighbor_location = sys.maxsize
#
#         for k in range(0, row):
#             if i != k:
#                 # print("Ask if " + str(i) + " is nearest neighbor with " + str(k))
#                 distance = math.sqrt(sum(pow(object_to_classify - temp_data[k, 1:], 2)))
#                 if distance < nearest_neighbor_distance:
#                     nearest_neighbor_distance = distance
#                     nearest_neighbor_location = k
#                     nearst_neighbor_label = temp_data[nearest_neighbor_location, 0]
#                 # print(distance)
#         if label_object_to_classify == temp_data[nearest_neighbor_location, 0]:
#             number_correctly_classified += 1
#         # print("Object " + str(i) + " is class" + str(label_object_to_classify))
#         # print("It's nearest neighbor is " + str(nearest_neighbor_location) +
#         #      " which is in class " + str(temp_data[nearest_neighbor_location, 0]))
#
#         # print(object_to_classify)
#         # print("Looping over i, at the " + str(i) + " location.")
#         # print("The " + str(i) + "th object is in class " + str(label_object_to_classify))
#     accuracy = number_correctly_classified / row
#     return accuracy
