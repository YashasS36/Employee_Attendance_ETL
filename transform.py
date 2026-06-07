import pandas as pd

print("===== TRANSFORMATION STARTED =====")

# Read files
attendance = pd.read_csv(
    "Processed_Files/Clean_Attendance.csv"
)

employees = pd.read_csv(
    "Source_Files/Employee_Master.csv"
)

# --------------------------------------------------
# Transformation 1: Merge Employee Details
# --------------------------------------------------

attendance = attendance.merge(
    employees,
    on="Employee_ID",
    how="left"
)

print("Employee details merged successfully")

# --------------------------------------------------
# Transformation 2: Convert Time Columns
# --------------------------------------------------

attendance["In_Time"] = pd.to_datetime(
    attendance["In_Time"],
    format="%H:%M"
)

attendance["Out_Time"] = pd.to_datetime(
    attendance["Out_Time"],
    format="%H:%M"
)

# --------------------------------------------------
# Transformation 3: Calculate Working Hours
# --------------------------------------------------

attendance["Working_Hours"] = (
    attendance["Out_Time"] -
    attendance["In_Time"]
).dt.total_seconds() / 3600

attendance["Working_Hours"] = (
    attendance["Working_Hours"]
    .round(2)
)

print("Working hours calculated")

# --------------------------------------------------
# Transformation 4: Identify Late Arrivals
# --------------------------------------------------

office_start = pd.to_datetime(
    "09:30",
    format="%H:%M"
).time()

attendance["Late"] = (
    attendance["In_Time"].dt.time >
    office_start
)

attendance["Late"] = attendance["Late"].map({
    True: "Yes",
    False: "No"
})

print("Late arrivals identified")

# --------------------------------------------------
# Transformation 5: Calculate Overtime
# --------------------------------------------------

attendance["Overtime_Hours"] = (
    attendance["Working_Hours"] - 8
)

attendance["Overtime_Hours"] = (
    attendance["Overtime_Hours"]
    .clip(lower=0)
    .round(2)
)

print("Overtime calculated")

# --------------------------------------------------
# Transformation 6: Attendance Status
# --------------------------------------------------

attendance["Status"] = "Present"

print("Attendance status assigned")

# --------------------------------------------------
# Display Final Output
# --------------------------------------------------

print("\n===== TRANSFORMED DATA =====\n")

print(
    attendance[
        [
            "Employee_ID",
            "Employee_Name",
            "Department",
            "Working_Hours",
            "Late",
            "Overtime_Hours",
            "Status"
        ]
    ]
)

# --------------------------------------------------
# Save Output File
# --------------------------------------------------

attendance.to_csv(
    "Processed_Files/Transformed_Attendance.csv",
    index=False
)

print("\nTransformed file saved successfully")

print("\n===== TRANSFORMATION COMPLETED =====")