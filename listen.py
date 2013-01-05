import SocketServer

class DatagramHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        samp = self.request[0].strip().strip(';').split(' ')
        #XXX: should we need to raise here (if samp.__len__ =! 31)?
        chan = samp.pop(0)
        #XXX: find out if I need to look-up the frequency band's value in Hz for datastream name
        print '\n'.join([chan+'.'+str(i)+','+x for i,x in enumerate(samp)])


if __name__ == "__main__":
    server = SocketServer.UDPServer(('localhost', 3000), DatagramHandler)
    server.serve_forever()
