from collections import Counter

failed_ips = []
total_records = 0

with open("login_logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")

        if len(parts) != 3:
            continue

        timestamp, ip_address, status = parts
        total_records += 1

        if status == "FAILED":
            failed_ips.append(ip_address)

attempt_counts = Counter(failed_ips)

report = []
report.append("===== SECURITY ANALYSIS REPORT =====")
report.append(f"Total records analyzed: {total_records}")
report.append(f"Total failed attempts: {len(failed_ips)}")
report.append("\n----- IP Address Analysis -----")

alert_count = 0

for ip_address, count in attempt_counts.items():
    report.append(f"\nIP Address: {ip_address}")
    report.append(f"Failed attempts: {count}")

    if count >= 3:
        report.append("ALERT: Repeated failed login attempts!")
        alert_count += 1
    else:
        report.append("Status: No alert")

report.append("\n----- Final Summary -----")
report.append(f"Suspicious IP addresses: {alert_count}")
report.append("Analysis completed.")

# Display the report
for line in report:
    print(line)

# Save the report to a text file
with open("security_report.txt", "w") as file:
    file.write("\n".join(report))

print("\nReport saved to security_report.txt")