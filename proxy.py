import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 3000               # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr

while 1:
    data = conn.recv(4096) # Getting all the data
    if not data: break # No data break out of it

    # Printing data and sending back
    print data
    conn.send(data)

# Exiting everything and returning
conn.close()
