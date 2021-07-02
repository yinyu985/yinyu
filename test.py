import docx
import re

file = docx.Document("resource/a.docx")
for para in file.paragraphs:
    """思路：用正则匹配到要求改的地方，利用正则对其进行修改"""
    """re.sub(pattern, repl, string, count=0, flags=0)"""
text = para.text


def time():
    a = re.sub(r'\d\d\d\d年\d月', '2020年1月', text, count=0)
    print(a)


def money():
    a = re.sub(r'\d*.\b', '888,888.888亿元', text, count=0)
    print(a)


if __name__ == '__main__':
    # time()
    money()
