import lxml
import requests
import os
import sys
import json
from requests.cookies import RequestsCookieJar

URL = "https://www.say-huahuo.com/qa.php"
Session = requests.session()
Html = Session.get(URL)

ExplainText = Html.text.encode('utf-8').decode('unicode_escape')  # 把Unicode代码转为中文

ExplainTextDic = json.loads(ExplainText)  # 将JSON转为字典

FileHandle = open("Question.json", 'a+', encoding='utf-8')  # 以追加模式打开文件
i = 0
while i <= 19:
    FileHandle2 = open("Question.json", 'r', encoding='utf-8')
    FileText = FileHandle2.read()
    IsExist = FileText.find(ExplainTextDic[i]['title'])
    if IsExist != -1:
        print("该题已经存在." + "\n")   # 检查题目是否已经存在
        i = i + 1
        continue

    print(str(i + 1) + '. ' + ExplainTextDic[i]['title'])
    FileHandle.write(str(i + 1) + '. ' + ExplainTextDic[i]['title'] + '\n')

    print('A ' + ExplainTextDic[i]['options'][0] + ' ')
    FileHandle.write('A ' + ExplainTextDic[i]['options'][0] + ' ' + '\n')

    print('B ' + ExplainTextDic[i]['options'][1] + ' ')
    FileHandle.write('B ' + ExplainTextDic[i]['options'][1] + ' ' + '\n')

    print('C ' + ExplainTextDic[i]['options'][2] + ' ')
    FileHandle.write('C ' + ExplainTextDic[i]['options'][2] + ' ' + '\n')

    print('D ' + ExplainTextDic[i]['options'][3] + ' ')
    FileHandle.write('D ' + ExplainTextDic[i]['options'][3] + ' ' + '\n')
    FileHandle.write('\n')

    print('\n')

    FileHandle2.close()
    i = i + 1
FileHandle2 = open("Question.json", 'r', encoding='utf-8')
FileText = FileHandle2.read()
print("当前有"+str(FileText.count("A"))+"道题目")
FileHandle.close()
FileHandle2.close()