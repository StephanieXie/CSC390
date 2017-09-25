"""
Stephanie Xie
09/25/2017
CSC 350

Collaborators: Emma Stephenson, Zainab Aqdas, Eleanor Ewing

"""
import matplotlib.pyplot as plt
import pandas as pd


def get_data_from_csv(csv):
    raw_data = pd.read_csv(csv)
    return raw_data


def fill_with_mean(raw_data):
    data = raw_data.copy()
    return data.fillna(data.mean())


def fill_with_zero(raw_data):
    data = raw_data.copy()
    return data.fillna(0)


def main():
    complete_data = get_data_from_csv("Wholesale customers data.csv")
    missing_data = get_data_from_csv("Wholesale customers data-missing.csv")
    mean = fill_with_mean(missing_data)
    zero = fill_with_zero(missing_data)

    # Comparing only two fields for easier visualization
    plt.figure()
    plt.xlabel('Fresh')
    plt.ylabel('Frozen')
    plt.scatter(complete_data['Fresh'], complete_data['Frozen'], color='Red')
    plt.scatter(mean['Fresh'], mean['Frozen'], color='Green')
    plt.scatter(zero['Fresh'], zero['Frozen'], color='Yellow')
    plt.show()


if __name__ == '__main__':
    main()
