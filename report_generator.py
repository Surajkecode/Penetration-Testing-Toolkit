import os
from datetime import datetime

def generate_report(test_type, target, result):
    # Get current timestamp and sanitize it for filenames
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Replace invalid characters for Windows file systems
    sanitized_date = date.replace(":", "-").replace("/", "-").replace(" ", "_")

    # Create the report filename
    report_filename = f"{test_type}_report_{target}_{sanitized_date}.html"
    
    # Ensure the 'reports' directory exists
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Create and write the report to the file
    with open(f"reports/{report_filename}", "w") as report_file:
        report_file.write(f"<html><body><h1>{test_type} Report</h1>")
        report_file.write(f"<p>Test executed on: {date}</p>")
        report_file.write(f"<p>Target: {target}</p>")
        report_file.write(f"<pre>{result}</pre>")
        report_file.write("</body></html>")

    print(f"Report saved as {report_filename}")

# Example Usage:
generate_report("Port Scan", "192.168.1.1", "Open ports: 22, 80, 443")
