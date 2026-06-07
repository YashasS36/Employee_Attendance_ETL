import pandas as pd

print("===== LOAD PROCESS STARTED =====")

# Read Fact Table
fact_table = pd.read_csv(
    "Reports/Fact_Attendance.csv"
)

print("\n===== DATA TO BE LOADED =====\n")

print(fact_table)

# Load into Excel
fact_table.to_excel(
    "Reports/Attendance_Report.xlsx",
    index=False
)

print("\nAttendance report created successfully")

print("\n===== LOAD PROCESS COMPLETED =====")