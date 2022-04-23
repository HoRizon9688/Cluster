from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    load_robot_execution_failures
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh import extract_features, extract_relevant_features, select_features
from tsfresh.feature_extraction import ComprehensiveFCParameters
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features
import pandas as pd


def run():
    df = pd.read_csv("merge_data.csv")
    print(df)
    extraction_settings = ComprehensiveFCParameters()
    extracted_features = extract_features(df, column_id="id", column_sort="timestamp",
                                          default_fc_parameters=extraction_settings,
                                          impute_function=impute)
    print(extracted_features)

    # extracted_features = extract_features(timeseries, column_id="id", column_sort="time")
    # impute(extracted_features)
    # features_filtered = select_features(extracted_features, y)
    # features_filtered_direct = extract_relevant_features(timeseries, y,
    #                                                      column_id='id', column_sort='time')
    # print(features_filtered_direct)


if __name__ == '__main__':
    run()
