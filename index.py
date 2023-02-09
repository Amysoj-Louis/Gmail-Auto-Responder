import smtplib
from email.mime.text import MIMEText
import imaplib
import email

EMAIL = "your Gmail Id"
APP_PASS = "your Google App Password"


def get_latest_sender():
    """
    Get the latest sender of an email from the Gmail inbox.

    Returns:
        tuple: A tuple containing the name of the latest email sender and their email address.
    """
    # Connect to Gmail IMAP4_SSL server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Login to the Gmail account
    mail.login(EMAIL, APP_PASS)

    # Select the "inbox" mailbox
    mail.select("inbox")

    # Search for all emails
    _, data = mail.search(None, "ALL")
    # Retrieving the name and email address of the latest email sender

    latest_email_id = data[0].split()[-1]

    # Fetch the email body (RFC822) for the given ID
    _, data = mail.fetch(latest_email_id, "(RFC822)")

    # Extract the email message from the data
    email_message = email.message_from_string(data[0][1].decode("utf-8"))

    # Extract the name and email from the "From" field
    sender = email_message['From'].split("<")[0].title()
    senders_email = email_message['From'].split("<")[1].replace(">", "")
    currentmessageid = email_message["Message-ID"]
    return sender, senders_email, currentmessageid


def send_email(to, name):
    """
    This function is used to send an email to the specified recipient.

    Parameters:
    to (str) : email address of the recipient
    name (str) : name of the recipient

    Returns:
    str : message indicating the email has been sent to the recipient's email address
    """
    try:
        # Creating a MIMEText object with the content of the email
        msg = MIMEText(
            f"Dear {name},\n\nThank you for sending an email.\n\nBest regards,\nAmysoj J A Louis Joseph")

        # Adding subject, from and to fields to the email
        msg['Subject'] = "Automated Response"
        msg['From'] = EMAIL
        msg['To'] = to

        # Connecting to the Gmail SMTP server using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, APP_PASS)
            smtp.sendmail(EMAIL, [to], msg.as_string())
        return f"Sent automated mail to {to}"
    except Exception as e:
        return f"Couldn't send mail to {to} due to {e}"


def main():
    """
    The main function of the script, it retrieves the latest email sender and then sends an automated response to them.
    """
    previousmessageid = None
    while True:
        # Get the latest email ID
        sender_name, sender_email, currentmessageid = get_latest_sender(
        )
        if previousmessageid != currentmessageid:
            # Sending an email to the latest email sender
            status = send_email(sender_email, sender_name)
            previousmessageid = currentmessageid
            print(status)
        else:
            pass


# Checking if the script is being run as the main program and not imported as a module
if __name__ == "__main__":
    main()
