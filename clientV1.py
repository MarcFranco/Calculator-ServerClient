#Client that interacts with the server by getting the values from the command line and performing its mathematical operation

#Import Libraries
import socket

port = 3000                                                                             # Port reserved by the server to connect
bufsize = 1024
client = socket.socket()                                                                # Create a socket object
ipaddr = input('Connect to IP: ')                                                       # Type the server IP: LocalHost(127.0.0.1)
client.connect((ipaddr, port))                                                          # Connect to the IP adress specified and the server port 
print ('Connected to server')

while True:
        
    operandA = input('Value 1: ')                                                       # Get the first value by keyboard input                                                    
    operator = input('Operation: ')                                                     # Get the operation by keyboard input 
    operandB = input('Value 2: ')                                                       # Get the second value by keyboard input

    # Send the data to the server
    client.sendto(operandA.encode(),(ipaddr,port))                                       
    client.sendto(operator.encode(),(ipaddr,port))
    client.sendto(operandB.encode(),(ipaddr,port))
            
    print (operandA, operator, operandB, '=', client.recv(bufsize).decode())            # Show the operation, values and result                
            
    if 'exit' == input('Type "exit" to exit, no input to continue \n'):                 # Shut down the connection with the server when exit is entered
        client.sendto('exit'.encode(),(ipaddr,port))
        client.close()
        exit()
