import pandas as pd

# Read source files
attendance = pd.read_csv("Source_Files/Attendance.csv")
employees = pd.read_csv("Source_Files/Employee_Master.csv")

print("===== DATA VALIDATION STARTED =====")

# Check missing Employee IDs
attendance = attendance.dropna(subset=["Employee_ID"])

# Check missing In_Time
attendance = attendance.dropna(subset=["In_Time"])

# Check missing Out_Time
attendance = attendance.dropna(subset=["Out_Time"])

# Remove duplicate records
attendance = attendance.drop_duplicates()

# Remove invalid Employee IDs
attendance = attendance[
    attendance["Employee_ID"].isin(employees["Employee_ID"])
]

print("Clean Records =", len(attendance))

# Save cleaned file
attendance.to_csv(
    "Processed_Files/Clean_Attendance.csv",
    index=False
)

print("===== DATA VALIDATION COMPLETED =====")