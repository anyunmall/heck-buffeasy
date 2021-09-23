#!/usr/bin/env python3
/*this is an python program for fuzzing any application
  to fuzz (means searching for desire amount of data you have to send to crash application)
  
  requirement 
  
  ip ,port , prefix ,buffer
  
  what is prifix?
  some application need prifix like "buffer1" then after typing this then we can only send
  arguments this is also need when you have to specify which parameter you want to exploit
  
  what is buffer?

  buffer is nothing just a amount of argument lenght we have to send to application to crash

  after knowing the size go to exploit.py  
  
*/

import socket,sys,time

ip = ""
port = 
prefix = ""
Buffer = prefix + "A" * 100

while True:
  try:
      s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(Buffer)))
      s.send(bytes(Buffer, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(Buffer)))
    sys.exit(0)
  Buffer += 100 * "A"
  time.sleep(1)
