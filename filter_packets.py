from __future__ import print_function  # Get the real print function


def filter():
    for i in range(1, 5):
        filter_text_file("data/Node" + str(i) + ".txt")

def filter_text_file(filename):
    name, ext = filename.split(".")
    with open(name + "_filtered." + ext, 'w') as outfile:
        with open(filename) as fil:
            while True:
                # Process 1 packet
                data = fil.readline()  # Read the headers information
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

