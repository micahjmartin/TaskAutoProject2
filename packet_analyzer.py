#!/usr/bin/env python

# Task Auto. Project 2
# Paul Hulbert
# Jonathan Jang
# Micah Martin

from filter_packets import filter
from packet_parser import parse
from compute_metrics import compute


# Filter the packets located in the "data/" directory
filter("data")

# Build arrays for each node
node1 = []
node2 = []
node3 = []
node4 = []

# Parse the data
parse(node1, node2, node3, node4)

# Compute the nodes
compute(node1, node2, node3, node4)

print("Output saved to output.csv")