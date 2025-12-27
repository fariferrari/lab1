RPC Implementation & Deployment on AWS EC2
This repository contains a custom Remote Procedure Call (RPC) system built for a Distributed Computing lab. The system is deployed on AWS EC2 using two separate nodes: a Client and a Server.

Project Overview:
The goal of this project is to simulate a distributed environment where a client requests a computation (addition) from a remote server. The communication is handled over TCP using JSON as the marshalling format.

Features:
Custom RPC Protocol: Uses JSON for request and response formatting.

Marshalling/Unmarshalling: Handles data conversion for network transmission.

Unique Request IDs: Every client request is assigned a unique UUID to track the transaction.

Retry Logic: The client includes a 2-second timeout and automatically retries the request up to 3 times if a failure occurs.

At-Least-Once Semantics: Ensures the request is delivered and processed even in the event of temporary network issues.

Repository Structure:
server.py: The Server Stub that listens for connections and executes the add(a, b) function.

client.py: The Client Stub that marshals data, handles timeouts, and performs retries.
