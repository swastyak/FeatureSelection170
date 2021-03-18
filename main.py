import pandas as pd
import numpy as np
import copy
import sys
import math
import time


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    # Make a deep copy since python does shallow copies, but we want to change data
    # Assign 0s to features not in use, we only want to look at the current features
    # and the feature we want to add
    temp_data = copy.deepcopy(data)
    row, col = data.shape
    number_correctly_classified = 0

    for iter in range(1, col):
        if iter not in current_set and iter != feature_to_add:
            temp_data[:, iter] = 0
    # Initialize nearest neighbor to int max, and go down from there
    # Double loops will go into finding nearest neighbor for validaton
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
    # Overall accuracy
    accuracy = number_correctly_classified / row
    return accuracy


def feature_search_demo(data):
    # Forward search function, iterates throguh all elements in the columns (features)
    # Inner loop lets us see which part has most accurate feature to expand
    # Then, add that feature to the current set of features
    row, col = data.shape
    currSetFeatures = set()
    print("Using feature(s) " + str(currSetFeatures) +
          " accuracy is " + str(leave_one_out_cross_validation(data, currSetFeatures, 0)))
    bestAccTotal = 0
    global bestSet
    for i in range(0, col-1):
        print("On the " + str(i + 1) + " th level of the search tree")
        global featureToAdd
        featureToAdd = set()
        bestAccuracySoFar = 0
        for k in range(0, col-1):
            if k + 1 not in currSetFeatures:
                # print("Consider expanding the " + str(k + 1) + " feature.")
                accuracy = leave_one_out_cross_validation(data, currSetFeatures, k+1)
                if accuracy > bestAccuracySoFar:
                    bestAccuracySoFar = accuracy
                    featureToAdd = k + 1
        currSetFeatures.add(featureToAdd)
        # print("On level " + str(i + 1) + " i added feature " + str(featureToAdd) + " to current set")
        # print("Current set of features is: " + str(currSetFeatures))
        # print(bestAccuracySoFar)
        print("Using feature(s) " + str(currSetFeatures) +
              " accuracy is " + str(bestAccuracySoFar))
        if bestAccuracySoFar > bestAccTotal:
            bestAccTotal = bestAccuracySoFar
            bestSet = copy.deepcopy(currSetFeatures)

    print("Best set overall: " + str(bestSet))
    print("This set had an accuracy of: " + str(bestAccTotal))
    return


def feature_backwards_demo(data):
    # Same thought process as forward iterations, but you start with a full set
    row, col = data.shape
    currSetFeatures = set()
    for iter in range(1, col):
        currSetFeatures.add(iter)
    print("Using feature(s) " + str(currSetFeatures) +
          " accuracy is " + str(leave_one_out_cross_validation(data, currSetFeatures, 0)))
    bestAccTotal = 0
    global cBestSet
    for i in range(0, col):
        print("On the " + str(col - i-1) + " th level of the search tree")
        global cFeatureToRemove
        cFeatureToRemove = set()
        bestAccuracySoFar = 0
        for k in range(0, col):
            if k in currSetFeatures:
                # print("Consider removing the " + str(k) + " feature.")
                temp_curr = copy.deepcopy(currSetFeatures)
                temp_curr.remove(k)
                accuracy = leave_one_out_cross_validation(data, temp_curr, 0)
                if accuracy > bestAccuracySoFar:
                    bestAccuracySoFar = accuracy
                    cFeatureToRemove = k
        if len(currSetFeatures) != 0:
            currSetFeatures.remove(cFeatureToRemove)
            # print("On level " + str(col - i-1) + " i removed feature " +
            #       str(cFeatureToRemove) + " from current set")
            # print("Current set of features is: " + str(currSetFeatures))
            # print(bestAccuracySoFar)
            print("Using feature(s) " + str(currSetFeatures) +
                  " accuracy is " + str(bestAccuracySoFar))
        else:
            print("Nothing removed anymore")
        # print(bestAccuracySoFar)
        if bestAccuracySoFar > bestAccTotal:
            bestAccTotal = bestAccuracySoFar
            cBestSet = copy.deepcopy(currSetFeatures)
    print("Best set overall: " + str(cBestSet))
    print("This set had an accuracy of: " + str(bestAccTotal))
    return


def main():
    print("Welcome to Swastyak's Feature Search Algorithm.")
    fileName = input(
        "Type in the name of file to test (1 for small, 2 for large, 3 for special small): \n")
    typeAlgorithm = input("Type the number of the algo you want to run (1 forward, 2 backward): \n")
    if fileName == "1":
        fileName = "CS170_SMALLtestdata__13.txt"
    if fileName == "2":
        fileName = "CS170_largetestdata__66.txt"
    if fileName == "3":
        fileName = "CS170_small_special_testdata__95.txt"
    print("Going to read " + fileName)
    data = pd.read_csv(fileName, delim_whitespace=True, header=None).values
    print("Timer will be turned on now.")
    start_time = time.time()
    if typeAlgorithm == "1":
        feature_search_demo(data)
    else:
        feature_backwards_demo(data)
    print("Total runtime was " + str(time.time() - start_time) + " seconds.")


main()
