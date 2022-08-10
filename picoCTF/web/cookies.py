import requests

url = "http://mercury.picoctf.net:21485/check"

for i in range(28):
    print(i)
    content = requests.get(url, cookies={"name":"{}".format(i)})
    if("CTF{" in content.text):
        print(content.text)
        break