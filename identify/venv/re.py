import requests
# res=requests.get("https://github.com/shuangxiangkan/learngit/blob/master/readme.txt")
# print(type(res))
# res.status_code=requests.codes.ok
# print(res.status_code)
# print(len(res.text))
# print(res.text[:250])

res=requests.get("localhost/D/python_work/identify")
res.raise_for_status()
playFile=open("RomeoAndJuliet.txt","wb")
for chunk in res.iter_content(1000000):
    playFile.write(chunk)

playFile.close()