import lxml
import requests
import os
import sys
import json
from requests.cookies import RequestsCookieJar
from lxml import etree

# python HuahuoTestEx.py
QuestionPath = 'D:\PythonCode\\venv\Include\HuahuoQuiz'


def GetQuestionJson():
    QuestionList = []
    FileName = os.listdir(QuestionPath)
    for File in FileName:
        QuestionList.append(QuestionPath + "\\" + str(File))
        # ImageList.append(str(File))
    return QuestionList


def GetQuestionFromBody(QuestionHtml):
    Parser = etree.HTMLParser(encoding='utf-8')
    Html = etree.parse(QuestionHtml, parser=Parser)
    XPath = '//html/body/text()'
    Question = Html.xpath(XPath)  # 这里获取到JSON格式的问题
    Text = Question[0].encode('utf-8').decode('unicode_escape')
    TextList = json.loads(Text)
    return TextList


if __name__ == '__main__':
    QuestionHtmlList = GetQuestionJson()  # 获取所有的问题Html文件的绝对路径
    FileHandle1 = open("D:\PythonCode\\venv\Include\\Question.json", 'a+', encoding='utf-8')#写入句柄
    for QuestionHtml in QuestionHtmlList:
        QuestionList = GetQuestionFromBody(QuestionHtml)
        #FileHandle2 = open(QuestionHtml, 'r', encoding='utf-8')
        i = 0
        while i <= 19:
            FileHandle3 = open("D:\PythonCode\\venv\Include\\Question.json", 'r', encoding='utf-8')#读取句柄
            FileText = FileHandle3.read()
            IsExist = FileText.find(QuestionList[i]['title'])
            if IsExist != -1:
                print("该题已经存在." + "\n")  # 检查题目是否已经存在
                FileHandle3.close()
                i = i + 1
                continue

            print(str(i + 1) + '. ' + QuestionList[i]['title'] + '\n')
            FileHandle1.write(str(i + 1) + '. ' + QuestionList[i]['title'] + '\n')

            print('A ' + QuestionList[i]['options'][0] + ' ')
            FileHandle1.write('A ' + QuestionList[i]['options'][0] + ' ' + '\n')

            print('B ' + QuestionList[i]['options'][1] + ' ')
            FileHandle1.write('B ' + QuestionList[i]['options'][1] + ' ' + '\n')

            print('C ' + QuestionList[i]['options'][2] + ' ')
            FileHandle1.write('C ' + QuestionList[i]['options'][2] + ' ' + '\n')

            print('D ' + QuestionList[i]['options'][3] + ' ')
            FileHandle1.write('D ' + QuestionList[i]['options'][3] + ' ' + '\n')

            FileHandle1.write("\n")
            FileHandle3.close()
            print("\n")
            i = i + 1
    FileHandle1.close()
    Handle = open("D:\PythonCode\\venv\Include\\Question.json", 'r', encoding='utf-8')
    FileText = Handle.read()
    print("当前有" + str(FileText.count("A")) + "道题目")
    Handle.close()