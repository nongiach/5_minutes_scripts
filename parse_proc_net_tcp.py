#!/usr/bin/python3

import sys
import re
import socket
import struct

def hex_to_ip(raw_ip):
    return socket.inet_ntoa(struct.pack("<L", int(raw_ip, 16)))

def parse_proc_net_status(filename):
    with open(filename) as F:
        next(F)

        values = "sl local_address local_port rem_address rem_port st tx_queue rx_queue tr tm_when retrnsmt uid timeout inode".split(' ')
        print(('{:>12} ' * len(values)).format(*values))
        for line in F:
            line = line.replace(':', ' ')
            line = re.sub(r'\s+', ' ', line)
            line = line.strip()
            line = line.split(' ')

            sl,local_address,local_port,rem_address,rem_port,st,tx_queue,rx_queue,tr,tm_when,retrnsmt,uid,timeout,inode,*other = line
            local_address = hex_to_ip(local_address)
            local_port = int(local_port, 16)
            rem_address = hex_to_ip(rem_address)
            rem_port = int(rem_port, 16)
            values = (sl,local_address,local_port,rem_address,rem_port,st,tx_queue,rx_queue,tr,tm_when,retrnsmt,uid,timeout,inode)
            print(('{:>12} ' * len(values)).format(*values))
            # print(sl,local_address,local_port,rem_address,rem_port,st,tx_queue,rx_queue,tr,tm_when,retrnsmt,uid,timeout,inode, sep='\t')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage %s [filename" % sys.argv[0])
    else:
        parse_proc_net_status(sys.argv[1])
