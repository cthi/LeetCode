class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def isIPv4(addr):
            addrSplit = addr.split('.')

            if len(addrSplit) != 4:
                return False

            for section in addrSplit:
                try:
                    if len(section) == 0:
                        return False
                    elif (len(section) > 1 and section[0] == '0') or section[0] == '+' or section[0] == '-':
                        return False
                    elif not 0 <= int(section) <= 255:
                        return False
                except ValueError:
                    return False

            return True
    
        def isIPv6(addr):
            addrSplit = addr.split(':')

            if len(addrSplit) != 8:
                return False

            for section in addrSplit:
                try:
                    print(len(section))
                    print(section, 0 <= int(section, 16), int(section, 16) <= 65535)
                    if len(section) == 0 or len(section) > 4:
                        return False
                    elif section[0] == '+' or section[0] == '-':
                        return False
                    elif not 0 <= int(section, 16) <= 65535:
                        return False
                except ValueError:
                    return False

            return True
        
        if isIPv4(IP):
            return 'IPv4'
        elif isIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
