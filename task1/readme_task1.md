# source file
- source file: dataset1.csv & dataset2.csv
- new files replace old files every day 1am

# processing script
- task1.py is the processing script

# output file
- output file: final_output.csv
- new file replaces old file after each processing

# job scheduling
- airflow file: airflow.py
- just deploy the file in Apache Airflow to schedule the task
- Task is scheduled to run 1:15 am daily
