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

- Registers with a positive response tend to be older
- Registers with a positive response tend to have a higher annual premium
- There is no clear correlation between age and annual premium.
- Registers with driving license have a higher proportion of responses than registers with no driving license (12.3% vs 5.5%)
- Registers previously insured have a lower proportion of responses than registers previously not insured (0.1% vs 22.8%)
- Registers with an older vehicle have a higher proportion of responses.
- Registers with vehicle damage have a higher proportion of responses than registers with no vehicle damage (24.1% vs 0.4%)
- There is a significant difference in the response proportion among the different region codes. For example for the region code 39 and 44 the proportion of positive response is 0%. On the other hand the Region codes 38 and 28 have a positive response in around 20% of the registers. There are more than 50 differen region codes, a new variable is created identifying the quartiles by proportion of positive responses.
- There is a significant difference in the response proportion among the sales channels. For example for the region code 27 and 67, there are 0% registers with a positive response. On the other hand the Region codes 123 and 43 have respectively 80% and 70% of positive responses. There are more than 150 different sales channels, a new variable is created identifying the sextiles by proportion of positive responses.

### Prediction Models and Competition results:

Submissions are scored on the root mean squared error. I evaluated the RMSE Score with a split of the given data to select the two models that are going to be evaluated by Kaggle.

- **Neural Network version 1 using keras from Tensorflow** - RMSE Score - test:  68,246.43958568497
- **Neural Network, version 2 using keras from Tensorflow** and a grid search procedure to select the best parameters - RMSE Score - test 68,257.12306814594
- **Decision Tree using DecisionTreeRegressor from sklearn** and a grid search procedure to select the best parameters- RMSE Score - test: 80,911.52
- **OLS using statsmodels** used to test statistical significance of the variables - RMSE Score - train test: 69,883.78566228921

### Interpretation

The AUC score for **Neural Network Version 1** is 0.86017. This means that with this model, there is a 86% probability that an individual with a positive response will have a higher predicted score than an individual with a negative response.

The ROC curve displays the performance of a binary classifier across different decision cutoffs by plotting the True Positive Rate (TPR) against the False Positive Rate (FPR).  A higher AUC indicates a better-performing model, as it signifies a higher TPR and a lower FPR across all thresholds.