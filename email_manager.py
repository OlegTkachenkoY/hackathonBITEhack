import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re 
sender_email="youremail@gmail.com"
port = 465  # For SSL
# password = input("Type your password and press enter: ")
password = "Yourpassword!"
receiver_email = input("Type receiver email and press enter: ")
#create email validation
def email_validation(email):
    if re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', email):
        return True
    else:
        return False

if email_validation(receiver_email):  
  message = MIMEMultipart("alternative")
  message["Subject"] = "multipart test"
  message["From"] = sender_email
  message["To"] = receiver_email


  text = """\
  Hi,
  """
  html = """\
  <html>
    <body>
      <p>
         Drogi Użytkowniku,<br><br>
  
  Niestety twoje konto jest zablokowane, a komentarze zostały uznane za mowę nienawiści i usunięte.<br><br>
  Jeśli chcesz zobaczyć szczegóły, zaloguj się na swoje konto w serwisie Kontroli Hejtu - używając konta google.<br><br>
  
  Pod tym linkiem znajdziesz interesujący Cię formularz.<br><br>
  
  
  Pozdrawiamy,<br><br>
  Zespół do walki z Mową Nienawiści<br><br>
  
    <p>
         
         This email has been sent automatically, please do not reply.
         
    </p>
    </body>
  </html>
  """


  
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")
  
  
  message.attach(part1)
  message.attach(part2)
  # Create a secure SSL context
  context = ssl.create_default_context()
  
  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())
    
