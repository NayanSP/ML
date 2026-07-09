import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
import sklearn
import optuna
import mlflow

def main():
    print("Hello from second-hyperparameter-tuning!")
    mlflow.set_experiment("Hyperparameter Tuning Experiment")
    X,y = fetch_california_housing(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=10, test_size=0.2)

def objective(trail):
    with mlflow.start_run(nested=True, run_name = f"trial_{trail.number}") as child_run:
        rf_max_depth = trail.suggest_int('rf_max_Depth',2,32)
        rf_n_estimators = trail.suggest_int('rf_n_estimators',50, 350, step = 10)
        rf_max_features = trail.suggest_int('rf_max_features',0.1, 10)
        params = {
            "max_depth" : rf_max_depth,
            "n_estimators": rf_n_estimators,
            "max_features" : rf_max_features,
        }
        mlflow.log_params(params)
        reg = sklearn.ensemble.RandomForestRegressor(**params)
        reg.fit(x)


if __name__ == "__main__":
    main()
