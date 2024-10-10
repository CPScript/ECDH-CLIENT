// src/network.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Establish a connection with a server
int establishConnection(const char* hostname, int port) {
  int sockfd;
  struct sockaddr_in server_addr;

  // Create a socket
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0) {
    perror("socket");
    exit(1);
  }

  // Set up the server address
  server_addr.sin_family = AF_INET;
  server_addr.sin_port = htons(port);
  inet_pton(AF_INET, hostname, &server_addr.sin_addr);

  // Connect to the server
  if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
    perror("connect");
    exit(1);
  }

  return sockfd;
}

// Send a message over a socket
void sendMessage(int sockfd, const char* message) {
  send(sockfd, message, strlen(message), 0);
}

// Receive a message over a socket
void receiveMessage(int sockfd, char* buffer) {
  recv(sockfd, buffer, 1024, 0);
}

// Close a socket
void closeSocket(int sockfd) {
  close(sockfd);
}
