# Task Auto. Project 2
# Paul Hulbert
# Jonathan Jang
# Micah Martin

class Icmp(object):
    def __init__(self, data):
        data = data.strip().split()
        self.num = int(data[0]) # Num of packet
        self.time = float(data[1])
        self.src = data[2] # Source IP
        self.dst = data[3] # Dest IP
        self.frame_size = int(data[5]) # Size of entire frame
        self.info = " ".join(data[6:]) # Random info
        # Get the time to live
        self.ttl = float([field.split("=")[-1] for field in data if "ttl=" in field][0])
        self.length = self.frame_size - 42 # Length of the ICMP data

        self._ips = {
            "192.168.100.1": 1,
            "192.168.100.2": 2,
            "192.168.200.1": 3,
            "192.168.200.2": 4
        }

    def isReply(self):
        return "Echo (ping) reply" in self.info
    
    def isRequest(self):
        return "Echo (ping) request" in self.info
    
    def getSrcNode(self):
        return self._ips.get(self.src, -1)
    
    def getDstNode(self):
        return self._ips.get(self.dst, -1)
    
    def __str__(self):
        return " ".join([str(self.num), str(self.time), self.src, self.dst, str(self.length), self.info])

def parse(node1, node2, node3, node4):
    """Get the packets for each of the nodes"""
    print("Parsing the files...")
    node1.extend(parse_text_file("data/Node1_filtered.txt"))
    node2.extend(parse_text_file("data/Node2_filtered.txt"))
    node3.extend(parse_text_file("data/Node3_filtered.txt"))
    node4.extend(parse_text_file("data/Node4_filtered.txt"))

def parse_text_file(filename):
    packets = []
    with open(filename) as fil:
        while True:
            # Process 1 packet
            data = fil.readline()  # Read the headers information
            if data.startswith("No."):
                packets += [Icmp(fil.readline())]
            if not data:
                break
    return packets
