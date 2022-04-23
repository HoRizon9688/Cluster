import pandas as pd
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.feature_extraction import extract_features, MinimalFCParameters
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics


def run():
    df = pd.read_csv("merge_data.csv")
    print(df)
    extracted_features = extract_features(df, column_id="id", column_sort="timestamp", default_fc_parameters=MinimalFCParameters())
    print(extracted_features)
    return extracted_features


if __name__ == '__main__':
    features = run()
    # km_cluster = KMeans(n_clusters=5)
    # y_pred = km_cluster.fit_predict(features)
    # print('聚类结果:\n', y_pred)
    # print(metrics.calinski_harabasz_score(features, y_pred))
