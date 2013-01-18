import os, select, socket

from sys import argv

buffer_size = 8192

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 3000))
s.setblocking(0)

pd = os.spawnlp(os.P_NOWAIT, 'pd', 'pd', '-alsa', '-nodac', '-nogui', argv[1])
print "Started pd (PID: %d)" % pd

lookup = [
    '25', '31.5', '40', '50', '63', '80', '100', '125', '160', '200',
    '250', '315', '400', '500', '630', '800', '1000', '1250', '1600', '2000',
    '2500', '3150', '4000', '5000', '6300', '8000', '10000', '12500', '16000', '20000',
]

while True:
    result = select.select([s],[],[])
    samp = result[0][0].recv(buffer_size).strip().strip(';').split(' ')
    #XXX: should we need to raise here (if samp.__len__ =! 31)?
    chan = samp.pop(0)
    #XXX: find out if I need to look-up the frequency band's value in Hz for datastream name
    print '\n'.join([chan+'-'+lookup[i]+','+x for i,x in enumerate(samp)])

