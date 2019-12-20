#Service capable of doing basic mathematical operations: add, substract, multiply, and divide two given numbers

#Import Libraries
import socket

#Define functions
def add(x, y):                                                      #This function adds two numbers    
    try:
        return x + y
    except (ValueError, TypeError):
        print("Error occurred")

def substract(x, y):                                                #This function subtracts two numbers    
    try:
        return x - y
    except (ValueError, TypeError):
        print("Error occurred")

def multiply(x, y):                                                 #This function multiplies two numbers    
    try:
        return x * y
    except (ValueError, TypeError):
        print("Error occurred")

def divide(x, y):                                                   #This function divides two numbers    
    try:
        return x / y
    except ZeroDivisionError:
        print("An error has occurred due to zero division")
    except (ValueError, TypeError):
        print("Error occurred")

port = 3000                                                         # Reserve a port for your service.
bufsize = 1024                                                      
server = socket.socket()                                            # Create a socket object
server.bind(('', port))                                             # Bind to the port
print ('Server ready at 127.0.0.1')
server.listen(5)                                                    # Now wait for client connection.
client, address = server.accept()                                   # Establish connection with client.
print ('Got connection from', address)
while True:
	data = []
	result = 0;
	data.append(client.recv(bufsize))                           # Receive the first operand value from the client
	if data[0] == 'exit':                                       # If received exit shut down the connection
		print ('Exiting')
		server.close()
		client.close()
		break
	data.append(client.recv(bufsize))                           # Receive the operation from the client
	data.append(client.recv(bufsize))                           # Receive the second operand value from the client
	
        # Call the function to operate the given values depending on the operation given
	if data[1].decode() == '+':		
                result = add(int(data[0]),int(data[2]))
	elif data[1].decode() == '-':
		result = substract(int(data[0]),int(data[2]))
	elif data[1].decode() == '*':
		result = multiply(int(data[0]),int(data[2]))
	elif data[1].decode() == '/':
		result = divide(int(data[0]),int(data[2]))
		
	print (data[0].decode(), data[1].decode(), data[2].decode(), '=', result) #Show the operation, values and result

	# Send the result data to the client 
	client.sendto(str(result).encode(),(address))               # Used str.encode() to convert the strings to bytes
	client.sendto(str(result).encode(),(address))
	
	print ('Data send back to the Client')
