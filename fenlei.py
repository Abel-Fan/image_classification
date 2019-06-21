import base64,json
import os.path
import requests,shutil

#获取 access_token
URL = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=FRwikKWeI1ED9dKFQDdncbYi&client_secret=yiHzcCDIasPDkdeiG3XBKr6it3igoVWI&'

res = requests.get(URL,headers={'Content-Type':'application/json; charset=UTF-8'})
access_token = res.json()['access_token']

# 请求算法

request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/uek_classify_catDog' + "?access_token=" + access_token

def myrequest(data,img):


    res = requests.post(request_url,data=json.dumps({'image':data})).json()
    print(res)
    if res['results']:
        if res['results'][0]['name'] =='dog':

            shutil.move(img,BASE_DIR+"\\res\\dog\\"+os.path.split(img)[1])
        else:
            shutil.move(img, BASE_DIR + "\\res\\cat\\" + os.path.split(img)[1])



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


imgFileNames = os.listdir("catDog")

for item in imgFileNames:
    img = BASE_DIR+r"\\catDog\\"+item
    with open(img,"rb") as f:
        data = base64.b64encode(f.read()).decode()
    myrequest(data,img)

