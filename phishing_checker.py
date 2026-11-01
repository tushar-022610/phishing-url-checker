from urllib.parse import urlsplit
import ipaddress


def check_url(url):
    warnings = []

    # Check @ symbol
    if "@" in url:
        warnings.append("URL contains '@' symbol.")

    # Check URL length
    if len(url) > 100:
        warnings.append("URL is longer than 100 characters.")

    try:
        parsed = urlsplit(url)

        hostname = parsed.hostname or ""
        scheme = parsed.scheme.lower()

        # Check IP address as hostname
        try:
            ipaddress.ip_address(hostname)
            warnings.append("Hostname is an IP address.")
        except ValueError:
            pass

        # Check number of hostname labels
        labels = hostname.split(".")
        if len(labels) >= 5:
            warnings.append("Hostname contains 5 or more labels/subdomains.")

        # Check punycode
        if "xn--" in hostname.lower():
            warnings.append("Hostname contains possible punycode.")

        # Check HTTP
        if scheme == "http":
            warnings.append("URL uses HTTP instead of HTTPS.")

    except ValueError:
        warnings.append("URL format could not be parsed.")

    return warnings


def main():
    print("=" * 50)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 50)
    print("This tool checks URL text for common warning signs.")
    print("It does NOT open URLs or make network requests.")

    while True:
        print("\n1. Check a URL")
        print("2. Review warning signs")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            url = input("\nEnter URL: ").strip()

            if not url:
                print("Please enter a URL.")
                continue

            warnings = check_url(url)

            print("\n--- RESULT ---")

            if warnings:
                print(f"Warning signs found: {len(warnings)}")
                for number, warning in enumerate(warnings, 1):
                    print(f"{number}. {warning}")
                print("\nReminder: These are awareness indicators,")
                print("not proof that a website is malicious.")
            else:
                print("No common warning signs detected.")

        elif choice == "2":
            print("\n--- COMMON PHISHING WARNING SIGNS ---")
            print("1. '@' symbol in the URL")
            print("2. Very long URL")
            print("3. IP address used as hostname")
            print("4. Many subdomains/hostname labels")
            print("5. Punycode (xn--) in hostname")
            print("6. HTTP instead of HTTPS")

        elif choice == "3":
            print("\nThank you for using the Phishing URL Awareness Checker.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name
