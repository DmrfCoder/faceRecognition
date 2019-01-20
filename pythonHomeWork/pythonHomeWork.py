from collections import Counter

"""
1.在代码中将如下信息备注到py文件中

abcdefghijklmn
opqrstuvwxyz
这是一段注释
可以换行的注释
"""
'''
abcdefghijklmn
opqrstuvwxyz
'''


def variableFunc():
    """
    1.将自己的”姓名”、”专业”、”学号”、”年龄”、”是否是新生”保存到自定义变量中，
    并打印在一句话中，，注意需要使用字符串格式化输出。
    :return:
    """
    strName = '薛方岗'
    strMaster = '软件工程'
    iAge = 22
    bIsNewStudent = False
    print('I\'m %s,my master is %s,I\'m %d years old,I\'m %s a new Student' % (strName, strMaster, iAge, bIsNewStudent))


def operatorFunc():
    """
    1.代码计算  10加20减5乘4除10
    2.代码计算忽略小数部分  100乘20除33
    3.代码计算  3.14乘3.14
    4.代码计算 求100除3的余数
    5.将前一题，第四题的结果作为6的多少次幂计算得到最终结果
    6.打印一行字符串，内容为20个”abc”
    7.有一个变量a等于100，将a的值加100后的结果再次保存到变量a中
    8.代码计算第一题的结果是否大于第二题的结果
    如果分数小于30分输出”你咋学习这么不认真的呢？”，如果分数在31分和59分之间输出
    ”你需要再在努力一下”，只要成绩大于60分输出”你的成绩是多少分，成绩及格”，
    如果成绩在60到80之间再输出”你再努力一点就是学霸”，
    如果成绩在81到90再输出”学霸你好”,如果成绩大于90再输出”哇，学神，抱大腿”
    :return:
    """
    fV1 = ((10 + 20) * 5 * 4) / 10
    iV2 = int(100 * 20) / 33
    fV3 = 3.14 ** 3.14
    iV4 = 100 % 3
    fV5 = pow(6, iV4)
    sV6 = 'abc' * 20
    print(sV6)
    bV7 = fV1 >= iV2
    strV8 = '你咋学习这么不认真的呢？'
    iScore = 100
    if 31 <= iScore <= 59:
        strV8 = '你需要再在努力一下'
    elif iScore > 60:
        strV8 = '你的成绩是%d分，成绩及格' % (iScore)

    if 60 <= iScore <= 80:
        strV8 += '\n你再努力一点就是学霸'
    elif 81 <= iScore <= 90:
        strV8 += '\n学霸你好'
    else:
        strV8 += '\n哇，学神，抱大腿'

    print(fV1)
    print(iV2)
    print(fV3)
    print(iV4)
    print(fV5)
    print(bV7)
    print(sV6)
    print(strV8)


def sumMultipleOfThree():
    """
    累加1到100之间，求所有3的倍数相加后的和
    :return:
    """
    bFlag = False
    iSum = 0
    iIndex = 1

    while (iIndex <= 100):
        if bFlag:
            print(iIndex)
            iSum += iIndex
            iIndex += 3

        elif iIndex % 3 == 0:
            print(iIndex)
            iSum += iIndex
            bFlag = True
            iIndex += 3
        else:
            iIndex += 1

    print(iSum)


def printMultiplicationTable():
    """
     打印九九乘法表
    :return:
    """
    for iRowIndex in range(1, 10):
        for iColumnIndex in range(1, iRowIndex + 1):
            print('%d x %d = %d' % (iColumnIndex, iRowIndex, iRowIndex * iColumnIndex), end=' ')
        print()


def printTriangle():
    """
    打印如下直角三角形
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    :return:
    """
    for i in range(1, 9):
        print('*' * i)


def printRightAngle():
    """
    打印如下直角三角形
    **
    ****
    ******
    ********
    **********
    ************
    **************
    ****************
    ******************
    :return:
    """
    for i in range(1, 9):
        print('*' * 2 * i)


