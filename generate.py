
query = 'INSERT INTO basic_info (dump_id, datetime, src_ip, dst_ip, proto, src_port, dst_port, tcp_flags, http, dns, src_city, src_long, src_lat, icmp_type) VALUES'


f = open("./insert.sql",'w')
f.write(query)
max = 1300000
for data in range(max):
    print(str(data+1) + "/"+str(max))
    tmp_query = '('+str(data+1)+', FROM_UNIXTIME(1596775145), "119.119.119.119", "120.120.120.120", "HTTP", 80, 80, 1, "TESTHTTPHTTPHTTP", "DNSTEST", "SEOUL", 1515.255, 11.22, 55),'
    if data == max-1: 
        tmp_query = '('+str(data+1)+', FROM_UNIXTIME(1596775145), "119.119.119.119", "120.120.120.120", "HTTP", 80, 80, 1, "TESTHTTPHTTPHTTP", "DNSTEST", "SEOUL", 1515.255, 11.22, 55)'
        
    f.write(tmp_query)


query = query[:-1]
f.close()