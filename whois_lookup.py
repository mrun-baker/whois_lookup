import whois

# Ask the user to input a domain name or IP address
domain_or_ip = input("Enter the domain name or IP address you want to check: ")

try:
    # Perform the WHOIS lookup
    domain_info = whois.whois(domain_or_ip)

    # Print the registration details
    print("Domain Name:", domain_info.domain_name)
    print("Registrar:", domain_info.registrar)
    print("Creation Date:", domain_info.creation_date)
    print("Expiration Date:", domain_info.expiration_date)
    print("Updated Date:", domain_info.updated_date)
    print("Name Servers:", domain_info.name_servers)
    
    # Print additional details if available
    print("Domain Owner:", domain_info.get('org', 'Not available'))
    print("Technical Contact Email:", domain_info.get('emails', 'Not available'))
    print("Technical Contact Phone:", domain_info.get('phone', 'Not available'))
except Exception as e:
    print(f"An error occurred: {e}")
