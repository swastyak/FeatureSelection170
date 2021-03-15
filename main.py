import random
import numpy


def accuracy():
    return random.random()


def feature_search_demo():
    return


def main():
    print("Welcome to Swastyak's Feature Search Algorithm.")
    fileName = input(
        "Type in the name of file to test (1 for small, 2 for large): \n")
    typeAlgorithm = input("Type the number of the algo you want to run: \n")
    defaultSmall = "CS170_SMALLtestdata_13.txt"
    defaultLarge = "CS170_largetestdata_66.txt"
    if fileName == "1":
        fileName = defaultSmall
    if fileName == "2":
        fileName = defaultLarge
    numpy.loadtxt(fileName, delimiter=' ')


main()
