import pandas as pd
import sklearn.model_selection

def load_data(filename):
    return pd.read_csv(filename)
    
def inspect_data(pd):
    # 1. provide stastistical information of all columns (counts, unique, frequency)
    pd.nunique()
    # print(pd)
    # 2. check for null


# def prep_training():
#     x = data.iloc[:,:6]
#     y = data.iloc[:, 6]

#     print("Shape of x: ", x.shape)
#     print("Shape of y: ", y.shape)

#     # Splitting the dataset into train and test sets (test_size = 0.2)
#     # see model_selection
    
def main():
    car_data = load_data('evaluation.csv')
    inspect_data(car_data)
    # x_train, x_test, y_train, y_test = prep_training(car_data)

main()

# Perform following task for Decision tree

#  1. create a model
#  2. feed training data into the model
#  3. predict values for your test data
#  4. visualize classifier
#  5. find the training and testing accuracy


# NOTE:
#        Use sklearn's DecisionTreeClassifier
#        Visualize your decision trees using any (Scikit-learn, Graphviz, Matplotlib) library

# 1. Decision Trees with max_depth = 2
# 2. Decision Trees with max_depth = 4
# 3. Decision Trees with max_depth = 6
# 4. Decision Trees with max_depth = 8
# 5. Decision Trees with max_depth = 10
# 6. Decision Trees with max_depth = 12