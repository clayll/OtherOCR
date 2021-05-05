# -*- coding:UTF-8 -*-
# -*- encoding: utf-8 -*-
import base64
import requests


from urllib.parse import quote
API_KEY = 'r0vGh28MqUL0FBsGSbx3ecKH'
SECRET_KEY = 'ukZ2aXHNw0aL7UIxG6q9LXFQjl2fBrOg'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
access_token = "24.9657ca7a8987e6240e76b72e8bc6c07a.2592000.1621306957.282335-24014868"
response = requests.get(host)
if response:
    print(response.json())


headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'charset': "utf-8"
    }
if __name__ == '__main__':
    # 代码中所需的工具包requests
    # 安装方式:pip install requests
    # iocr识别api_url
    recognise_api_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise/finance"



    templateSign = "vat_invoice"
    detectorId = 0
    classifierId = "10001"
    # 测试数据路径
    image_path = "1.jpg"
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            image_b64 = base64.b64encode(image_data).decode().replace("\r", "")

            # 请求模板的bodys
            recognise_bodys = "access_token=" + access_token + "&templateSign=" + templateSign + \
                    "&image=" + quote(image_b64.encode("utf8"))
            # 请求分类器的bodys
            classifier_bodys = "access_token=" + access_token + "&classifierId=" + classifierId + \
                    "&image=" + quote(image_b64.encode("utf8"))
            # 请求模板识别
            response = requests.post(recognise_api_url, data=recognise_bodys, headers=headers)
            # 请求分类器识别
            # response = requests.post(recognise_api_url, data=classifier_bodys, headers=headers)
            print (response.text)
    except Exception as e:
        print (e)

def parseImg(image_path="1.jpg"):
    # 代码中所需的工具包requests
    # 安装方式:pip install requests
    # iocr识别api_url
    recognise_api_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise/finance"

    templateSign = "vat_invoice"
    detectorId = 0
    classifierId = "10001"
    # 测试数据路径
    # image_path = "1.jpg"

    print(type(image_path))

    if image_path == "1.jpg":
        try:
            with open(image_path, 'rb') as f:
                image_data = f.read()
                image_b64 = base64.b64encode(image_data).decode().replace("\r", "")


                # 请求模板的bodys
                recognise_bodys = "access_token=" + access_token + "&templateSign=" + templateSign + \
                                  "&image=" + quote(image_b64.encode("utf8"))
                # 请求分类器的bodys
                classifier_bodys = "access_token=" + access_token + "&classifierId=" + classifierId + \
                                   "&image=" + quote(image_b64.encode("utf8"))
                # 请求模板识别
                response = requests.post(recognise_api_url, data=recognise_bodys, headers=headers)
                # 请求分类器识别
                # response = requests.post(recognise_api_url, data=classifier_bodys, headers=headers)
                print(response.text)
                return  response.text
        except Exception as e:
            print(e)
            return e
    else:
        try:

            imgdata = base64.b64decode(image_path)  # 转换成图片对象

            image_b64 =  base64.b64encode(image_path).decode().replace("\r", "")

            # 请求模板的bodys
            recognise_bodys = "access_token=" + access_token + "&templateSign=" + templateSign + \
                              "&image=" + quote(image_b64.encode("utf8"))
            # 请求分类器的bodys
            classifier_bodys = "access_token=" + access_token + "&classifierId=" + classifierId + \
                               "&image=" + quote(image_b64.encode("utf8"))
            # 请求模板识别
            response = requests.post(recognise_api_url, data=recognise_bodys, headers=headers)
            # 请求分类器识别
            # response = requests.post(recognise_api_url, data=classifier_bodys, headers=headers)
            print(response.text)
            return response.text
        except Exception as e:
            print(e)
            return e