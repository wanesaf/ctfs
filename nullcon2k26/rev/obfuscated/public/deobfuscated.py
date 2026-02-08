import base64

# --- f1: substitution table ---
F1 = {
    97:83, 98:117, 99:67, 100:98, 101:116, 102:36, 103:96, 104:64,
    105:49, 106:33, 107:72, 108:85, 109:69, 110:75, 111:119, 112:107,
    113:86, 114:78, 115:48, 116:99, 117:76, 118:61, 119:100, 120:125,
    121:113, 122:121, 65:106, 66:118, 67:58, 68:103, 69:65, 70:57,
    71:89, 72:91, 73:44, 74:59, 75:63, 76:115, 77:50, 78:51,
    79:77, 80:55, 81:101, 82:71, 83:92, 84:39, 85:46, 86:80,
    87:90, 88:79, 89:41, 90:108, 33:70, 34:62, 35:87, 36:120,
    37:40, 38:123, 39:34, 40:42, 41:68, 42:81, 43:109, 44:35,
    45:110, 46:37, 47:54, 58:97, 59:84, 60:112, 61:66, 62:114,
    63:122, 64:47, 91:53, 92:38, 93:56, 94:52, 95:74, 96:45,
    123:102, 124:126, 125:104, 126:43, 48:60, 49:124, 50:94,
    51:95, 52:88, 53:73, 54:105, 55:111, 56:82, 57:93
}

def f1(a):
    return F1.get(a, a)


# --- f3: substitution over string ---
def substitute(s):
    return ''.join(chr(f1(ord(c))) for c in s)


# --- f6: parity function ---
def f6(a):
    return 1 if a % 2 == 0 else 255  # 255 ≡ -1 mod 256


# --- f7: add g to every byte ---
def f7(arr, g):
    g %= 256
    return [(x + g) % 256 for x in arr]


# --- f8: rolling byte transform ---
def f8(arr):
    n = arr[:]  #copy of array
    m = arr[:]  #copy of array
    for l in range(len(m)):
        b = m[l]
        p = f6(b % 2)
        q = (l * p) % 256
        n = f7(n, q)
    return n


# --- f13: Base64 encoding (standard-compliant) ---
def f13(byte_arr):
    return base64.b64encode(bytes(byte_arr)).decode()


# --- f14: full pipeline ---
def challenge_final(s):
    step1 = substitute(s)
    step2 = [ord(c) for c in step1]
    step3 = f8(step2)
    return f13(step3)


# --- CLI behavior equivalent ---
if __name__ == "__main__":
    import sys
    line = sys.stdin.readline().rstrip("\n")
    print(challenge_final(line))

