import re
corpus_file = open('corpus2.txt',encoding='utf-8')
corpus_fl = corpus_file.read()
corpus_file.close()

grams = 2
corpus = re.sub(r'\n(.*?):', '', corpus_fl)
corpus = corpus.replace('\n',' ').replace('.',' . ').replace('?',' ? ').replace('!',' ! ').replace(',',' , ')
corpus = re.sub(r'\s+', ' ', corpus)
corpus = corpus.split(' ')[0:1000000]
corpus_fl = ' '.join(corpus)
words = set(corpus)
prompts = []
preds = []

# precompute n-gram counts
ngram_counts = {}
for i in range(len(corpus)-grams):
    prompt = ' '.join(corpus[i:i+grams])
    word = corpus[i+grams]
    if prompt not in ngram_counts:
        ngram_counts[prompt] = {}
    if word not in ngram_counts[prompt]:
        ngram_counts[prompt][word] = 0
    ngram_counts[prompt][word] += 1

for x in range(len(corpus)-grams):
    prompt = ' '.join(corpus[x:x+grams])
    if x%1000 ==0:
        print(x*100/len(corpus))
    if prompt not in prompts:
        prompts.append(prompt)
        best_word = []
        prob = 0
        if prompt in ngram_counts:
            for word, count in ngram_counts[prompt].items():
                if count > prob:
                    best_word.append(word)
                    prob=count
        preds.append(list(reversed(best_word)))

prompt_fl = open('prompts2.txt', 'w',encoding="utf-8")
prompt_fl.write(str(prompts))
prompt_fl.close()

preds_fil = open('preds2.txt', 'w',encoding="utf-8")
preds_fil.write(str(preds))
preds_fil.close()
