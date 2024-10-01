# Predicting Used Car Prices - Kaggle Playground Series S4E9

This repository contains the code and notebooks used for my participation in the Kaggle "Playground Series - Season 4, Episode 9" competition. The challenge involves predicting the prices of used cars based on various features such as mileage, engine size, and more. The project showcases data exploration, feature engineering, and the application of machine learning models to achieve accurate price predictions.

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
- `data_exploration.ipynb`: Jupyter notebook for exploring and analyzing the dataset.
- `data_transformation.py`: Python script for final transformations applied to train and test data.
- `prediction_models.ipynb`: Jupyter notebook for building, training, and evaluating machine learning models.
- `requirements.txt`: List of required libraries for reproducing the environment.

### Data Exploration Summary

Key insights from the data exploration phase include the following:
- Vehicles with a turbo engine tend to have higher prices.
- Vehicles with damage have lower prices.
- Vehicles with a clean title tend to have lower prices (surprisingly).
- The model year is positively correlated with the price.
- Mileage is negatively correlated with the price.
- Horsepower and engine size are positively correlated with the price.
- Cars with 12 cylinders generally have the highest prices, while those with 5 cylinders have the lowest.
- Cars with 10-speed transmissions are priced higher, while those with 4-speed transmissions are lower.
- Electric cars have the highest average prices, while gasoline-powered cars are the lowest.
- Inline and flat engine configurations are associated with higher prices, while V-type configurations tend to be cheaper.
- Dual-clutch transmissions (DCT) are linked to higher prices, while manual transmissions tend to be associated with lower prices.
- Both exterior and interior colors are statistically significant factors for car prices. These were binned into 5 categories based on their correlation with price.


### Prediction Models and Competition Results
The models were evaluated based on their Root Mean Squared Error (RMSE) performance on the test set. Two neural networks and a few other machine learning models were trained and evaluated.

#### Final Models Submitted to Kaggle:
- **Neural Network (version 1)** using Keras (TensorFlow) - RMSE on test: 68,246.44
- **Neural Network (version 2)** using Keras with a Grid Search for hyperparameter tuning - RMSE on test: 68,241.34
- **Decision Tree Regressor** using Grid Search for hyperparameters - RMSE on test: 80,911.52
- **Random Forest Regressor** using `RandomForestRegressor` from `sklearn.ensemble` - RMSE on test: 75,097.69
- **Ordinary Least Squares (OLS)** using `statsmodels` for statistical significance testing - RMSE on test: 69,883.79
- **Gradient Boosting Regressor** using `GradientBoostingRegressor` from `sklearn.ensemble` and Grid Search - RMSE on test: 68,178.98

#### Competition Outcome:
Final Kaggle leaderboard position: **1491 out of 3068 participants**.
