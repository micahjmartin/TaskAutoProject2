from __future__ import print_function

class Icmp(object):
	def __init__(self, data):
		data = data.strip().split()
		self.num = int(data[0]) # Num of packet
		self.time = float(data[1])
		self.src = data[2] # Source IP
		self.dst = data[3] # Dest IP
		self.length = int(data[5])
		self.info = " ".join(data[6:])
		print(self.__dict__)
	def __str__(self):
		return " ".join([str(self.num), str(self.time), self.src, self.dst, str(self.length), self.info])

def parse():
	data = "441 590.404752     192.168.100.1         192.168.100.2         ICMP     74     Echo (ping) request  id=0x0001, seq=91/23296, ttl=128 (reply in 442)"
	x = Icmp(data)
	print(x)

parse()
