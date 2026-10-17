# Mini Project Report

## Project Title
Python-Based Failed Login Attempt Detection System

## Introduction
Failed login attempts can be useful indicators for identifying potentially suspicious login activity. This project demonstrates how Python can analyze sample login records and highlight repeated failures.

## Problem Statement
Manually reviewing login records can make repeated failed attempts difficult to identify. A simple automated program can count failures by IP address and flag activity that meets a predefined threshold.

## Objectives
1. Read login records from a text file.
2. Count failed attempts by IP address.
3. Display alerts for IP addresses with three or more failures.
4. Save the analysis results to a report file.

## Methodology
The program reads each line from the input file and separates the timestamp, IP address, and status. It collects failed attempts and uses Python's Counter class to calculate the number of failures associated with each IP address. An alert is generated when the count is at least three.

## Software Requirements
- Windows operating system
- Python 3
- Visual Studio Code

## Input
A text file containing timestamps, IP addresses, and login statuses.

## Output
A security analysis report showing the number of records analyzed, total failed attempts, per-IP failure counts, and suspicious-IP count.

## Testing
The program was tested with nine fictional login records. The expected result is nine records analyzed, seven failed attempts, and one IP address meeting the alert threshold.

## Limitations
The program analyzes sample data and does not independently verify real attacks or monitor live login events.

## Conclusion
This project demonstrates basic Python programming, file handling, data counting, conditional logic, and introductory security log analysis.

## Future Scope
Future improvements could include input validation, date-based analysis, a graphical interface, and authorized real-log integration.