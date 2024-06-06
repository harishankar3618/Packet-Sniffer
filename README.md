# Packet Sniffer

This Python script is a packet sniffer that captures and analyzes network packets. It provides detailed information about Ethernet frames, IPv4 packets, TCP segments, and UDP segments.

## Features

- **Comprehensive Packet Analysis**: Parses Ethernet frames, IPv4 packets, TCP segments, and UDP segments to extract key information such as MAC addresses, IP addresses, ports, and protocol details.
- **Flexible Interface Selection**: Allows users to select the network interface for packet capture, providing versatility in monitoring different network connections.
- **Graceful Error Handling**: Implements robust exception handling to ensure smooth operation even in the face of unexpected errors or interruptions.

## Usage

1. Ensure you have Python 3 installed on your system.
2. Run the `packet_sniffer.py` script.
3. Follow the on-screen instructions to select the network interface for packet capture.
4. The script will start capturing packets and displaying relevant information.
5. Press Ctrl+C to stop packet capture and exit the script.

## Requirements

- Python 3
- Administrative privileges (may be required for capturing packets using raw sockets)

## Disclaimer

This packet sniffer is intended for educational purposes only. Always use it responsibly and ensure compliance with ethical and legal considerations. Unauthorized interception of network traffic is illegal and unethical.

