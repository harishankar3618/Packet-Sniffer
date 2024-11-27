import subprocess


def start_packet_sniffer(interface):
    """
    Start packet sniffing on the specified network interface using tcpdump.

    Args:
        interface (str): The network interface to sniff packets on.
    """
    try:
        # Define the tcpdump command
        command = ["tcpdump", "-i", interface, "-nn", "-v"]

        # Start tcpdump process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Print status message
        print(f"Packet sniffing started on interface '{interface}'. Press Ctrl+C to stop.")

        # Read the output of tcpdump line by line
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8').strip())

    except KeyboardInterrupt:
        # Handle keyboard interrupt to gracefully exit
        print("\nStopping packet sniffing...")
        process.terminate()
        process.wait()  # Ensure subprocess resources are cleaned up
        print("Packet sniffing stopped.")
    except FileNotFoundError:
        print("Error: 'tcpdump' not found. Please install it to use this tool.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def select_interface():
    """
    Select a network interface for packet sniffing.

    Returns:
        str: The selected network interface, or None if no interface is selected.
    """
    try:
        # Use 'ip a' for modern systems to list interfaces
        interfaces = subprocess.check_output(["ip", "a"]).decode("utf-8")
        print("Available network interfaces:\n")
        print(interfaces)

        # Prompt user for interface selection
        interface = input("Enter the interface name you want to sniff packets on: ").strip()
        return interface if interface else None

    except subprocess.CalledProcessError as e:
        print(f"Error while listing interfaces: {e.output.decode('utf-8')}")
        return None
    except FileNotFoundError:
        print("Error: 'ip' or 'ifconfig' command not found. Please ensure network tools are installed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    interface = select_interface()
    if interface:
        start_packet_sniffer(interface)
    else:
        print("No valid interface selected. Exiting...")
