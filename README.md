# heck-buffeasy
This repo is for bufferover flow scripts 

So how to use this file is a very critical thing but i try to explain easily

this is an python program for fuzzing any application
  to fuzz (means searching for desire amount of data you have to send to crash application)
  
  requirement 
  
  ip ,port , prefix ,buffer
  
  what is prifix?
  some application need prifix like "buffer1" then after typing this then we can only send
  arguments this is also need when you have to specify which parameter you want to exploit
  
  what is buffer?

  buffer is nothing just a amount of argument lenght we have to send to application to crash

  after knowing the size go to exploit.py  
  
  create a pattern in your linux system 
   msf-pattern_create -l (lenght of buffer you find above)
   
  # after this paste in exploit.py < string ="paste here"
   
   save file and run
   
   now check the eip location in debugger
   after noting down eip location.
   now we have to find the exact match of location in msf
   
   msf-pattern_offset -l (lenght of buffer) -q (location)
   
   
   after finding exact location
   now you know where is eip memory 
   
  # go to exploiteip.py
   just overwrite by jump esp present in program 
   
   after that find location for payload 
   paste it 
   run
   
   exploit done .
   
