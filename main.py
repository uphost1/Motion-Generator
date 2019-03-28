import datetime
import os
from git import Repo


r_dir = os.path.dirname(os.path.realpath(__file__))
r = Repo(r_dir)
github_repo = '' # link to your github repository

today = datetime.date.today().strftime('%d %B, %Y')
signature = '<p align="right">Signed, your signature</p>'


def start_function():
    t_o_f = ['Sentencing Order', 'Motion to Suppress', 'Motion to Compel', 'Motion to Dismiss',
             'Motion for Discovery', 'Custom Title']
    for v, i in enumerate(t_o_f):
        print(f'[{v}]{i}\n')
    op1 = input('\nInput: ')
    print(f'Starting input for {t_o_f[int(op1)]}')
    
    def input_stuff(ftype):
        global fileName, header, op4, fileType
        fileType = ftype
        op2 = input('Plaintiff: ')
        op3 = input('Defendant: ')
        case = f'{op2} v. {op3}'
        fileName = f'{op2}-v-{op3}-{datetime.datetime.now().strftime("%Y-%m-%d@%H-%M")}.md'
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

    for v, i in enumerate(t_o_f):
        if op1 == str(v):
            input_stuff(i)
            save_stuff()


start_function()
