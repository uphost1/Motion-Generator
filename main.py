import os
import datetime
import base64
import git
from git import Repo

r_dir = 'directory here'
r = Repo(r_dir)

today = datetime.date.today().strftime('%d %B, %Y')
signature = '<p align="right">Signed, your signature</p>'

def start_function():
    op1 = input('[1] Sentencing Order\n[2] Motion to Suppress\n[3] Motion to Compel\n[4] Motion to Dismiss\n[5] Motion for Discovery\n[6] Custom Title\nInput: ')
    def input_stuff(ftype):
        global fileName, header, op4, fileType
        fileType = ftype
        op2 = input('Plaintiff: ')
        op3 = input('Defendant: ')
        fileName = op2 + '-v-' + op3 + datetime.datetime.now().strftime('%Y-%m-%d@%H-%M') + '.md'
        op4 = input('Body Text: ')
        header = '\n# In the Federal District Court of the United States\n###### ' + op2 + ' v. ' + op3 + '\n' + '<b>' + ftype + '</b>'
    def save_stuff():
        newVerdict = open(fileName, 'w')
        newVerdict.write(today + header +'<p>' + op4 + '</p>\n' + signature)
        newVerdict.close()
        print(newVerdict.name, 'created')
        
        file_list = [
            'C:\\Users\westo\Desktop\Test\\'+fileName
            ]
        r.index.add(file_list)
        r.index.commit(fileType)
        r.git.pull('origin', 'master')
        r.git.push('origin','master')
        print('github repo here'+fileName)
        start_function()
    if op1 == '1':
        input_stuff("SENTENCING ORDER")
        save_stuff()
    if op1 == '2':
        input_stuff("MOTION TO SUPPRESS EVIDENCE")
        save_stuff()
    if op1 == '3':
        input_stuff("MOTION TO COMPEL")
        save_stuff()
    if op1 == '4':
        input_stuff("MOTION TO DISMISS")
        save_stuff()
    if op1 == '5':
        input_stuff("MOTION FOR DISCOVERY")
        save_stuff()
    if op1 == '6':
        input_stuff(input('Title: '))
        save_stuff()
    else:
        print('ok')
        start_function()

start_function()
