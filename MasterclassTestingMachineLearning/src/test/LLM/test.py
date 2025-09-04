import os
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
print("Current Path:", CURRENT_PATH)

current_working_directory = os.getcwd().replace("\\", "/")
print(f"Current Working Directory: {current_working_directory}")
CURRENT_PATH = CURRENT_PATH.replace(current_working_directory, ".")
DATASET_PATH = os.path.join(
    CURRENT_PATH, "dataset/gpqa/gpqa_modified.csv").replace("\\", "/")
print("Dataset Path:", DATASET_PATH)
