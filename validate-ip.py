# https://leetcode.com/problems/validate-ip-address/#/description
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            IP = IP.split('.')
            if len(IP) != 4:
                return 'Neither'
            for ip in IP:
                if ip.find('-')!=-1 or ip.find('+')!=-1:
                    return 'Neither'
                if ip.find('0')==0 and len(ip)>1:
                    return 'Neither'
                try:
                    ip = int(ip)
                except ValueError:
                    return 'Neither'
                if ip>255 or ip<0:
                    return 'Neither'
                
            return 'IPv4'
        elif ':' in IP:
            IP = IP.split(':')
            if len(IP) != 8:
                return 'Neither'
            for ip in IP:
                if len(ip) > 4 or ip.find('-')!=-1 or ip.find('+')!=-1:
                    return 'Neither'
                try:
                    int(ip,16)
                except ValueError:
                    return 'Neither'
                
            return 'IPv6'
        else:
            return 'Neither'