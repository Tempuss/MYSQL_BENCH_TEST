import dpkt

import datetime


def mac_addr(address):
    return ':'.join('%02x' % ord(b) for b in address)


with open('./test2.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)


    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
      
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue

        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue

        #print('Timestamp: '+ timestamp)

        #print ('Ethernet Frame: '+ mac_addr(eth.src)+ ' -> '+ mac_addr(eth.dst)+ eth.type)



