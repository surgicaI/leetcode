# https://leetcode.com/problems/encode-and-decode-tinyurl/#/description
class Codec:
    def __init__(self):
        self.hash = {}
        self.shortUrl = [0]

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        alphs = 'abcdefghijklmnopqurstuvwxyz'
        alphs += alphs.upper() + '0123456789'
        index = 0
        if index < len(alphs):
            self.shortUrl[-1] = alphs[index]
            index += 1
        else:
            index = 1
            self.shortUrl.append(alphs[0])
        
        result = ''.join(self.shortUrl)
        self.hash[result] = longUrl
        return result

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.hash[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))