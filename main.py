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

# Update the server and install basics, then run a setup script for docker and vpn
setup_commands = [
    "suto apt-get update -y",
    "sudo apt-get upgrade -y",
    "sudo apt-get install curl -y",
    "curl -O https://raw.githubusercontent.com/o-libSyntax-o/server_control/main/setup.sh",
    "bash setup.sh",
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
