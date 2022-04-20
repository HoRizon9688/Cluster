import pandas as pd
from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    load_robot_execution_failures
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features


def run():
    df = pd.read_csv("渝北.csv")
    df["timestamp"] = pd.to_datetime(df.timestamp)
    print(df)
    print(df.dtypes)
    # extracted_features = extract_features(df, column_id="id", column_sort="timestamp")
    # print(extracted_features)


if __name__ == '__main__':
    run()
