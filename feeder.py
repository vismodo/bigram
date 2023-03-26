import re
corpus_file = open('corpus.txt',encoding='utf-8')
corpus_fl = corpus_file.read()
corpus_file.close()
#set number of grams
grams = 2
#format corpus
corpus = re.sub(r'\n(.*?):', '', corpus_fl)
corpus = corpus.replace('\n',' ').replace('.',' . ').replace('?',' ? ').replace('!',' ! ').replace(',',' , ').replace('"',' " ')
corpus = re.sub(r'\s+', ' ', corpus).lower()
corpus = corpus.split(' ')[0:1000000]
corpus_fl = ' '.join(corpus)
#Get unique tokens
words = set(corpus)

prompts = set()
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
corp_len = len(corpus)
for x in range(corp_len-grams):
    #set prompt to last 2 tokens
    prompt = ' '.join(corpus[x:x+grams])
    if x%1000 ==0:
        print(x*100/corp_len)
    prompts.add(prompt)
    words = ngram_counts[prompt].keys()
    counts = ngram_counts[prompt].values()
    arranged = sorted(zip(counts, words), reverse=True)
    a = list(dict(arranged).values())
    preds.append(a[0:min(10,len(a))])
#save prompts
prompt_fl = open('prompts.txt', 'w',encoding="utf-8")
prompt_fl.write(str(list(prompts)))
prompt_fl.close()
#save predictins
preds_fil = open('preds.txt', 'w',encoding="utf-8")
preds_fil.write(str(preds))
preds_fil.close()
