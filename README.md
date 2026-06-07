📊 Employee Attendance ETL Pipeline
📌 Project Overview

This project is an end-to-end ETL pipeline built to process employee attendance data. It extracts raw data, cleans and validates it, transforms it into structured formats, and loads it into fact and report tables for analytics and dashboarding.

The project helps generate meaningful HR insights like attendance rate, working hours, overtime, and department-wise performance.

🏗️ Project Structure
Employee_Attendance_ETL/
│
├── processed_files/
│   ├── clean_attendance.csv
│   ├── transformed_attendance.csv
│
├── reports/
│   ├── Attendance_Report.xlsx
│   ├── Fact_Attendance.xlsx
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── fact_table.py
│   ├── load.py
│
└── README.md
⚙️ ETL Workflow
1. Extract
Load raw attendance data from source files
2. Validate
Check missing Employee IDs
Remove duplicate records
Handle missing time values
3. Transform
Calculate working hours
Compute overtime and late hours
Standardize department-wise data
4. Load
Store cleaned data into Fact Table
Generate Attendance Reports
📊 Key Outputs
Employee Attendance Report
Fact Attendance Table
Department-wise attendance summary
Overtime analysis
Working hours insights
📈 Sample Insights
Which department has highest attendance?
Employees with highest overtime
Average working hours per department
Late arrival patterns
🛠️ Tech Stack
Python 🐍
Pandas
Excel (Reports)
ETL Concepts
🚀 How to Run
# Step 1: Run extraction
python scripts/extract.py

# Step 2: Validate data
python scripts/validate.py

# Step 3: Transform data
python scripts/transform.py

# Step 4: Build fact table
python scripts/fact_table.py

# Step 5: Load reports
python scripts/load.py
📌 Future Improvements
Automate pipeline using Airflow
Connect to SQL database
Build Power BI dashboard
Add real-time data ingestion
👤 Author

Yashas S