def printHelloWorld():
    """
    有一个字符串”HelloWorld”按如下格式打印，每行打印一个字符，（提示：while）
    H
    e
    l
    l
    o
    W
    o
    r
    l
    d
    :return:
    """
    sHello = 'HelloWorld'

    for c in sHello:
        print(c)


def sub345FromStr():
    """
    截取字符串”12345678”中的”345”
    :return:
    """
    sNumbers = '12345678'
    print(sNumbers[2:5])


def searchTargetStrs():
    """
    检索如下字符串,是否包含密码password，如果包含，则截取password对应的密码。
    :return:
    """
    sTemp = 'userName:123456,password:abcdef,email:12345678@qq.com,phoneNumber:13112345678'
    if sTemp.find('password') != -1:
        index = sTemp.index('password')
        index2 = sTemp[index:].find(",") + index
        listSplit = sTemp[index:index2].split(":")
        return listSplit[1]


def replaceTargetStrs():
    """
    将如下字符串中”username”替换为”用户名”，”password”替换为”密码”,”email”替换为”邮箱”，”phoneNumber”替换为”电话号码”，并将最终字符串打印
    ”userName:123456,password:abcdef,email:12345678@qq.com,phoneNumber:13112345678”
    :return:
    """
    sTemp = 'userName:123456,password:abcdef,email:12345678@qq.com,phoneNumber:13112345678'
    sTemp = sTemp.replace('userName', '用户名')
    sTemp = sTemp.replace('password', '密码')
    sTemp = sTemp.replace('email', '邮箱')
    sTemp = sTemp.replace('phoneNumber', '电话号码')
    print(sTemp)


def cycleDemo():
    """
    #for和while分别实现打印如下内容
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    :return:
    """
    print('---for---')
    for i in range(10, 0, -1):
        print('*' * i)

    print('---while---')
    iIndex = 10
    while (iIndex >= 1):
        print('*' * iIndex)
        iIndex -= 1


def listDemo1():
    """
    创建一个列表，列表元素为：'one','two','three','four','five'。并打印下标为3的元素

    """
    listTemp = ['one', 'two', 'three', 'four', 'five']
    print(listTemp[3])

    """
    创建两个列表，第一个列表元素为：1,2,3,4,5。第二个列表元素为：'a','b','c','d','e'。拼接上题中创建的列表和本题中的两个列表，生成新的列表。
    最终元素内容为：'one','two','three','four','five',1,2,3,4,5,'a','b','c','d','e'。
    """
    listTemp1 = [1, 2, 3, 4, 6]
    listTemp2 = ['a', 'b', 'c', 'd', 'e']
    listTemp += listTemp1
    listTemp += listTemp2
    print(listTemp)

    """
    打印上题新列表的元素个数，修改列表下标为7的元素，改为'new',并打印结果。修改列表中第4到第7的元素为：'aaa','bbb','ccc',并打印结果。
    删除下标为9的元素，并打印结果。删除第3到第5个元素，并打印结果。
    
    """
    listTemp[7] = 'new'
    print(listTemp)
    listTemp[3:6] = ['aaa', 'bbb', 'ccc']
    print(listTemp)
    del listTemp[9]
    print(listTemp)
    del listTemp[2:5]
    print(listTemp)
    """
    将新元素'new_one'追加到上题列表的尾部，并打印结果。
    将新元素'new_two'插入到第3个元素和第4个元素中间，并打印结果。
    将整个列表逆序排列，并打印结果。
    """

    listTemp.append('new_one')
    print(listTemp)
    listTemp.insert(3, 'new_two')
    print(listTemp)
    """
    创建一个字符串myStr = "one,two,three,four,five,six,seven",
    将字符串分割，最后保存到一个列表中，列表元素为：'one','two','three','four','five','six','seven'，并打印结果
    """
    myStr = "one,two,three,four,five,six,seven"
    myStrList = myStr.split(',')
    print(myStrList)


