from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, classification_report,
                             confusion_matrix)


def train_and_evaluate_model(model, x_train, y_train, x_test, y_test, model_name):
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    print(f"{model_name} Confusion Matrix:")
    print(conf_matrix)
    print(f"{model_name} Classification Report:")
    print(class_report)
    
def train_and_evaluate_with_grid_search(model, param_grid, x_train, y_train, x_test, y_test, model_name):
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(x_train, y_train)
    
    print(f"Best parameters for {model_name}: {grid_search.best_params_}")
    
    # Make predictions using the best model
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(x_test)
    
    # Evaluate the model
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    
    print(f"{model_name} Confusion Matrix:")
    print(conf_matrix)
    print(f"{model_name} Classification Report:")
    print(class_report)
    
    
def train_and_evaluate_with_random_search(model, param_dist, x_train, y_train, x_test, y_test, model_name):
    random_search = RandomizedSearchCV(model, param_dist, n_iter=100, cv=5, scoring='accuracy', random_state=999, n_jobs=-1)
    random_search.fit(x_train, y_train)
    
    print(f"Best parameters for {model_name}: {random_search.best_params_}")
    
    # Make predictions using the best model
    best_model = random_search.best_estimator_
    y_pred = best_model.predict(x_test)
    y_prob = best_model.predict_proba(x_test)[:, 1]  # Probabilities for ROC-AUC

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print(f"{model_name} Evaluation Metrics:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    print(f"{model_name} Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print(f"{model_name} Classification Report:")
    print(classification_report(y_test, y_pred))