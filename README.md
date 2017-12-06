# kindle-note
用Python写的整理笔记的程序和自己的读书笔记。

程序执行通过

```shell
python3 makeNote.py demo.txt
```

剩下的都是看过的笔记保存。

## python3 常用代码
使用Python3主要是因为python3对中文的支持更好，在正则匹配的时候能够直接匹配。

### 读写文件
```python
# 读文件
with open(path, 'r', encoding='utf-8') as file:
    # 一次性读取文件
    file.read()
    # 每次读取一行
    file.readline()
    # 调用readlines()一次读取所有内容并按行返回list
    for line in f.readlines():
        print(line.strip())
# 写文件
with open('file.md', 'w', encoding='utf-8') as note:
    note.write('content')
```

### 正则表达式
```python
import re
# 找到所有匹配的子串，并返回一个 list
re.findall(r'\d{1,2}', string)
```

### 读取调用文件的参数
```python
import sys
def main(argv=None):
    if argv is None:
        argv = sys.argv
    print(argv[1])
```

### 字典操作
```python
#新建
d = {}
# 判断是否在字典中
title in d
```

### 数组操作
```python
# 新建
l = []
# 添加
l.append(1)
```