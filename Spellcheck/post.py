import smtplib, ssl

def sendemail( email ):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "spellcheckerresidence@gmail.com"
    password = "Hahahaha1"
    message = "You have successfuly registered! Welcome to the spellchecker! Thank you!"
    receiver_email = email

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
    return
