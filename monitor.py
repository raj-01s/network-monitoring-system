import os
import time
from datetime import datetime

# List of devices to monitor
devices = {
    "Router": "192.168.1.1",
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1"
}

print("=== Network Monitoring Tool ===")

while True:
    command = input("\n Type 'start' to begin checking or 'exit' to quit: ").strip().lower()

    if command == "exit":
        print("Exiting program. Goodbye!")
        break

    elif command == "start":
        try:
            rounds = int(input("How many times should I check the network? "))
        except ValueError:
            print(" Please enter a valid number.")
            continue

        print(f"\n Starting network checks ({rounds} rounds)...\n")

        with open("network_log.txt", "a") as log:
            for i in range(rounds):
                print(f"--- Round {i+1} of {rounds} ---")

                for name, ip in devices.items():
                    response = os.system(f"ping -n 1 {ip} >nul 2>&1")
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    status = "UP" if response == 0 else "DOWN"
                    line = f"[{now}] {name} ({ip}) is {status}\n"

                    print(line.strip())
                    log.write(line)
                    log.flush()

                print("\n Waiting 10 seconds before next check...\n")
                time.sleep(10)

        print("\n Monitoring complete! Results saved in network_log.txt")

    else:
        print("Invalid command. Please type 'start' or 'exit'.")