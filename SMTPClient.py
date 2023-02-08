#!/usr/bin/env python3

# Include needed libraries. Do _not_ include any libraries not included with
# Python3 (i.e. do not use `pip` use 'pip3' instead of installs).
import socket


# Establish a TCP connection with the mail server.
TCP_IP = '127.0.0.1'
TCP_PORT = 25
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


# Read greeting from the server
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

# if not response.startswith('220'):
# 	raise Exception('220 reply not received from server.')

# Send HELO command and get server response.
cmd_HELO = 'HELO alice\r\n'
print(cmd_HELO)
s.send(cmd_HELO.encode())

response = s.recv(4096).decode('utf-8')
print(response)

if not response.startswith('250'):
    raise Exception('250 reply not received from server.')


# Send MAIL FROM command.
cmd_MAIL_FROM = 'MAIL FROM: <test@test.com> \r\n'
s.send(cmd_MAIL_FROM.encode())

# Send RCPT TO command. You will send to <sys> which account on the VM.
cmd_RCPT_TO = 'RCPT TO: <sys>\r\n'
s.send(cmd_RCPT_TO.encode())
response = s.recv(4096).decode('utf-8')

# Send DATA command.
cmd_DATA = 'DATA\r\n'
s.send(cmd_DATA.encode())
response = s.recv(4096).decode('utf-8')

# Send message data.
cmd_MSG = 'Subject: SMTP e-mail test\r\n\r\nThis is a test e-mail message.\r\n.\r\n'
s.send(cmd_MSG.encode())

# End with line with a single period.
s.send('.\r\n'.encode())

# Send QUIT command.
cmd_QUIT = 'QUIT\r\n'
s.send(cmd_QUIT.encode())

# Close the socket when finished.
s.close()