def tupleDemo1():
    """
    新建一个元组，元素内容为:'a1','b2','c3','d4','e5','f6'，打印元组长度。
    遍历元素，每行打印一个元素，要求打印结果如下所示：
    a1
    b2
    c3
    d4
    e5
    f6
    :return:
    """
    tupleTemp = ('a1', 'b2', 'c3', 'd4', 'e5', 'f6')
    for itemTuple in tupleTemp:
        print(itemTuple)

    """
    简述元组与列表的区别
    """
    '''
    数组初始化以后允许二次对其进行修改，元组初始化后不允许二次改写内容    
    '''


def tupleDemo2():
    """
    for循环打印第1项到第100项的斐波那契数列，并保存到一个元组中。
    斐波那契数列：1、1、2、3、5、8、13、21、34...,前两个元素都为1，后一个元素为前两个元素的和。

    :return:
    """
    tupleTemp = (1, 1)
    for i in range(3, 101):
        iTemp = tupleTemp[i - 2] + tupleTemp[i - 3]
        newTuple = (iTemp,)
        tupleTemp = tupleTemp + newTuple

    print(tupleTemp)


def dictDemo1():
    """
    将如下信息,保存为一个字典
    "userName:123abc,password:abcdef,email:12345678@qq.com,phoneNumber:13112345678"
    打印所有key。打印所有value。两种方式打印userName的值。修改key为password的值，将字符改为大写，替换原来的值。
    :return:
    """
    dictTemp = {'userName': '123abc', 'password': 'abcdef', 'email': '12345678@qq.com', 'phoneNumber': '13112345678'}
    print('keys:')
    print(dictTemp.keys())
    print('values')
    print(dictTemp.values())
    print('方式1打印userName：')
    print(dictTemp['userName'])
    print('方式2打印userName：')
    print(dictTemp.get('userName'))
    dictTemp['password'] = dictTemp['password'].upper()
    print(dictTemp)


def dictDemo2():
    """
    新建两个元组，一个元组内的元素为：1,2,3,4,5,6,7,8,9。一个元组内的元素为：aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii。
    将两个元组的内容合并到一个字典中，最终字典内容为：1:aaa,2:bbb,...,9:iii，并打印。删除字典中的key为5的键和值。
    循环遍历此字典，将key小于等于5的保存到一个新字典中，将key大于5的保存到另一个新字典中。

    :return:
    """
    tupleTemp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tupleTemp2 = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii']
    dictTemp = {}
    for key, value in zip(tupleTemp1, tupleTemp2):
        dictTemp[key] = value

    print(dictTemp)
    del dictTemp[5]
    print(dictTemp)
    dictNew1 = {}
    dictNew2 = {}
    for key, value in dictTemp.items():
        if key <= 5:
            dictNew1[key] = value
        else:
            dictNew2[key] = value

    print(dictNew1)
    print(dictNew2)


def dictDemo3():
    """
    新建一个空字典，依次追加如下内容：
    "姓名"对应的值"张三"
    "学号"对应值123
    "我的数字列表"对应的值为一个元组(10,20,30,40,50,60,70,80,90)
    "我的爱好"对应的值为一个列表["唱歌","跳舞","看书","游泳","打球"]
    #修改"我的爱好"对应的值，将"跳舞"删除掉，并保存打印。
    #修改"我的数字列表"对应的值，去掉小于等于30的数字，并保存打印。
    :return:
    """
    dictTemp = {'姓名': '张三', '学号': 123, '我的数字列表': (10, 20, 30, 40, 50, 60, 70, 80, 90),
                '我的爱好': ["唱歌", "跳舞", "看书", "游泳", "打球"], }
    print(dictTemp)
    listLove = dictTemp['我的爱好']
    listLove.remove('跳舞')
    dictTemp['我的爱好'] = listLove
    print(dictTemp)
    tupleNumber = dictTemp['我的数字列表']

    newTuple = ()
    for itemNumber in tupleNumber:
        if itemNumber > 30:
            tempTuple = (itemNumber,)
            newTuple += tempTuple

    dictTemp['我的数字列表'] = newTuple
    print(dictTemp)


