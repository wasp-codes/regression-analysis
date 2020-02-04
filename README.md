# Regression Analysis 
Analysis of tides in Brisbane

## Abbreviations
1. MAE: Mean Absolute Error
2. MSE: Mean Squared Error

## Literature Review
From Tensorflow [1]:
1. Mean Squared Error (MSE) is a common loss function used for regression problems (different loss functions are used for classification problems).
2. Similarly, evaluation metrics used for regression differ from classification. A common regression metric is Mean Absolute Error (MAE).
3. When numeric input data features have values with different ranges, each feature should be scaled independently to the same range.
4. If there is not much training data, one technique is to prefer a small network with few hidden layers to avoid overfitting.
5. Early stopping is a useful technique to prevent overfitting.

Use Pandas to normalize data [4]

## Dataset
Tide and current data for northern hemisphere can be found at [2]
The World Bank provides a Climate Data API [3].
Farmsense moon api [5]
Mateomatics moon API [6]


## Code
For real-time-tide-readings.py, the text response can be character limited using the following, which can possibly be used to print specific things from the api, like the name of the port:

print(response.text[:100])


# Changelog
Changelog guide at [7]

## References
1. Available from: https://www.tensorflow.org/tutorials/keras/regression
2. Available from: https://tidesandcurrents.noaa.gov/astronomical.html
3. Available from: https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api
4. Available from: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#normalization
5. Available from: http://www.farmsense.net/api/
6. Available from https://www.meteomatics.com/en/api/available-parameters/moon/#moon_phase
7. Available from: https://keepachangelog.com/en/1.0.0/
