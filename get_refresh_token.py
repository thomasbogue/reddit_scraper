#!/usr/bin/env python

import random
import socket
import sys

import praw

import key

def received_connection():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(("localhost",8080))
  server.listen(1)
  client = server.accept()[0]
  server.close()
  return client

def send_message(client, message):
  print(message)
  client.send(f"HTTP/1.1 200 OK\r\n\r\n{message}".encode("utf-8"))
  client.close()

def main():
  scopes = ["*"]
  reddit = praw.Reddit(
    client_id=key.reddit_secrets["client_id"],
    client_secret=key.reddit_secrets["client_secret"],
    redirect_uri=key.reddit_secrets["redirect_uri"],
    user_agent=key.reddit_secrets["user_agent"]
  )
  state = str(random.randint(0, 65000))
  url = reddit.auth.url(scopes, state, "permanent")
  print(f"connect to {url}")

  client = received_connection()
  data = client.recv(1024).decode("utf-8")
  param_tokens = data.split(" ", 2)[1].split("?", 1)[1].split("&")
  params = {key:value for (key, value) in [token.split("=") for token in param_tokens]}
  print(params)
  if state != params["state"]:
      send_message(client, f"State mismatch. Expected {state} Received {params['state']}")
      return 1
  elif "error" in params:
    send_message(client, params["error"])
    return 1

  refresh_token = reddit.auth.authorize(params["code"])
  send_message(client, f"Refresh token: {refresh_token}")
  return 0

if __name__=="__main__":
    sys.exit(main())
