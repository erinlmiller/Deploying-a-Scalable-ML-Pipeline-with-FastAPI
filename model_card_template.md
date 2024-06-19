# Model Card
The task was to develop a model using public data from the US Census Bureau and deploy the model using FastAPI.

## Model Details
The model uses RandomForestClassifier from sklearn.ensemble. 
Developed by Erin Miller, 06/18/2024. 

## Intended Use
The model is intended to be used to predict whether a person makes greater than $50K or less than $50K per year based on data from the US Census Bureau.

## Training Data
The training data from the 1994 US Census was provided by UC Irvine Machine Learning Repository: https://archive.ics.uci.edu/dataset/20/census+income. The dataset contains 32,561 records and 15 columns. 

## Evaluation Data
The evaluation dataset is comprised of 20% of the data used for training. 

## Metrics
Precision: 0.7427; Recall: 0.6467; F1: 0.6914

## Ethical Considerations
The dataset contains sensitive information such as race, sex, income, education, and workclass, but it is anonymized. The dataset is intended to be used for educational purposes only.

## Caveats and Recommendations
The dataset is from the 1994 US Census. The model should be used on more recent data, and given the state of inflation in the US, a different income cutoff should be explored. $50K in 2024 is very different from $50K in 1994.