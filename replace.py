import docx
import re

file = docx.Document("resource/a.docx")
for para in file.paragraphs:
    """思路：用正则匹配到要求改的地方，利用正则对其进行修改"""
    """想的太简单了，这样修改只能修改文本，并不能匹配样式。就这样放着吧！"""
    """re.sub(pattern, repl, string, count=0, flags=0)"""
text1 = para.text


def time1(text1):
    text2 = re.sub(r'\d{4}年\d月\d{2}日', '2020年1月1日', text1, count=0)
    # 三部分时间
    return text2


text2 = time1(text1)


def time2(text2):
    text3 = re.sub(r'\d{4}年\d-\d月', '2020年1月1日', text2, count=0)
    # 两部分时间
    return text3


text3 = time2(text2)


def money(text3):
    text = re.sub(r'-*\d,*\d*\.\d*亿元', '888,888.888亿元', text3, count=0)
    print(text)


if __name__ == '__main__':
    time1(text1)
    time2(text2)
    money(text3)
