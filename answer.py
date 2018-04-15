from lib.base64 import Base64


class Answer(object):
    def __init__(self):
        self._base64 = Base64()
        self.c4 = "ABCD"
        self.c_map = {self.c4[i]: i for i in range(4)}

    def encode(self, origin_answer):
        assert type(origin_answer) == str
        origin_answer = origin_answer.upper()
        c4_num_list = []

        for ch in origin_answer:
            if ch not in self.c4:
                raise ValueError("origin answer should be in %s, while %s not" % (self.c4 + self.c4.lower(), ch))
            else:
                c4_num_list.append(self.c_map[ch])
        # please ignore answer when you find more answer than you wanted
        while len(c4_num_list) % 3 != 0:
            c4_num_list.append(0)

        c64_num_list = [c4_num_list[i] * 16 + c4_num_list[i+1] * 4 + c4_num_list[i+2] for i in range(0,
                                                                                                     len(c4_num_list),
                                                                                                 3)]
        return ''.join([self._base64.encode(num) for num in c64_num_list])

    def decode(self, encode_answer):
        assert type(encode_answer) == str
        c4_num_list = []
        c64_num_list = [self._base64.decode(ch) for ch in encode_answer]
        for num in c64_num_list:
            c4_num_list.append(num / 16)
            num %= 16
            c4_num_list.append(num / 4)
            num %= 4
            c4_num_list.append(num)
        return ''.join([self.c4[num] for num in c4_num_list])


if __name__ == "__main__":
    answer = Answer()
    origin_answer = "ABADCBACBAADBAC"
    encode_answer = answer.encode(origin_answer)
    print("Encode answer for %s is %s" % (origin_answer, encode_answer))
    print("decode is %s" % answer.decode(encode_answer))

