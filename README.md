# RPC Implementation and Deployment on AWS EC2

This project is a part of the Distributed Computing Lab. It demonstrates a custom **Remote Procedure Call (RPC)** system implemented in Python, deployed on two separate **AWS EC2** instances.

## Project Overview
The system allows a Client node to perform a mathematical operation (`add`) on a Server node remotely. The communication is handled over a TCP network using JSON for data serialization.

##  Features Implemented
- **Marshalling/Unmarshalling**: Data is converted into JSON format for network transmission.
- **Unique Request IDs**: Each request is assigned a unique UUID to track transactions and ensure consistency.
- **Timeout Handling**: The client has a built-in 2-second timeout to prevent hanging.
- **Retry Logic**: If the server is unavailable, the client automatically retries the request up to 3 times.
- **At-Least-Once Semantics**: The system ensures that the request is delivered and processed through its retry mechanism.

##  Repository Structure
- `server.py`: The Server stub that listens for connections and executes the remote function.
- `client.py`: The Client stub that initiates requests, handles timeouts, and retries.
- `README.md`: Project documentation and instructions.

##  Deployment Details
- **Infrastructure**: 2x AWS EC2 instances (t2.micro / Ubuntu 22.04).
- **Security Group Rules**: 
  - Port 22 (SSH) opened for both nodes.
  - Port 5000 (TCP) opened on the Server node for RPC traffic.
