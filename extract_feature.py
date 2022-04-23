from tsfresh import extract_features, extract_relevant_features, select_features
from tsfresh.feature_extraction import ComprehensiveFCParameters, feature_calculators, MinimalFCParameters
from tsfresh.utilities.dataframe_functions import impute
import pandas as pd


def run():
    df = pd.read_csv("merge_data.csv")
    print(df)
    extraction_settings = ComprehensiveFCParameters()
    extracted_features = extract_features(df, column_id="id", column_sort="timestamp", column_value='price',
                                          default_fc_parameters=MinimalFCParameters(),
                                          impute_function=impute)
    print(extracted_features)
    extracted_features.to_csv('features.csv')
    # extracted_features = extract_features(df, column_id="id", column_sort="time", column_value='price')
    # impute(extracted_features)
    # features_filtered = select_features(extracted_features, y)

    # features_filtered_direct = extract_relevant_features(df, y,
    #                                                      column_id='id', column_sort='time', column_value='price')
    # print(features_filtered_direct)


if __name__ == '__main__':
    run()
