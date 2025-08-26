from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

# Step 1: Load the Iris dataset from Hugging Face
iris = load_iris()
x = iris.data  # Features
y = iris.target  # Labels

# Step 2: Split the dataset into training (120 samples) and evaluation (30 samples)
x_train, x_eval, y_train, y_eval = train_test_split(
    x, y, test_size=30/150, random_state=42)

# Step 3: Convert split to DataFrames
train_data = pd.DataFrame(x_train, columns=iris.feature_names)
train_data["target"] = y_train

eval_data = pd.DataFrame(x_eval, columns=iris.feature_names)
eval_data["target"] = y_eval

# Step 4: Save the splits to CSV files
current_path = "./src/test/LLM/Data_Spliting/"
train_file = current_path + "iris_train.csv"
eval_file = current_path + "iris_eval.csv"

train_data.to_csv(train_file, index=False)
eval_data.to_csv(eval_file, index=False)

print(f"Training data saved to '{train_file}'")
print(f"Evaluation data saved to '{eval_file}'")
