# Gmail Auto-Response Python Script
This script allows you to send an automated response to the latest sender of an email in your Gmail inbox. The script uses the `imaplib` and `smtplib` libraries in Python to connect to the Gmail IMAP4_SSL and SMTP_SSL servers, respectively, and perform actions such as fetching emails and sending emails.

## Prerequisites
- A Gmail account
- An App Password for your Gmail account, refer to this [link]("https://support.google.com/accounts/answer/185833?hl=en") to generate one.
## Usage
- Clone the repository to your local machine.
- Open the `index.py` file in a text editor and replace your Gmail Id with your Gmail email address and your app password with your App Password.
- Run the script by executing the command `python index.py` in your terminal.
## Functionalities
The script has three main functions:

`get_latest_sender()` : This function retrieves the name and email address of the latest email sender in the Gmail inbox.

`send_email(to, name)` : This function sends an automated response email to the recipient specified by the to parameter, which is their email address, and the name parameter, which is their name.

`main()` : This is the main function of the script that calls the get_latest_sender function and then sends an automated response to the latest email sender using the send_email function.

The script runs in an infinite loop, constantly checking for the latest email sender and sending an automated response until it is interrupted.

### Note
The script assumes that the latest email in the Gmail inbox is the latest email received. This may not always be the case as new emails may be received while the script is running. However, it is a reasonable assumption for the purpose of sending an automated response.