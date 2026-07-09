import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import mlflow

def main():
    print("Hello from first!")
    X,y = datasets.make_classification(n_samples=10000, n_features=10, n_informative=2, n_redundant=8,
                                       weights=[0.9,0.1], flip_y=0, random_state=20)
    print(X)
    print(np.unique(y, return_counts = True))

    x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=20)

    params = {
        'solver' : 'lbfgs',
        'max_iter' : 1000,
        'random_state' : 8888,
    }

    log = LogisticRegression(**params)
    log.fit(x_train, y_train)

    predict = log.predict(x_test)

    report = classification_report(y_test, predict)
    print(report)
    report_dict = classification_report(y_test, predict, output_dict=True)
    print(report_dict)

    mlflow.set_experiment('First experiment')
    mlflow.set_tracking_uri("http://127.0.0.1:5000/")

    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metrics({
            'accuracy' : report_dict['accuracy'],
            'recall_class_0' : report_dict['0']['recall'],
            'recall_class_1' : report_dict['1']['recall'],
            'macro_Avg' : report_dict['macro avg']['f1-score']
        })
        mlflow.sklearn.log_model(log,'Logistic Regression')  
if __name__ == "__main__":
    main()
