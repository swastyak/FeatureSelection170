import random
import pandas as pd


def accuracy():
    return random.random()


def feature_search_demo(df):
    i, k = df.shape
    i -= 1
    k -= 1
    print(i)
    print(k)
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
