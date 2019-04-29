
def compute(*nodes):
    open('data/Output.csv', 'w').close()
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


    # TODO: Print out the metrics and calcuate the rest of them

    with open("data/Output.csv", 'a') as outfile:
        outfile.write("Node " + str(node) + "\n\n")
        outfile.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
        outfile.write(str(EchoRequestsSent) + "," + str(EchoRequestsRec) + "," + str(EchoReplySent) + "," + str(EchoReplyRec) + "\n")
        outfile.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        outfile.write(str(EchoRequestBytesSent) + "," + str(EchoRequestDataSent) + "\n")
        outfile.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        outfile.write(str(EchoRequestBytesRec) + "," + str(EchoRequestDataRec) + "\n\n")
        outfile.write("Average RTT (milliseconds)," + str(round(AveragePingRTT, 2)) + "\n")
        outfile.write("Echo Request Throughput (kB/sec)," + str(round(EchoRequestThroughput, 1)) + "\n")
        outfile.write("Echo Request Goodput (kB/sec)," + str(round(EchoRequestGoodput, 1)) + "\n")
        outfile.write("Average Reply Delay (microseconds)," + str(round(AverageReplyDelay, 2)) + "\n\n")

