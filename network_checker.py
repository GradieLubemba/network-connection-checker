
import socket
from datetime import datetime

def check_connection(host, port=443, timeout=5):
    """Check whether a host is reachable on a TCP port."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.gaierror, OSError):
        return False


def main():
    websites = [
        ("Google", "www.google.com"),
        ("Microsoft", "www.microsoft.com"),
        ("GitHub", "github.com"),
    ]

    print("=" * 45)
    print("       NETWORK CONNECTION CHECKER")
    print("=" * 45)
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print()

    for name, host in websites:
        print(f"Checking {name} ({host})...", end=" ")
        if check_connection(host):
            print("CONNECTED")
        else:
            print("UNREACHABLE")

    print()
    print("Check complete.")


if __name__ == "__main__":
    main()
