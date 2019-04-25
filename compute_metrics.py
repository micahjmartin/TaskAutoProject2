
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

    # TODO: Print out the metrics and calcuate the rest of them