def fileIoDemo():
    '''

    :return:
    '''
    # 一个.代表当前路径
    # 两个..代表上一级路径
    fileDemo = open('../resource/fileIoDemo.txt', mode='w', encoding='utf-8')
    fileDemo.write('12345')
    fileDemo.close()

    try:
        fileDemo2 = open('../resource/fileIoDemo2.txt', mode='r', encoding='utf-8')
    except:
        print('error')
    finally:
        print('finally')

    with open('../resource/fileIoDemo2.txt', mode='r', encoding='utf-8') as fileDemo3:
        str1 = fileDemo3.read()
        print(str1)


if __name__ == '__main__':
    fileIoDemo()
