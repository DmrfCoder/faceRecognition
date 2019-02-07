from config import faceConfig
from faceNetIoUtil import *


def detectPictureFromFaceApi(base64Pic):
    """

    curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F "api_key=<api_key>" \
    -F "api_secret=<api_secret>" \
    -F "image_file=@image_file.jpg" \
    -F "return_landmark=1" \
    -F "return_attributes=gender,age"

    :param base64Pic: Pending analysis picture which be encoded by base64
    :return:
    jsonResponse:
        dictRequestResult:  dictionary  object,keys:
                                                - bResult:success or failure
                                                - dictResponse: If the success returns response,else None
    """
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    api_key = faceConfig.api_key
    api_secret = faceConfig.api_secret
    return_attributes = 'gender,age,glass,eyestatus,emotion,ethnicity,beauty,skinstatus'
    return_landmark = 0

    request_body = {}
    request_body['api_key'] = api_key
    request_body['api_secret'] = api_secret
    request_body['return_attributes'] = return_attributes

    request_body['image_base64'] = base64Pic
    request_body['return_landmark'] = return_landmark

    return postRequest(url, request_body)


def creatFaceSetInFaceApi():
    """
    curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/faceset/create" \
    -F "api_key=<api_key>" \
    -F "api_secret=<api_secret>" \
    -F "outer_id=newfaceset" \
    -F "tag=person,male" \
    -F "face_tokens=c2fc0ad7c8da3af5a34b9c70ff764da0,ad248a809408b6320485ab4de13fe6a9"
    :return:
    """
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    api_key = faceConfig.api_key
    api_secret = faceConfig.api_secret
    display_name = faceConfig.display_name
    request_body = {}
    request_body['api_key'] = api_key
    request_body['api_secret'] = api_secret
    request_body['display_name'] = display_name
    return postRequest(url, request_body)


def addFaceToFaceSet(faceSetToken, face_tokens):
    """
    将face_tokens添加到faceSetToken中，将face_tokens添加到faceSetToken最多有5个face_token，以，间隔
    :param faceSetToken:
    :param face_tokens:
    :return:
    """
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    request_body = {}
    request_body['api_key'] = faceConfig.api_key
    request_body['api_secret'] = faceConfig.api_secret
    request_body['faceset_token'] = faceSetToken
    request_body['face_tokens'] = face_tokens
    return postRequest(url, request_body)


def searchTargetPictureInFaceSet(faceSetToken, imageBase64):
    """

    :param faceSetToken:
    :param imageBase64:
    :return:
    """
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    request_body = {}
    request_body['api_key'] = faceConfig.api_key
    request_body['api_secret'] = faceConfig.api_secret
    request_body['faceset_token'] = faceSetToken
    request_body['image_base64'] = imageBase64

    return postRequest(url, request_body)
