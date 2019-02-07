import json

import requests
import base64

from config import faceConfig
from faceApiUtil import *


def phaseFaceTokenFromDectectResponseDict(dictTemp):
    print(dictTemp)
    faces = dictTemp['faces'][0]
    face_token = faces['face_token']
    print(face_token)
    return face_token


def detectPicture(picturePath):
    """
    :param picturePath: path of picture
    :return: face_token
    """
    base64Picture = ''
    try:
        with open(picturePath, mode='rb') as picFile:
            base64Picture = base64.b64encode(picFile.read())
    except FileNotFoundError:
        print('file not found')

    dictRequestResult = detectPictureFromFaceApi(base64Picture)
    if dictRequestResult['bResult']:
        return phaseFaceTokenFromDectectResponseDict(dictRequestResult['dictResponse'])
    else:
        return None



if __name__ == '__main__':
    picPath = '../resource/demoPic.jpg'

    creatReault = creatFaceSetInFaceApi()
    print(creatReault)
