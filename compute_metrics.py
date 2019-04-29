
def compute(*nodes):
    for i in range(1, 5):
        computeNode(i, nodes[i-1])

def computeNode(node, packets):
    """Compute the metrics for each node"""
    ReplyRec = [] # The reply packets that were rec.
    RequestRec = [] # The req. packets that were rec.
    ReplySent = [] # The reply packets that were sent
    RequestSent = [] # The req. packets that were rec.
    for packet in packets:
        # Handle replies
        if packet.isReply():
            # If the source node is the same as us, we sent it
            if packet.getSrcNode() == node:
                ReplySent += [packet]
            # If the dest node is us, we received it
            if packet.getDstNode() == node:
                ReplyRec += [packet]
        # Handle req.
        if packet.isRequest():
            # If the source node is the same as us, we sent it
            if packet.getSrcNode() == node:
                RequestSent += [packet]
            # If the dest node is us, we received it
            if packet.getDstNode() == node:
                RequestRec += [packet]
    
    ### Now we have sorted the packets, we can calculate metrics
    
    ### Data Size Metrics
    EchoRequestsSent = len(RequestSent)
    EchoRequestsRec = len(RequestRec)
    EchoReplySent = len(ReplySent)
    EchoReplyRec = len(ReplyRec)

    # Frame size total
    EchoRequestBytesSent = sum([p.frame_size for p in RequestSent])
    EchoRequestBytesRec = sum([p.frame_size for p in RequestRec])

    # Icmp Payload size total
    EchoRequestDataSent = sum([p.length for p in RequestSent])
    EchoRequestDataRec = sum([p.length for p in RequestRec])

    totalTime = 0
    for i in range(0, EchoRequestsSent):
        totalTime += ReplyRec[i].time - RequestSent[i].time

    AveragePingRTT = totalTime / EchoRequestsSent * 1000
    EchoRequestThroughput = EchoRequestBytesSent / totalTime / 1000
    EchoRequestGoodput = EchoRequestDataSent / totalTime / 1000


    totalTimeResponse = 0
    for i in range(0, EchoRequestsRec):
        totalTimeResponse += ReplySent[i].time - RequestRec[i].time

    AverageReplyDelay = totalTimeResponse / EchoRequestsRec * 1000000

    # Hops / Distance Metrics
    numOfHops = float(0)
    count = float(0)
    for packet in packets:
        if packet.isRequest():
            count += 1
            tmp = packet.info.split(',')
            tmp2 = tmp[2].split(' ')
            ttl = tmp2[1].split("=")

            source = packet.getSrc().split(".")
            dest = packet.getDst().split(".")
            #print source[2] + " , " + dest[2]

            # If the network is the same add 1
            if source[2] == dest[2]:
                numOfHops += 1#float( 128 - float(ttl[1]) + 1)
            # If the network is not the same add 3
            if source[2] != dest[2]:
                numOfHops += 3#float( 128 - float(ttl[1]) + 3)
            
    ave = float( numOfHops / count )
    print str(numOfHops) + " , " + str(ave)


    # TODO: Print out the metrics and calcuate the rest of them