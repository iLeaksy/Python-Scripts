import os
import socket
import time

# Function to check if an IP is responding
def check_ip(ip):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(5)
  try:
    s.connect((ip, 80))
    s.close()
    return True
  except:
    return False

# Function to send an SMS
def send_sms(message):
  # Add code here to use a third-party SMS API to send the message to your phone
  pass

# Main function to check the IP and send an SMS if necessary
def main():
  ip = '141.136.9.110'

  while True:
    print('Server up')
    if not check_ip(ip):
      send_sms('The IP is not responding!')

    time.sleep(60)  # Check every 60 seconds

if __name__ == '__main__':
  main()