import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('junk90yard@gmail.com','tesu tkfd pikb qlza')

server.sendmail('junk90yard@gmail.com','harishastro18@gmail.com','mail content')
print("mail sent ")