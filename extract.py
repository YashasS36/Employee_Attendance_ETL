import pandas as pd

attendance = pd.read_csv(r"C:\Users\Yashas S\OneDrive\Desktop\Employee_Attendance_ETL\Source_Files\Attendance.csv")
employees = pd.read_csv(r"C:\Users\Yashas S\OneDrive\Desktop\Employee_Attendance_ETL\Source_Files\Employee_Master.csv")

print("========== ATTENDANCE DATA ==========")
print(attendance)

print("\n========== EMPLOYEE MASTER DATA ==========")
print(employees)

print("\n========== ATTENDANCE INFO ==========")
attendance.info()

print("\n========== EMPLOYEE INFO ==========")
employees.info()