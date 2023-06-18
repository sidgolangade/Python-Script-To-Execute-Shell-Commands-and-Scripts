## System Resource Monitor Script
This Python script connects to an AWS EC2 RHEL instance and retrieves system resource information using the `top` command. It then sorts the output based on CPU usage and displays the top 5 processes along with their %CPU, %MEM, COMMAND, USER, and PID.

### Prerequisites
- An AWS EC2 instance running RHEL
- Python 3.x installed on the local machine
- Required Python packages: `paramiko`

### Usage
The script will connect to the EC2 instance, retrieve the system resource information, sort and display the top 5 processes, and save the sorted output to the specified output file.

### Output
The script will display the sorted output to the console with the following information for each process:
- CPU Usage (%)
- Memory Usage (%)
- Command
- User
- PID

Additionally, the sorted output will be saved to a text file specified by the `output_file` variable.

**Note:** This script assumes that you have the necessary permissions and access credentials to connect to the AWS EC2 RHEL instance.
