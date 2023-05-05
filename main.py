import os
from dotenv import load_dotenv
import paramiko

# Load environment variables from .env file
load_dotenv()

# Get the SSH connection settings from environment variables
host = os.environ["SSH_HOST"]
port = int(os.environ.get("SSH_PORT", "22"))
username = os.environ["SSH_USERNAME"]
password = os.environ["SSH_PASSWORD"]

# Define the commands to run on the remote server
setup_commands = [
    "sudo apt-get install git -y",
]

# Connect to the remote server over SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Execute the setup commands on the remote server
    for command in setup_commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
finally:
    # Close the SSH connection
    ssh_client.close()
