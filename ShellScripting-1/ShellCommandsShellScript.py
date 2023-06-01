import paramiko

# EC2 instance details
hostname = input("Enter the hostname: ")
username = input("Enter the username: ")
private_key_path = input("Enter the private_key_path: ")
output_file = input("Enter the output file name (.txt): ")

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load the private key
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Connect to the EC2 instance
ssh.connect(hostname, username=username, pkey=private_key)

# Run the single-line Python script on the instance
stdin, stdout, stderr = ssh.exec_command("top -b -n 1 -o %CPU | awk 'NR>7 {print $1, $9, $10, $12, $2}' | sort -k2 -nr | head -n 5")

# Read the output of the command
top_output = stdout.read().decode("utf-8")

# Print the sorted output to the console
headers = "PID %CPU %MEM COMMAND USER"
print(headers)
print("-" * len(headers))
print(top_output)

# Save the sorted output to a text file
with open(output_file, "w") as file:
    file.write(headers + "\n")
    print("-" * len(headers))
    file.write(top_output)
