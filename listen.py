import json
import SocketServer

class DatagramHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        samp = self.request[0].strip().strip(';').split(' ')
        #XXX: should we need to raise here (if samp.__len__ =! 31)?
        chan = samp[0]
        samp.__delitem__(0)
        datastreams = [{'id':chan+'.'+str(i), 'current_value':x} for i,x in enumerate(samp)]
        print json.dumps(datastreams)


if __name__ == "__main__":
    server = SocketServer.UDPServer(('localhost', 3000), DatagramHandler)
    server.serve_forever()
