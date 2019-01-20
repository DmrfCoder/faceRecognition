import json

import requests
import base64

import matplotlib.pyplot as plt
from PIL import Image

'''
curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F "api_key=<api_key>" \
-F "api_secret=<api_secret>" \
-F "image_file=@image_file.jpg" \
-F "return_landmark=1" \
-F "return_attributes=gender,age"
'''


def postPictureToFaceApi(base64Pic):
    """

    :param base64Pic: Pending analysis picture which be encoded by base64
    :return:
    jsonResponse:
        dictRequestResult:  dictionary  object,keys:
                                                - bResult:success or failure
                                                - dictResponse: If the success returns response,else None
    """
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    api_key = 'MPr17J0T8rgCBOzMMhw89OYZJ3GYMGvO'
    api_secret = 'E3T0MbYO4RuApJNMC6-ytEaOlYN37AfU'
    return_attributes = 'gender,age,glass,eyestatus,emotion,ethnicity,beauty,skinstatus'
    return_landmark = 0

    request_body = {}
    request_body['api_key'] = api_key
    request_body['api_secret'] = api_secret
    request_body['return_attributes'] = return_attributes

    request_body['image_base64'] = base64Pic
    request_body['return_landmark'] = return_landmark
    dictRequestResult = {}

    response = requests.post(url=url, data=request_body, timeout=5)

    if response.status_code == 200:
        dictRequestResult['bResult'] = True
        dictResponse = phaseJsonToDict(response.text)
        dictRequestResult['dictResponse'] = dictResponse

    else:
        dictRequestResult['bResult'] = False
        dictRequestResult['dictResponse'] = None

    return dictRequestResult


def phaseDictOfResponse(dictTemp):
    print(dictTemp)

    return None


def phaseJsonToDict(strJson):
    return json.loads(strJson)


if __name__ == '__main__':
    base64Picture = ''
    picPath = '../resource/demoPic.jpg'

    img = Image.open(picPath)
    plt.imshow(img)
    plt.show()

    try:
        with open(picPath, mode='rb') as picFile:
            base64Picture = base64.b64encode(picFile.read())
    except FileNotFoundError:
        print('file not found')

    dictRequestResult = postPictureToFaceApi(base64Picture)
    if dictRequestResult['bResult']:
        phaseDictOfResponse(dictRequestResult['dictResponse'])