def functionDemo1(strTemp):
    """
    写一个函数，实现功能为传入一个字符串，将字符全部转换为大写，并且倒序排列后返回字符串。

    :return:
    """
    strTemp = strTemp.upper()
    listTemp = list(strTemp)

    return "".join(reversed(listTemp))


def functionDemo2(listTemp):
    """
    写一个函数，实现功能为传入一个元素都为数字的列表，
    将列表中小于10，大于100的数字去掉，返回修改后的列表。
    :return:
    """
    return [i for i in listTemp if 10 <= i <= 100]


def functionDemo3(listTemp):
    """
    写一个函数，实现功能为传入一个元素都为数字的列表，
    将列表中重复的数字删除，返回修改后的列表。（使用循环遍历元素实现）
    :return:
    """

    listReturn = []

    dictResult = Counter(listTemp)
    for key in dictResult.keys():
        if dictResult.get(key) == 1:
            listReturn.append(key)

    return listReturn


def functionDemo4(tupleTemp1, tupleTemp2):
    """
     写一个函数，实现功能为传入两个元组，组合两个元组成一个新的元组，并返回元组。
    :return:
    """
    return tupleTemp1 + tupleTemp2


def functionDemo5(tupleTemp):
    """
    写一个函数，实现功能为传入一个元素都为数字的元组，使用循环查找最大值，并返回最大值。
    :return:
    """
    maxValue = tupleTemp[0]
    for itemTuple in tupleTemp:
        if maxValue < itemTuple:
            maxValue = itemTuple

    return maxValue


def functionDemo6(listTemp):
    """
    写一个函数，实现功能为传入一个元素都为数字的列表，
    使用循环将遍历方式将列表按从小到大的顺序排列后返回排序后的列表。
    :return:
    """

    for i in range(len(listTemp)):
        for j in range(i):
            if listTemp[i] < listTemp[j]:
                iTemp = listTemp[i]
                listTemp[i] = listTemp[j]
                listTemp[j] = iTemp

    return listTemp


def functionDemo7(sTemp):
    """
    写一个函数，要求传入字符串"userName:123456|password:abcdef|email:12345678@qq.com|phoneNumber:13112345678",
    实现字符串切割，返回一个键值对的字典。
    :return:
    """
    dictTemp = {}
    listSplit = sTemp.split('|')
    for itemSplit in listSplit:
        tempSplit = itemSplit.split(':')
        dictTemp[tempSplit[0]] = tempSplit[1]

    return dictTemp


def functionDemo8(iN):
    """
    写一个函数，实现功能为传入一个大于1的整数n，求1*2*3*...*n的结果，并返回。（求阶乘）
    :return:
    """
    iResult = 1
    for i in range(1, iN + 1):
        iResult *= i

    return iResult


def functionDemo9(listTemp):
    """
    写一个函数，实现功能为传入一个元素都为数字的列表，
    要求将列表中所有数字都四舍五入且保留两位小数，并将修改后的列表返回。
    :return:
    """

    for i in range(len(listTemp)):
        listTemp[i] = round(listTemp[i], 2)

    return listTemp


"""
请将如下函数改为lambda匿名函数。
def fun_A(x,y=2):
    return x*y
"""

functionDemo10 = lambda x, y=2: x * y


def functionDemo11(x):
    """
    请将如下lambda匿名函数改为普通函数
    lambda x:x if x%2 else None

    :return:
    """

    if x % 2:
        return x
    else:
        return None


if __name__ == '__main__':
    searchTargetStrs()
