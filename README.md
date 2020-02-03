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

## Dataset
Tide and current data for northern hemisphere can be found at [2]

## Code
For real-time-tide-readings.py, the text response can be character limited using:
print(response.text[:100])
This can possibly be used to print specific things from the api, like the name of the port.

## References
1. Available from: https://www.tensorflow.org/tutorials/keras/regression
2. Available from: https://tidesandcurrents.noaa.gov/astronomical.html