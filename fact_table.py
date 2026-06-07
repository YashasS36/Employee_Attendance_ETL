import pandas as pd

print("===== FACT TABLE CREATION STARTED =====")

attendance = pd.read_csv(
    "Processed_Files/Transformed_Attendance.csv"
)

fact_table = attendance[
    [
        "Date",
        "Employee_Name",
        "Department",
        "Working_Hours",
        "Late",
        "Overtime_Hours",
        "Status"
    ]
]

fact_table.columns = [
    "Date",
    "Employee",
    "Department",
    "Work_Hours",
    "Late",
    "Overtime",
    "Status"
]

print("\n===== FACT TABLE =====\n")
print(fact_table)

fact_table.to_csv(
    "Reports/Fact_Attendance.csv",
    index=False
)

print("\nFact table saved successfully")
print("\n===== FACT TABLE CREATION COMPLETED =====")