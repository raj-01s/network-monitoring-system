# Network Monitoring Tool

A simple Python-based command-line tool to monitor the status of multiple devices (like routers, DNS servers, etc.) by sending ping requests. The results are logged into a file (`network_log.txt`) for future reference.

## Features
- Monitor multiple devices by IP address.
- Logs results with timestamp and device status (UP/DOWN).
- Saves logs to `network_log.txt`.
- Interactive CLI: start monitoring for a given number of rounds or exit anytime.

## Requirements
- Python 3.x
- Works on **Windows** (uses `ping -n`).
  - For Linux/MacOS, change `ping -n 1` to `ping -c 1` in the code.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/network-monitoring-tool.git
   cd network-monitoring-tool
   ```

2. Run the script:
   ```bash
   python network_monitor.py
   ```

## Usage
1. Start the program.
2. Type `start` to begin monitoring.
3. Enter how many rounds of checks you want.
   - Each round checks all listed devices.
   - Waits 10 seconds between rounds.
4. Type `exit` to quit.

Example interaction:
```
=== Network Monitoring Tool ===

 Type 'start' to begin checking or 'exit' to quit: start
 How many times should I check the network? 3

 Starting network checks (3 rounds)...

 --- Round 1 of 3 ---
 [2025-10-05 21:05:00] Router (192.168.1.1) is UP
 [2025-10-05 21:05:00] Google DNS (8.8.8.8) is UP
 [2025-10-05 21:05:00] Cloudflare DNS (1.1.1.1) is DOWN

 Waiting 10 seconds before next check...
```

## Output
- Results are displayed in the terminal.
- Logs are saved in `network_log.txt` with timestamps.

## Customization
- You can add/remove devices in the `devices` dictionary inside the script:
```python
devices = {
    "Router": "192.168.1.1",
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1"
}
```

## License
This project is licensed under the MIT License.
