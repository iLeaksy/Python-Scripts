import subprocess

# Function to open a port in the firewall and allow connections
def open_port(port, protocol):
  subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=OpenPort' + str(port), 'dir=in', 'protocol=' + protocol, 'localport=' + str(port), 'action=allow'])

# Main function to open ports specified by the user
def main():
  while True:
    port = input('Enter the port number: ')
    protocol = input('Enter the protocol (TCP or UTP): ')
    open_port(port, protocol)

if __name__ == '__main__':
  main()