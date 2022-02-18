import httpx
a = {"username": "myuser", "password": "mypass"}
respones = httpx.post('http://127.0.0.1:8888/n', data=a)

print(respones.text)
