import socket

sockett = socket.socket(socket.AF_INET,  socket. SOCKET_STREAM)
sockett.connect(('data.pr4e.org', 80))
cmd = 'Get '
# will continue from here
