
DNS_ALL = '''
+--+--+--+--+--+--+--+
|       Header       |
+--+--+--+--+--+--+--+
|      Question      |
+--+--+--+--+--+--+--+
|       Answer       |
+--+--+--+--+--+--+--+
|      Authority     |
+--+--+--+--+--+--+--+
|     Additional     |
+--+--+--+--+--+--+--+
'''

DNS_HEADER = '''
Header 报文头
  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |                 TransactionID                 |
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |QR|  opcode   |AA|TC|RD|RA|   Z    |   RCODE   |   # flags
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |                    QDCOUNT                    |
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |                    ANCOUNT                    |
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |                    NSCOUNT                    |
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
  |                    ARCOUNT                    |
  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
'''
'''-----------------------------------------------------------------------------------------------'''
DNS_HEADER_REQUEST = '''
DNS 请求报文示例：
Transaction ID: 0x9ad0                              #事务ID
Flags: 0x0000 Standard query                        #报文中的标志字段
    0... .... .... .... = Response: Message is a query
                                                    #QR标识该数据包为请求还是响应，0为请求，1为响应
    .000 0... .... .... = Opcode: Standard query (0)
                                                    #Opcode字段, 操作码，用于请求消息中，指示要执行的操作类型
                                                    0 正常查询，4 DNS Notify，5 DNS Update
    .... ..0. .... .... = Truncated: Message is not truncated
                                                    #TC字段
    .... ...0 .... .... = Recursion desired: Don't do query recursively 
                                                    #RD字段
    .... .... .0.. .... = Z: reserved (0)           #保留字段, 值为0
    .... .... ...0 .... = Non-authenticated data: Unacceptable   
                                                    #保留字段, 值为0
Questions: 1                                        #问题计数, 这里有1个问题
Answer RRs: 0                                       #回答资源记录数
Authority RRs: 0                                    #权威名称服务器计数
Additional RRs: 0                                   #附加资源记录数
'''
'''-----------------------------------------------------------------------------------------------'''
DNS_HEADER_RESPONSE = '''
DNS 响应报文示例：
Transaction ID: 0x9ad0                          #(16bit) 事务ID
Flags: 0x0000 Standard query                    #(16bit)  报文中的标志字段

    1... .... .... .... = (1bit)Response: Message is a query
                                                    # QR，标识该数据包为请求还是响应，0为请求，1为响应
    .000 0... .... .... = (4bit)Opcode: Standard query (0)
                                                    # Opcode字段, 操作码，用于请求消息中，指示要执行的操作类型
                                                    # 0 正常查询，4 DNS Notify，5 DNS Update
    .... .0.. .... .... = (1bit)Authoritative: Server is not an authority for domain
                                                    # AA字段，用于响应消息中，指示该响应是否权威
    .... ..0. .... .... = (1bit)Truncated: Message is not truncated
                                                    # TC字段，标识本条消息是否因过长而被截断
    .... ...1 .... .... = (1bit)Recursion desired: Do query recursively 
                                                    # RD字段，用于请求消息中，指示被查询的服务器是否应该执行递归查询
    .... .... 1... .... = (1bit)Recursion available: Server can do recursive queries
                                                    # RA字段, 用于响应消息中，指示被查询的服务器是否支持递归查询
    .... .... .0.. .... = (1bit)Z: reserved (0)           # Z字段,保留字段, 值为0
    .... .... ..0. .... = (1bit)Answer authenticated: Answer/authority portion was net authenticated by the server
                                                    # AD字段,保留字段, 值为0
    .... .... ...0 .... = (1bit)Non-authenticated data: Unacceptable
                                                    # CD字段,保留字段, 值为0
    .... .... .... 0000 = (4bit)RCode: No error           # 响应码，用于响应消息中
                                                    # 0 NoError，无错误；1 FormErr，格式错误；2 ServFail，服务器失效；
                                                    # 3 NXDomain，域名不存在；4 NotImp，未实现；5 Refused，查询被拒绝；

Questions: 1                                        #(16bit) 问题计数, 这里有1个问题
Answer RRs: 0                                       #(16bit) 回答资源记录数
Authority RRs: 0                                    #(16bit) 权威名称服务器计数
Additional RRs: 0                                   #(16bit) 附加资源记录数
'''
'''-----------------------------------------------------------------------------------------------'''
DNS_QUESTION = '''
Question 查询字段
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    ......                     |
|                    Q_name                     |
|                    Q_name                     |
|                    Q_name                     |
|                    Q_name                     |
|                    ......                     |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    Q_type                     |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    Q_class                    |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
Q_name: 无符号8bit为单位长度不限表示查询名(广泛的说就是：域名)
Q_type: 无符号16bit整数表示查询的协议类型.
Q_class: 无符号16bit整数表示查询的类,比如，IN代表Internet.
'''
'''-----------------------------------------------------------------------------------------------'''
DNS_3A = '''
Answer/Authority/Additional (这3个字段的格式都是一样的。)
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    NAME                       |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    TYPE                       |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    CLASS                      |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    TTL                        |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    RDLENGTH                   |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|                    RDATA                      |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

NAME 资源记录包含的域名.
TYPE 表示DNS协议的类型.
CLASS 表示RDATA的类.
TTL 4字节无符号整数表示资源记录可以缓存的时间。0代表只能被传输，但是不能被缓存。
RDLENGTH 2个字节无符号整数表示RDATA的长度
RDATA 不定长字符串来表示记录，格式根TYPE和CLASS有关。比如，TYPE是A，CLASS 是 IN，那么RDATA就是一个4个字节的ARPA网络地址。
'''


'''
TYPE	值	含义	备注
A	1	a host address/主机地址	
NS	2	an authoritative name server/权威名称服务器	
MD	3	a mail destination/邮件目的地	被废弃，使用 MX
MF	4	a mail forwarder/邮件转发器	被废弃，使用 MX
CNAME	5	the canonical name for an alias/别名的正则名称	
SOA	6	a marks the start of a zone of authority/标记权威区域的开始	
MB	7	a mailbox domain name/邮箱域名	EXPERIMENTAL
MG	8	a mail group member/邮件组成员	EXPERIMENTAL
MR	9	a mail rename domain name/邮件重新命名域名	EXPERIMENTAL
NULL	10	a null RR	EXPERIMENTAL
WKS	11	a well known service description/众所周知的服务描述	
PTR	12	a domain name pointer/域名指针	
HINFO	13	host information/主机信息	
MINFO	14	mailbox or mail list information/邮箱或邮件列表信息	
MX	15	mail exchange/邮件交换	
TXT	16	text strings/文本字符串	
SRV	33	service and protocol/服务和协议	在rfc2052中引入
'''
