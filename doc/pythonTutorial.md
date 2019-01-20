

# pythonTutorial

## Variable

### 二进制数据类型：

```python
def dataTypeBase():
    bName = b"jack"
    # bName = b"jack测试" #报错，因为'测试'不是ascii字符，bytes类型不接受非ascii
    print(type(bName))
    print(bName)
```

Output:

![image-20190119105509839](https://ws3.sinaimg.cn/large/006tNc79ly1fzbphenlo9j30sg03omxb.jpg)

### 字符串类型

三引号声明可换行字符串类型

```python

def strTypeBase():
    strName = '''abc
    abc
    abc'''
    print(strName)
```

Output:

![image-20190119105651397](https://ws2.sinaimg.cn/large/006tNc79ly1fzbpj5uo77j30sg04w3yn.jpg)

### 删除变量

使用del删除变量，有点类似于c里面的手动释放内存：

```python
def delVariableBase():
    strName='name'
    print(strName)
    del strName
    print(strName)
```

Output:

![image-20190119105943390](https://ws4.sinaimg.cn/large/006tNc79ly1fzbpm57xvfj31bq07ytab.jpg)

### 字符串运算

```python

def strMultiplyBase():
    strName='abc'
    print(strName)
    strName=strName*3
    print(strName)
```

output:

![image-20190119110142459](https://ws3.sinaimg.cn/large/006tNc79ly1fzbpo7mqmaj31bq03s3yo.jpg)

### 字符串截取

使用str[a::b],a是起始位置，b是步长，例如：

```python
def strSubBase():
    strName='12345678'
    print(strName[0::2])
```

![image-20190119110557451](https://ws1.sinaimg.cn/large/006tNc79ly1fzbpsmrh6bj31bq03s0sv.jpg)

### 字符串格式化

```python
def strModel():
    strContent = '姓名：%s,年龄：%d' % ('小明', 20)
    print(strContent)

```

output：

![image-20190119110906914](https://ws4.sinaimg.cn/large/006tNc79ly1fzbpvx83qjj31bq03sjrm.jpg)

| **符**   **号** | **描述**                             |
| --------------- | ------------------------------------ |
| %c              | 格式化字符及其ASCII码                |
| %s              | 格式化字符串                         |
| %d              | 格式化整数                           |
| %u              | 格式化无符号整型                     |
| %o              | 格式化无符号八进制数                 |
| %x              | 格式化无符号十六进制数               |
| %X              | 格式化无符号十六进制数（大写）       |
| %f              | 格式化浮点数字，可指定小数点后的精度 |
| %e              | 用科学计数法格式化浮点数             |
| %E              | 作用同%e，用科学计数法格式化浮点数   |
| %g              | %f和%e的简写                         |
| %G              | %f 和 %E 的简写                      |
| %p              | 用十六进制数格式化变量的地址         |

### 转义

字符串前面加上r代表该字符串所有内容不转义：

```python
def strConvertBase():
    strContent = '1223\t'
    print(strContent)
    strContent = r'1223\t'
    print(strContent)
    strContent = '1223\\t'
    print(strContent)

```

Output:

![image-20190119111541052](https://ws4.sinaimg.cn/large/006tNc79ly1fzbq2rkklnj31bq04a0sy.jpg)

| **转义字符** | **描述**                                     |
| ------------ | -------------------------------------------- |
| \(在行尾时)  | 续行符                                       |
| \\           | 反斜杠符号                                   |
| \'           | 单引号                                       |
| \"           | 双引号                                       |
| \a           | 响铃                                         |
| \b           | 退格(Backspace)                              |
| \e           | 转义                                         |
| \000         | 空                                           |
| \n           | 换行                                         |
| \v           | 纵向制表符                                   |
| \t           | 横向制表符                                   |
| \r           | 回车                                         |
| \f           | 换页                                         |
| \oyy         | 八进制数，yy代表的字符，例如：\o12代表换行   |
| \xyy         | 十六进制数，yy代表的字符，例如：\x0a代表换行 |
| \other       | 其它的字符以普通格式输出                     |

### 二进制的编码与解码

```python
def strEncodeAndDecodeBase():
    strContent = '测试字符串'
    strEncode = strContent.encode('utf-8')
    print(type(strEncode))
    strDecode = strEncode.decode('utf-8')
    print(type(strDecode))
```

output：

![image-20190119112006924](https://ws1.sinaimg.cn/large/006tNc79ly1fzbq7d8r6kj31bq04a74k.jpg)

### Other

python3中数字没有大小限制，可以任意大

## Function

### \_\_name\_\_

`__name__`的意思是当前文件的“环境”，比如我们写：

Demo1.py:

```python
def demo1():
    a=1
    b=1
    
if __name__=='__main__':
	print('demo')
```

如果执行Demo1.py，则会执行`print('demo')`这一句，因为当前`__name__`就是`__main__`，但是如果：

Demo2.py

```python
import Demo1

Demo1.demo1()

```

这时就不会执行`print('demo')`这一句，因为此时`Demo1.py`中的`__name__`已经成了`Demo1`:

```python
def nameDemo():
    print(demo1.__name__)
```

![image-20190119154056708](https://ws3.sinaimg.cn/large/006tNc79ly1fzbxqrcx4tj30l803kglp.jpg)

### find&index

功能：查找目标字符串中的特定字串，如果找到返回第一个符合的下标，如果没找到：

- find：返回-1
- index： Raises ValueError

```python

def findAndINdex():
    strContent = '12345623'
    print(strContent.find('23'))
    print(strContent.index('23'))
    print(strContent.find('233'))
    print(strContent.index('233'))
```

![image-20190119153753793](https://ws4.sinaimg.cn/large/006tNc79ly1fzbxnl1i0yj31a60beq4l.jpg)



### isinstance

判断变量类型：

```python
def isinstanceFunc():
    strName = '测试字符串'
    print(isinstance(strName, str))
    a=0
    print(isinstance(a,int))
```

![image-20190119154346532](https://ws2.sinaimg.cn/large/006tNc79ly1fzbxtpa73nj30l803kq2z.jpg)

### lambda表达式

用于实现功能简单的函数

```python
def lambdaFunc():
    func = lambda x: x * x
    print(func(5))
    func2 = lambda x, y=3: x + y
    print(func2(10, 20))
    print(func2(10))

    func3 = lambda x, y: x + y if x > y else x * y
    print(func3(10, 20))

```

![image-20190119154818619](https://ws2.sinaimg.cn/large/006tNc79ly1fzbxyfanjfj30l80700sw.jpg)

## 链表

#### enumerate

enumerate:返回数组的下标和值

```python
def listFunc():
    listDemo = ['str1', 10, True, 3.14,[1,2,3]]
    print(listDemo)
    #替换前后的长度可以不一样
    listDemo[1:3]=[1,2,3,4,5]
    print(listDemo)

    for x,y in enumerate(listDemo):
        print(x,y)
```

![image-20190119160532808](https://ws4.sinaimg.cn/large/006tNc79ly1fzbygcdk3nj30l80b0t98.jpg)

#### count

计算指定内容出现了多少次

```python
def listCountFunc():
    listDemo=[1,2,3,4,1,2,4]
    print(listDemo.count(1))
```

![image-20190119162309389](https://ws3.sinaimg.cn/large/006tNc79ly1fzbyyoopt5j30l8046wei.jpg)

#### copy

普通list的`=`是引用赋值，二者会建立关联，copy返回的拷贝对象与原对象之间没有引用的关系：

```python
def copyFunc():
    listDemo=[1,2,3,4,5]
    listDemo2=listDemo
    listDemo2[1]=1
    print(listDemo)
    listDemo3=listDemo.copy()
    listDemo3[1]=10
    print(listDemo)

```

![image-20190119162707920](https://ws1.sinaimg.cn/large/006tNc79ly1fzbz2tosbfj30l8046q31.jpg)

## 字典

```python
def dictFunc():
    demoDic={'key1':12,'key2':122,'key3':1234}
    print(demoDic['key1'])
    print(demoDic.get('key1'))
```

![image-20190119164021556](https://ws3.sinaimg.cn/large/006tNc79ly1fzbzgkx97qj30l803qdfv.jpg)

直接使用[]和使用get获取特定key的区别是使用[]时如果没有符合的key则抛出异常，使用get则会返回None；

```python
def dictFunc():
    demoDic={'key1':12,'key2':122,'key3':1234}
    print(demoDic['key11'])
    print(demoDic.get('key11'))
```

![image-20190119164138331](https://ws2.sinaimg.cn/large/006tNc79ly1fzbzhwq3k1j3184078wfu.jpg)

## 元组

元组和链表的唯一区别是元组里面的内容是不能更改的，而链表里面的内容是可以更改的。

## FileIo

一个.代表当前路径
两个..代表上一级路径

```python
fileDemo=open('../resource/fileIoDemo.txt',mode='w',encoding='utf-8')
fileDemo.write('12345')
fileDemo.close()
```

如果文件可能不存在或没有操作权限，使用try...except 捕捉异常:

```python
    try:
        fileDemo2 = open('../resource/fileIoDemo2.txt', mode='r', encoding='utf-8')
        ...
        #注意如果open不成功，close也会异常，所以需要对其进行捕捉
        fileDemo2.close()
    except:
        print('error')
    finally:
        print('finally')
```

finally不管出没出错都会执行：

![image-20190120090157016](https://ws4.sinaimg.cn/large/006tNc79ly1fzcrtx5tr5j30mu04mglp.jpg)



使用with不同再手动关闭文件.

```python
    with open('../resource/fileIoDemo2.txt', mode='r', encoding='utf-8') as fileDemo3:
        str1 = fileDemo3.read()
        print(str1)
```

