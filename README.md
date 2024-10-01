# Used Car Prices Regression

This repository contains the notebook for exploring the dataset and the notebook for building regression models for predicting the prices of used cars.The models are used for the Kaggle competition "Playground Series - Season 4, Episode 9".

https://www.kaggle.com/competitions/playground-series-s4e9

## Table of Contents
 - Overview
 - Repository Structure
 - Data Exploration
 - Prediction Models
 - Results

## Overview
The goal of this competition is to predict the price of used cars based on various attributes. The dataset used for this competition is provided by Kaggle. The approach involves data exploration, feature engineering, and building various machine learning models to achieve the best performance measured by Root Mean Squared Error (RMSE).

## Repository Structure

 - `data_exploration.ipynb`: Jupyter notebook for exploring the dataset and performing initial data analysis.
 - `data_transformation.py`: Contains the script for performing the final data transformatio for the train and test data.
 - `prediction_models.ipynb`: Jupyter notebook for building, training, and evaluating machine learning models.
 - `requirements.txt`: Txt file with the requirements if the code execution wants to be replicated

### Data Exploration Summary:

Some of the graphs and insights may seem obvious but it is recommended to see the graphs and visualizations to understand the relation and impact.

- Vehicles with Turbo tend to have a higher price of the car.
- Vehicles with damage tend to have a lower price of the car.
- Vehicles with a clean_title tend to have a lower price of the car.
- The year of the model is positively correlated with the price of the car.
- The milage of the car is negatively correlated with the price of the car.
- The hp is positvely correlated with the price of the car.
- The engine size is positively correlated with the price of the car.
- The cars with 12 cylinders on average have the higher prices and the cars with 5 cylinders on average have the lower prices. 
- The cars with 10 speeds on average have the higher prices and the cars with 4 speeds on average have the lower prices.
- The cars that use electric power on average have the higher prices and the cars taht use Gasolin on average have the lower prices.
- The cars that use an inline or flat engine configuration on average have the higher prices. The cars that use a v type engine configuration on average have the lower prices.
- The cars that use a DCT transmission on average have the higher prices and the cars that use a manual transmission on average have the lower prices.
- Exterior and Interior colors are statistically significant for the price of the cars. The colors were distributed in 5 bins by their relation with the price.


### Prediction Models and Competition results:

Submissions are scored on the root mean squared error. With the given train data, I did a split for training, testing and valudation. The models selected to be submited and evaluated to Kaggle were selected according to their erformance on the RMSE of the data used for testing. Two models were selected to be evaluated by Kaggle.

- **Neural Network version 1 using keras from Tensorflow** - RMSE Score - test:  68,246.43958568497
- **Neural Network, version 2 using keras from Tensorflow** and a grid search procedure to select the best parameters - RMSE Score - test 68,241.3372627156
- **Decision Tree using DecisionTreeRegressor from sklearn** and a grid search procedure to select the best parameters - RMSE Score - test: 80,911.52
- **Random Forest Regressor using RandomForestRegressor from sklearn.ensemble** - RMSE Score - test: 75,097.69
- **OLS using statsmodels** used to test statistical significance of the variables - RMSE Score - train test: 69,883.78566228921
- **Gradient Boosting Regressor using GradientBoostingRegressor from sklearn.ensemble** and a grid search proceder to select the best parameters - RMSE Score - test: 68,178.98

With the selected submissions, the position obtained in the competition was 1491 from 3068 competitors.
