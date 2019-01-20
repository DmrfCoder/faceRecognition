def dataTypeBase():
    bName = b"jack"
    # bName = b"jack测试" #报错，因为'测试'不是ascii字符，bytes类型不接受非ascii
    print(type(bName))
    print(bName)


def strTypeBase():
    strName = '''abc
    abc
    abc'''
    print(strName)


def delVariableBase():
    strName = 'name'
    print(strName)
    del strName
    print(strName)


def strMultiplyBase():
    strName = 'abc'
    print(strName)
    strName = strName * 3
    print(strName)


def strSubBase():
    strName = '12345678'
    print(strName[0::2])


def strModel():
    strContent = '姓名：%s,年龄：%d' % ('小明', 20)
    print(strContent)


def strConvertBase():
    strContent = '1223\t'
    print(strContent)
    strContent = r'1223\t'
    print(strContent)
    strContent = '1223\\t'
    print(strContent)


def strEncodeAndDecodeBase():
    strContent = '测试字符串'
    strEncode = strContent.encode('utf-8')
    print(type(strEncode))
    strDecode = strEncode.decode('utf-8')
    print(type(strDecode))


def fibonacci():
    fiboList = [0, 1]
    print('---for---')
    for i in range(1, 100):
        fiboList.append(fiboList[i] + fiboList[i - 1])
        if fiboList[-1] <= 100:
            print(fiboList[-1])
        else:
            break

    print('--while---')
    fiboListWhile = [0, 1]
    index = 1

    while (True):
        fiboListWhile.append(fiboListWhile[index] + fiboListWhile[index - 1])
        index += 1
        if (fiboListWhile[-1] <= 100):
            print(fiboListWhile[-1])
        else:
            break


def findAndINdex():
    strContent = '12345623'
    print(strContent.find('23'))
    print(strContent.index('23'))
    print(strContent.find('233'))
    print(strContent.index('233'))


import pythonTutorial.demo1 as demo1


def nameDemo():
    print(demo1.__name__)


def isinstanceFunc():
    strName = '测试字符串'
    print(isinstance(strName, str))
    a = 0
    print(isinstance(a, int))


def lambdaFunc():
    func = lambda x: x * x
    print(func(5))
    func2 = lambda x, y=3: x + y
    print(func2(10, 20))
    print(func2(10))

    func3 = lambda x, y: x + y if x > y else x * y
    print(func3(10, 20))


def listEnumerateFunc():
    listDemo = ['str1', 10, True, 3.14,[1,2,3]]
    print(listDemo)
    #替换前后的长度可以不一样
    listDemo[1:3]=[1,2,3,4,5]
    print(listDemo)

    for x,y in enumerate(listDemo):
        print(x,y)

def listCountFunc():
    listDemo=[1,2,3,4,1,2,4]
    print(listDemo.count(1))

def copyFunc():
    listDemo=[1,2,3,4,5]
    listDemo2=listDemo
    listDemo2[1]=1
    print(listDemo)
    listDemo3=listDemo.copy()
    listDemo3[1]=10
    print(listDemo)

def dictFunc():
    demoDic={'key1':12,'key2':122,'key3':1234}
    print(demoDic['key1'])
    print(demoDic.get('key1'))
    # print(demoDic['key11'])
    # print(demoDic.get('key11'))



if __name__ == '__main__':
    dictFunc()
