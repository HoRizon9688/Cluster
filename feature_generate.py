import pandas as pd
from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    load_robot_execution_failures
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features

series = {'price': [9109, 9746, 8636, 9040, 9758, 10476, 10975, 11545, 11405, 11243, 11086, 10786,
                    10549, 10475, 10532, 10510, 10601, 10639, 10780, 10886, 10889, 10842, 10739, 10615,
                    10706, 10678, 10751, 10527, 10508, 10542, 10675, 10712, 10751, 10778, 10800, 10775,
                    10791, 10870, 10963, 11111, 11364, 11640, 11755, 11939, 12018, 11903, 11902, 11839]}

df = pd.DataFrame(data=series)
print(df)
# features = extract_features(df, column_id="price")
# print(features)

# impute(extracted_features)
#
# print(features_filtered_direct)

