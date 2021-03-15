import random
import pandas as pd
import numpy as np
# df: first val row index, 2nd value col index


def accuracy():
    return random.random()


def feature_search_demo(df):
    row, col = df.shape
    for i in range(1, row):
        print("On the " + str(i) + " th level of the search tree")
        for k in range(1, col):
            print("Consider expanding the " + str(k) + " feature.")
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
