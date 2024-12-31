# Task 3: Penetration-Testing-Toolkit

## Developer Information:
- **Developer**: Suraj Borkute
- **Company**: Codtech IT Solutions
- **Employee ID**: CT08DSM
- **Domain**: Cyber Security & Ethical Hacking
- **Project Duration**: December 2024 to January 2025
- **Mentor**: Neela Santosh Kumar

---

## Overview:
The **Penetration Testing Toolkit** is a robust, Python-based suite designed to streamline and enhance the process of penetration testing. This toolkit is modular, consisting of multiple tools that are essential for assessing the security posture of web applications and network infrastructure. It includes functionalities for network scanning, login brute-forcing, HTTP header analysis, directory discovery, network sniffing, SSL/TLS certificate validation, vulnerability scanning, and report generation.

This toolkit is built for cybersecurity professionals, ethical hackers, and penetration testers, enabling them to identify vulnerabilities, misconfigurations, and potential security risks in their target environments.

---

## Key Features:
- **Port Scanner**: Scan the network for open ports on a target system to identify active services.
- **Brute Force Login**: Perform brute-force attacks to test for weak or default credentials on login pages.
- **HTTP Header Analyzer**: Inspect HTTP headers for common misconfigurations and missing security headers.
- **Directory Buster**: Use wordlists to discover hidden directories or files on a web server.
- **Network Sniffer**: Capture network traffic to analyze packets and potential vulnerabilities in the network.
- **SSL/TLS Certificate Scanner**: Validate SSL/TLS certificates for proper configuration and security.
- **Vulnerability Scanner**: Perform scans to detect known vulnerabilities and weaknesses on the target system.
- **Report Generator**: Generate detailed HTML reports documenting test results, vulnerabilities, and findings.

---

## Installation Instructions:
Follow these steps to install and set up the **Penetration Testing Toolkit**:

1. **Clone the Repository**:
   Clone the repository from GitHub to your local system:
   ```bash
   git clone https://github.com/yourusername/penetration-testing-toolkit.git
   ```

2. **Navigate to the Project Directory**:
   Change your directory to the cloned project:
   ```bash
   cd penetration-testing-toolkit
   ```

3. **Set Up a Virtual Environment** (Recommended):
   To avoid conflicts with existing Python packages, it’s recommended to use a virtual environment.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Dependencies**:
   Install all the necessary libraries using:
   ```bash
   pip install -r requirements.txt
   ```

---

## Required Libraries:
Ensure the following libraries are installed for the toolkit to function properly:
```bash
pip install requests scapy paramiko beautifulsoup4 ssl nmap urllib3 colorama
```

---

## Usage:

Once the dependencies are installed, you can execute the **Penetration Testing Toolkit** by running the `main.py` script. The script will present an interactive menu for selecting various penetration testing modules.

```bash
python main.py
```

You will be presented with the following options to perform various tasks:

### Available Modules:
1. **Port Scanner** - Scan a target system for open ports and services.
2. **Brute Force Login** - Attempt brute-force attacks to test login page security.
3. **HTTP Header Analyzer** - Analyze HTTP headers for security misconfigurations.
4. **Directory Buster** - Discover hidden directories or files using wordlists.
5. **Network Sniffer** - Capture and analyze network traffic to detect vulnerabilities.
6. **SSL/TLS Certificate Scanner** - Inspect SSL certificates for potential security risks.
7. **Vulnerability Scanner** - Scan a system for known vulnerabilities and weaknesses.
8. **Generate Report** - Generate and save detailed HTML reports of your findings.
9. **Exit** - Exit the toolkit.

---

## Example Usage:

### Example 1: Port Scanner
1. Select option `1` from the menu (Port Scanner).
2. Enter the target IP address or domain name.
3. The tool will scan for open ports and services and display the results.

### Example 2: Brute Force Login
1. Select option `2` (Brute Force Login).
2. Enter the target URL of the login page.
3. Choose a wordlist and begin the brute-force attempt to crack the login credentials.

### Example 3: Directory Buster
1. Select option `4` (Directory Buster).
2. Provide the target URL and path to a wordlist file for the directory discovery.
3. The tool will attempt to uncover hidden files or directories based on the wordlist.

---

## Report Generation:
Once a test is completed, you can generate an HTML report containing detailed results. The report will include:
- Test Type
- Target Information
- Test Results
- Any vulnerabilities or findings detected

The report will be saved in the `reports/` directory of your project.

---

## Troubleshooting:
If you encounter any issues, here are some common problems and their solutions:

1. **DNS or Network Connectivity Errors**: Ensure your target is reachable, and your network connection is stable.
2. **Missing Libraries**: If you see errors related to missing libraries, ensure all dependencies are installed correctly by running `pip install -r requirements.txt`.
3. **Permission Issues**: Ensure you have the required permissions to execute the scripts and write files in the report directory.

For further assistance, feel free to open an issue in the GitHub repository.

---
## Contact:
If you have any questions or inquiries, feel free to contact me:

- **Developer**: Suraj Borkute
- **GitHub**: [https://github.com/Surajkecode](https://github.com/Surajkecode)
- **Email**: [surajborkute9881392842@gmail.com](mailto:surajborkute9881392842@gmail.com)
- **LinkedIn Profile**: [https://www.linkedin.com/in/suraj-borkute-512665341](https://www.linkedin.com/in/suraj-borkute-512665341)

---
## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements:
We would like to express our gratitude to the open-source community for their contributions to the tools and libraries used in this project. Special thanks to **Neela Santosh Kumar** for providing mentorship and guidance during the development of this toolkit.
