"""
Stephanie Xie
09/25/2017
CSC 350

Collaborators: Emma Stephenson, Zainab Aqdas, Eleanor Ewing
References: StackOverflow
"""
import numpy as np
import pandas as pd


def get_data_from_csv(csv):
    df = pd.read_csv(csv)
    return df


def fill_with_mean(df):
    df_copy = df.copy()
    return df_copy.fillna(df_copy.mean())


def fill_with_zero(df):
    df_copy = df.copy()
    return df_copy.fillna(0)


def diff_df(df1, df1_name, df2, df2_name):
    df1_copy = df1.copy()
    df2_copy = df2.copy()

    if df1_copy.equals(df2_copy):
        return None
    else:
        ne_stacked = (df1_copy != df2_copy).stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'field']
        diff_locations = np.where(df1_copy != df2_copy)
        d1_diff = df1_copy.values[diff_locations]
        d2_diff = df2_copy.values[diff_locations]
        return pd.DataFrame({"{}".format(df1_name): d1_diff, "{}".format(df2_name): d2_diff},
                            index=changed.index)


def main():
    complete_df = get_data_from_csv("Wholesale customers data.csv")
    missing_df = get_data_from_csv("Wholesale customers data-missing.csv")
    means_df = fill_with_mean(missing_df)
    zeros_df = fill_with_zero(missing_df)

    complete_missing_diff = diff_df(complete_df, "complete", missing_df, "missing")
    complete_means_diff = diff_df(complete_df, "complete", means_df, "means")
    complete_zeros_diff = diff_df(complete_df, "complete", zeros_df, "zeros")

    print(complete_missing_diff)
    print("\n-------------\n")
    print(complete_means_diff)
    print("\n-------------\n")
    print(complete_zeros_diff)


if __name__ == '__main__':
    main()
