# Repo: https://github.com/pv-lftd/operator_lab/tree/main/module5_data_export
# Fill in the blanks
import pandas as pd  # usually people import pandas as pd. You can import as pandas_library too.

sample_dict = [
    {"id": 101, "name": "Alice Johnson", "role": "Lead Engineer", "skills": ["Python", "AWS", "Docker"], "is_active": True},
    {"id": 102, "name": "Marcus Chen", "role": "UX Designer", "skills": ["Figma", "CSS", "React"], "is_active": True},
    {"id": 103, "name": "Sarah Smith", "role": "Data Analyst", "skills": ["SQL", "Tableau", "R"], "is_active": False}
]
# Convert list of dictionaries to CSV string
py_result = pd.DataFrame(sample_dict).to_csv(index=False)  # (Dataframe is a pandas datastructure)
print(py_result)
# Save manually into:
# python_output.csv
# Recheck the saved CSV
df = pd.read_csv("python_output.csv")
print(df)
