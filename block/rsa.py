class RSA:
    def __init__(self):
        pass

    def make_public(self, e, n):
        self.e = e
        self.n = n
    
    def make_private(self, p, q):
        n = p * q
        phi = (p-1) * (q-1)


    def encrypt(self, msg):
        try:
            data = m.decode()
        except AttributeError:
            raise AttributeError("A byte-like object is required")
        
        m = int.from_bytes(msg)
        return pow(m, self.e, self.n)
    
