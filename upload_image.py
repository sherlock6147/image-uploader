URL = "https://api.imgbb.com/1/upload"
import requests
import base64
import secret

def upload_and_get_url(img_path)->str:
    with open(img_path,"rb") as file:
        payload = {
            "key" : secret.KEY,
            "image" : base64.b64encode(file.read())
        }
        response = requests.post(URL,payload)
        response = response.json()
        data = response.get('data')
        if 'url' in data:
            return data.get('url')
        else:
            return "None"

print("Url for the image is: "+upload_and_get_url("bck.jpg"))
print("Url for the image is: "+upload_and_get_url("pexels-andrea-piacquadio-3778928.jpg"))