import re
import itertools

reg= re.compile("[0-9a-zA-Z_@!?-]")

enc = list(map(ord,'¢×&Ê´cÊ¯¬$¶³´}ÍÈ´T©Ð8Í³Í|Ô÷aÈÐÝ&¨þJ'))


sols = []

# try all solution of 4 with 255 chars
flagxor=[[253,149,21,249],[253,153,21,249]]

for [k1,k2,k3,k4] in flagxor:
    s = [k1,k2,k3,k4]
    res = ""
    for j in range(len(enc)):
        res += chr(enc[j] ^ s[j%4])
    if(reg.match(res)):
        sols.append(res)


print(sols)
# 
# ➜ attachments python solver.py
# ['_B3x7!v3R91ON!h45!AnTE-4NXi-abt1-H3bUk_', '_N3x7-v3R51ON-h45-AnTI-4NTi-ant1-D3bUg_']

# 