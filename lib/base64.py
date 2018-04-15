import string


class Base64(object):
    def __init__(self):
        self.c64 = '*' + string.ascii_lowercase + string.ascii_uppercase + string.digits[1:] + '0' + '#'
        self.c_map = {self.c64[i]: i for i in range(64)}

    def encode(self, num):
        assert num < 64
        assert num >= 0
        assert type(num) == int
        return self.c64[num]

    def decode(self, ch):
        assert ch in self.c64
        assert len(ch) == 1
        return self.c_map[ch]


if __name__ == '__main__':
    base64 = Base64()
    print(base64.encode(26))
