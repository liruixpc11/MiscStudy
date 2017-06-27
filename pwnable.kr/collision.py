import struct

hash_code = 0x21dd09ec

def custom_hash(s):
    if len(s) != 20:
        raise Exception()

    n = 0
    for i in range(5):
        n0 = struct.unpack('<I', s[i * 4:i * 4 + 4])[0]
        print hex(n0)
        n += n0
        print hex(n)
        print

    return n & 0xffffffff


if __name__ == '__main__':
    s = '/4,9' * 4 + '09,='
    print s
    print hex(custom_hash(s))
