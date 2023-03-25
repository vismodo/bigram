prompts = eval(open('prompts2.txt',encoding='utf-8').read().lower())
preds = eval(open('preds2.txt',encoding='utf-8').read().lower())
from random import choice
while True:
    prompt = input('\n Enter 2 Words: ')
    if prompt.lower() in prompts:
        sentence = ' '.join(prompt.lower().split(' ')[0:4])
        print(sentence, end="")
        for x in range(20):
            word = choice(preds[prompts.index(sentence)][0:min(2,len(preds[prompts.index(sentence)]))])
            sentence = sentence.split(' ')[-1] + ' ' + word
            print(' '+word, end="")
            if not sentence in prompts:
                print('\nUNABLE TO CONTINUE')
                break
        print('\n')
    else:
        print('UNABLE TO CONTINUE')

