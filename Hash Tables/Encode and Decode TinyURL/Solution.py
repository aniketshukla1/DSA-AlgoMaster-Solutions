class Codec:
    def __init__(self):
        self.encodedMap = {}
        self.decodedMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodedMap:
            short_url = self.base + str(len(self.encodedMap)+1)
            self.encodedMap[longUrl] = short_url
            self.decodedMap[short_url] = longUrl
        return self.encodedMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodedMap[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
