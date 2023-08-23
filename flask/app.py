from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
  template = "<h3>Hello {name}!</h3><b>Hostname: </b>{hostname}"
  return template.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000)
