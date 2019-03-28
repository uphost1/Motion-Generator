import datetime
import os
from git import Repo

r_dir = os.path.dirname(os.path.realpath(__file__))
r = Repo(r_dir)
github_repo = '' # Link to github repository

today = datetime.date.today().strftime('%d %B, %Y')
signature = '<p align="right">Signed, your signature</p>'


def start_function():
    op1 = input('[1] Sentencing Order\n[2] Motion to Suppress\n[3] Motion to Compel\n[4]'
                ' Motion to Dismiss\n[5] Motion for Discovery\n[6] Custom Title\nInput: ')

    def input_stuff(ftype):
        global fileName, header, op4, fileType
        fileType = ftype
        op2 = input('Plaintiff: ')
        op3 = input('Defendant: ')
        case = f'{op2} v. {op3}'
        fileName = f'{op2}-v-{op3}date{datetime.datetime.now().strftime("%Y-%m-%d@%H-%M")}.md'
        op4 = input('Body Text: ')
        header = f'\n# In the Federal District Court of the United States\n###### {case}\n<b>{ftype}</b>'

    def save_stuff():
        new_verdict = open(fileName, 'w')
        new_verdict.write(f'{today}{header}<p>{op4}</p>\n{signature}')
        new_verdict.close()
        print(new_verdict.name, 'created')
        
        file_list = [
            f'{os.path.dirname(os.path.realpath(__file__))}/{fileName}'
            ]
        r.index.add(file_list)
        r.index.commit(fileType)
        r.git.pull('origin', 'master')
        r.git.push('origin', 'master')
        print(github_repo+fileName)
        start_function()
    if op1 == '1':
        input_stuff('SENTENCING ORDER')
        save_stuff()
    if op1 == '2':
        input_stuff('MOTION TO SUPPRESS EVIDENCE')
        save_stuff()
    if op1 == '3':
        input_stuff('MOTION TO COMPEL')
        save_stuff()
    if op1 == '4':
        input_stuff('MOTION TO DISMISS')
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


