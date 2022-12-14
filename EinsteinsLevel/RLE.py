def run_length_encoding(a):
    """RLE"""
    a += '*'
    k = 1
    x = ''
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            k += 1
        else:
            x += str(k) + a[i]
            k = 1

    """Compression ratio"""
    I = 0
    for i in range(len(x)):
        if not x[i].isdigit():
            I += 1
    K = len(x) / (I * 2)
    return 'RLE:', x, 'Compression ratio:', K


print(run_length_encoding('ABBCCCDDDD'))


def de_rle(s):
    l = []
    xl = ''

    for i in range(0, len(s), 8):
        l.append(s[i:i + 8])
    l.append('00000000')

    for i in range(len(l) - 1):
        if l[i][0] == '1':
            xl += int(l[i][1:], 2) * chr((int(l[i + 1], 2)))
            l.pop(i + 1)

        if l[i][0] == '0':
            k = int(l[i][1:], 2)
            xl += str(int(l[i][1:], 2))
            for j in range(i + 1, k):
                xl += chr(int(l[i], 2))
    return xl


print(de_rle('1000111101000001000000100100001001000011'))
