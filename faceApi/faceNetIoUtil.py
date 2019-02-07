import json

import requests


def phaseJsonToDict(strJson):
    return json.loads(strJson)


def postRequest(url, request_body, timeout=5):
    """
    :param url:
    :param request_body:
    :param timeout:
    :return:
    """
    dictRequestResult = {}

    response = requests.post(url=url, data=request_body, timeout=timeout)

    if response.status_code == 200:
        dictRequestResult['bResult'] = True
        dictResponse = phaseJsonToDict(response.text)
        dictRequestResult['dictResponse'] = dictResponse

    else:
        dictRequestResult['bResult'] = False
        dictRequestResult['dictResponse'] = None

    return dictRequestResult
