import SocketServer

class DatagramHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    data = self.request[0].strip()
    socket = self.request[1]
    print data

if __name__ == "__main__":
  server = SocketServer.UDPServer(('localhost', 3000), DatagramHandler)
  server.serve_forever()
