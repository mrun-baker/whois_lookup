# WHOIS Lookup Script

This Python script performs a WHOIS lookup for a given domain name or IP address and prints the registration details, including the domain owner, technical contact email, and phone number if available.

## Features

- Prompts the user to input a domain name or IP address.
- Retrieves and displays WHOIS information such as:
  - Domain Name
  - Registrar
  - Creation Date
  - Expiration Date
  - Updated Date
  - Name Servers
  - Domain Owner
  - Technical Contact Email
  - Technical Contact Phone

## Requirements

- Python 3.x
- `python-whois` module

## Installation

1. Clone the repository or download the script file.

2. Install the required module using pip:
   ```bash
   pip install python-whois
Usage
Rename the script file to avoid naming conflicts (e.g., whois_lookup.py).

Run the script:

python whois_lookup.py
Enter the domain name or IP address when prompted:

Enter the domain name or IP address you want to check: example.com
The script will display the WHOIS information:

Domain Name: EXAMPLE.COM
Registrar: Example Registrar, Inc.
Creation Date: 2000-01-01 00:00:00
Expiration Date: 2025-01-01 00:00:00
Updated Date: 2023-01-01 00:00:00
Name Servers: ['NS1.EXAMPLE.COM', 'NS2.EXAMPLE.COM']
Domain Owner: Example Organization
Technical Contact Email: contact@example.com
Technical Contact Phone: +1.234567890
Error Handling
If an error occurs during the WHOIS lookup, the script will print an error message:

An error occurred: [error message]
