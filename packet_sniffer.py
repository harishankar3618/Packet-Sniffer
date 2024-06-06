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
        print(f"Packet sniffing started on interface {interface}. Press Ctrl+C to stop.")

        # Read the output of tcpdump line by line
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8').strip())

    except KeyboardInterrupt:
        # Handle keyboard interrupt to gracefully exit
        process.terminate()
        print("\nPacket sniffing stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")


def select_interface():
    """
    Select a network interface for packet sniffing.
    Returns:
        str: The selected network interface.
    """
    try:
        interfaces = subprocess.check_output(["ifconfig"]).decode("utf-8")
        print("Available network interfaces:")
        print(interfaces)
        interface = input("Enter the interface name you want to sniff packets on: ").strip()
        return interface
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode('utf-8')}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    interface = select_interface()
    if interface:
        start_packet_sniffer(interface)
    else:
        print("Exiting...")
