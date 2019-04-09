from __future__ import print_function  # Get the real print function

def filter() :
	print('called filter function in filter_packets.py')
	
def filter_text_file(filename):
	name, ext = filename.split(".")
	with open(name + "_filtered." + ext, 'w') as outfile:
		with open(filename) as fil:
			while True:
				# Process 1 packet
				data = fil.readline() # Read the headers information
				headers = fil.readline()
				data += headers
				if not headers or not data:
					break
				protocol = headers.split()[4]
				data += fil.readline() # Read the blank line
				loop = True
				while loop:
					d = fil.readline()
					if d.strip() != "":
						data += d
					else:
						break
				if protocol == "ICMP":
					outfile.write(data+"\n")

filter_text_file("data/Node1.txt")
