# Python-Based Failed Login Attempt Detection System

## 1. Project Overview
This is a beginner-friendly cybersecurity mini project developed using Python. It analyzes sample login records, counts failed login attempts from each IP address, and identifies IP addresses that exceed a defined failure threshold.

## 2. Objectives
- Analyze login records from a text file.
- Identify failed login attempts.
- Count failed attempts for each IP address.
- Generate an alert when an IP address has 3 or more failed attempts.
- Save the analysis results in a report file.

## 3. Technologies Used
- Python
- Visual Studio Code
- Collections module (Counter)
- Text files for sample logs and reports

## 4. Project Files
- `login_detector.py` - Main Python program.
- `login_logs.txt` - Sample login records.
- `security_report.txt` - Generated security analysis report.
- `README.md` - Project documentation.

## 5. How It Works
1. The program reads login records from `login_logs.txt`.
2. Each record contains a timestamp, IP address, and login status.
3. The program collects records marked `FAILED`.
4. It counts failed attempts for each IP address.
5. It generates an alert when the count reaches 3 or more.
6. It displays and saves the security report.

## 6. How to Run
1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project folder.
4. Run the command:

   `python login_detector.py`

5. Check the terminal output and open `security_report.txt`.

## 7. Sample Data
The project uses fictional login records for testing. For the supplied sample data, the expected summary is:
- Total records analyzed: 9
- Total failed attempts: 7
- Suspicious IP addresses: 1

## 8. Learning Outcomes
- Python file handling
- Conditional statements and loops
- Counting data using Counter
- Basic cybersecurity log analysis
- Generating text reports

## 9. Limitations
This version analyzes sample log files only. It does not monitor live login activity, block IP addresses, or confirm that an actual attack has occurred.

## 10. Future Enhancements
- Validate log entries and IP addresses.
- Add date and time filtering.
- Create a graphical dashboard.
- Support authorized real system logs.
- Add automated monitoring and notifications.

## 11. Disclaimer
This project is intended for educational purposes. Use authorized logs and systems only.