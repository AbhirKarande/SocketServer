from socket import *
from dnsPacket import DNSPacket
from Utilities import Util
class DNSPacketModifier:

  

    def __init__(self, _file, _serverName, _DNS_UDP_PORT, _BUFFERSIZE):
        self.DNS_UDP_PORT = _DNS_UDP_PORT
        self.BUFFERSIZE = _BUFFERSIZE
        self.serverName = _serverName
        self.urlIPMap = self.parseFile(_file)
        self.socket_DNS_out = socket(AF_INET, SOCK_DGRAM)
        self.dnsCache = {}

        
         
    def parseFile(self, _file):
        """
            This function parsers the file. 
            This file currently only supports IPV4 address.
        """
        urlIPMap = {}
        lines = open(_file,'r').readlines()
        for line in  lines: 
            splitLine = line.split(' ')
            urlIPMap[splitLine[0]] = splitLine[1]
        return urlIPMap

    def modify(self, dnsPacket): 
        """
            This function is responsible for representing the modify module in the write
            It should take in a DNSPacket. Do a recursive query and get the result.
            If intercept.txt file contains the QNAME found it query it should replace the answer
            section with IPV4 address from the intercept file. 
            Finally it should cache the result and then check the cache before doing future recursive queries. 
        """
        #TODO: Student impment the modifier method