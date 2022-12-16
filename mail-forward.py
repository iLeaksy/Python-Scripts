import imaplib
import email
import smtplib

# Replace these values with your own email account information
imap_server = 'imap.example.com'
username = 'user@example.com'
password = 'password'

# Replace this value with the email address you want to forward the emails to
forward_to = 'forward@example.com'

# Connect to the email server
imap_conn = imaplib.IMAP4_SSL(imap_server)
imap_conn.login(username, password)

# Select the mailbox you want to retrieve emails from
imap_conn.select('INBOX')

# Search for all unread emails
_, email_ids = imap_conn.search(None, 'UNSEEN')

# Split the email IDs into a list
email_ids = email_ids[0].split()

# Iterate over the email IDs and forward each email to the specified address
for email_id in email_ids:
    # Retrieve the email
    _, msg = imap_conn.fetch(email_id, '(RFC822)')
    msg = msg[0][1]
    msg = email.message_from_bytes(msg)

    # Create a SMTP connection
    smtp_conn = smtplib.SMTP('smtp.example.com')
    smtp_conn.login(username, password)

    # Forward the email
    smtp_conn.sendmail(username, forward_to, msg.as_bytes())

    # Close the SMTP connection
    smtp_conn.quit()

# Close the IMAP connection
imap_conn.close()
imap_conn.logout()