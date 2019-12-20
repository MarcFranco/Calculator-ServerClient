# Calculator-ServerClient

Author Marc Franco

Version 20/12/19

Client-Service capable of doing basic mathematical operations with Python.

There are two different versions of the code. The first one corresponds to the "clientV1.py" file. This one takes the mathematical operation by command line input and receives the server result also in the command line. 

User's Guide:

- Run "server.py" in a terminal
- Run "clientV1.py" in a different terminal
- Insert the server IP or "127.0.0.1" if run locally
- Insert the first operand value
- Insert the operation
- Insert the second operand value
- The server will send the result of the computation and the client will print the result
- (You can type "exit" to exit the program, just press enter to continue)

The other version is the "client.py" file. This one takes the mathematical operation from a CSV file and receives the server result also in the command line as well as in a CSV file. 

User's Guide:

- Run "server.py" in a terminal
- Run "client.py" in a different terminal
- Insert the server IP or "127.0.0.1" if run locally
- Insert a CSV file in the same directory with the CSV file with three columns. First column is the first value, second is the operation and third is the second value to process.
- The server will send the result of the computation and the client will print the result and store it in a CSV file.
- (You can type "exit" to exit the program, just press enter to continue)
