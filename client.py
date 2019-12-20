# Client that interacts with the server by reading a CSV file with the mathematical operations and sends a http request to the server
# The whole operation with the result is shown in the command line and also written in a new CSV file 

# Import Libraries
import socket
import csv
from csv import reader, writer

port = 3000                                                                             # Port reserved by the server to connect
bufsize = 1024
client = socket.socket()                                                                # Create a socket object
ipaddr = input('Connect to IP: ')                                                       # Type the server IP: LocalHost(127.0.0.1)
client.connect((ipaddr, port))                                                          # Connect to the IP adress specified and the server port 
print ('Connected to server')

with open('sample.csv', 'r') as in_file, open('sampleAnswer.csv' , 'w') as out_file:    # Open the reading and writting files
    reader1 = csv.reader(in_file)                                                       # Write the headers for the result file
    writer = csv.writer(out_file)                                                       # Write the headers for the result file
    writer.writerow(['Value1', 'Operator', 'Value 2', 'Result'])                        # Write the headers for the result file    
  
    while True:
        for row in reader1:
	    
            operandA = row[0]                                                           # Read the first value (Operand 1) of the file	    
            operator = row[1]                                                           # Read the second value (Operation) of the file	    
            operandB = row[2]                                                           # Read the third value (Operand 2) of the file

            # Send the data to the server
            client.sendto(operandA.encode(),(ipaddr,port))
            client.sendto(operator.encode(),(ipaddr,port))
            client.sendto(operandB.encode(),(ipaddr,port))

            
            print (operandA, operator, operandB, '=', client.recv(bufsize).decode())    # Show the operation, values and result                
            writer.writerow([operandA,operator,operandB,client.recv(bufsize).decode()]) # Write the result in a file   

            if 'exit' == input('Type "exit" to exit, no input to continue \n'):         # Shut down the connection with the server when exit is entered
                    client.sendto('exit'.encode(),(ipaddr,port))
                    client.close()
                    exit()
