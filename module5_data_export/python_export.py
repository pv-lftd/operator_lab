# Fill in the blanks
import pandas as pd  # usually people import pandas as pd. You can import as pandas_library too.

sample_dict = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
    {"id": 3, "name": "Charlie", "role": "Guest"}
]
# Convert list of dictionaries to CSV string
py_result = pd.DataFrame(sample_dict).to_csv(index=False)  # (Dataframe is a pandas datastructure)
print(py_result)
# Save manually into:
# python_output.csv
# Recheck the saved CSV
df = pd.read_csv("python_output.csv")
print(df)
