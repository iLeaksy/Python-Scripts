import os
import socket
import time

# Check if the server is being DDOS-ed by creating a socket and trying to connect to it
def check_ddos(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(5)
  try:
    s.connect((host, port))
    s.close()
    return False
  except:
    return True

# Function to send an email
def send_email(subject, message):
  import smtplib
  from email.mime.text import MIMEText

  # Set up email server and login
  server = smtplib.SMTP('smtp.example.com')
  server.login('username', 'password')

  # Create and send the email
  msg = MIMEText(message)
  msg['Subject'] = subject
  msg['To'] = 'you@example.com'
  msg['From'] = 'alerts@example.com'
  server.sendmail('alerts@example.com', ['you@example.com'], msg.as_string())
  server.quit()

# Main function to check for DDOS and send an email if necessary
def main():
  host = 'your_server_hostname'
  port = 80

  while True:
    if check_ddos(host, port):
      send_email('DDOS ALERT!', 'Your server is being DDOS-ed!')
    else:
      print('You are safe from DDOS!')

    time.sleep(60)  # Check every 60 seconds

if __name__ == '__main__':
  main()