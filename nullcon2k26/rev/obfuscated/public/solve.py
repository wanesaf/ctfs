import base64

F1 = {97:83, 98:117, 99:67, 100:98, 101:116, 102:36, 103:96, 104:64, 105:49, 106:33, 107:72, 108:85, 109:69, 110:75, 111:119, 112:107, 113:86, 114:78, 115:48, 116:99, 117:76, 118:61, 119:100, 120:125, 121:113, 122:121, 65:106, 66:118, 67:58, 68:103, 69:65, 70:57, 71:89, 72:91, 73:44, 74:59, 75:63, 76:115, 77:50, 78:51, 79:77, 80:55, 81:101, 82:71, 83:92, 84:39, 85:46, 86:80, 87:90, 88:79, 89:41, 90:108, 33:70, 34:62, 35:87, 36:120, 37:40, 38:123, 39:34, 40:42, 41:68, 42:81, 43:109, 44:35, 45:110, 46:37, 47:54, 58:97, 59:84, 60:112, 61:66, 62:114, 63:122, 64:47, 91:53, 92:38, 93:56, 94:52, 95:74, 96:45, 123:102, 124:126, 125:104, 126:43, 48:60, 49:124, 50:94, 51:95, 52:88, 53:73, 54:105, 55:111, 56:82, 57:93}
INV_F1 = {v: k for k, v in F1.items()} # the inverse of substitution

def solve_correctly():
    encoded_b64 = "YnpYZVeGc45lc2VUZ05h"
    target_bytes = list(base64.b64decode(encoded_b64)) #step4
    length = len(target_bytes)

    trial_m = [0] * length
    
    total_q_sum = 0
    
    #we dont need to perform the reverse of inverse f8 we need to bruteforce 
    for potential_total_q in range(256):
        current_m = [(target_bytes[i] - potential_total_q) % 256 for i in range(length)]
        
        actual_q_sum = 0
        for l in range(length):
            p = 1 if current_m[l] % 2 == 0 else 255
            actual_q_sum = (actual_q_sum + (l * p)) % 256
            
        if actual_q_sum == potential_total_q:
            flag = "".join(chr(INV_F1.get(b, 63)) for b in current_m)
            return flag

    return "Could not solve xd "

print(f"Flag: {solve_correctly()}")
