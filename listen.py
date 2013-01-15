import os, select, socket

buffer_size = 8192

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 3000))
s.setblocking(0)

pd = os.spawnlp(os.P_NOWAIT, 'pd', 'pd', '-nogui', 'test-1.pd')
print "Started pd (PID: %d)" % pd

while True:
    result = select.select([s],[],[])
    samp = result[0][0].recv(buffer_size).strip().strip(';').split(' ')
    #XXX: should we need to raise here (if samp.__len__ =! 31)?
    chan = samp.pop(0)
    #XXX: find out if I need to look-up the frequency band's value in Hz for datastream name
    print '\n'.join([chan+'.'+str(i)+','+x for i,x in enumerate(samp)])

