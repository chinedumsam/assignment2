import paralleldots
import re
import csv


key = "sBVNWZRgJkC32ZCjvD9fD9cnDDZBrqR1izPOyWfU8wQ"

paralleldots.set_api_key(key)

def clean_tweet(tweet):
    '''
        cleaning tweets with regex
   '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

filename = 'mytweets.csv'

smp = []
mint = []
kimp = []
fine = []

with open(filename,'r',encoding = 'utf8', errors='ignore') as cf:
    mentor = csv.reader(cf)
    for row in mentor:
        smp.append(row[1])

for row in smp:
    mint.append(clean_tweet(row))

for i in range(len(mint)):
    data = paralleldots.sentiment(mint[i])
    for m,n in data.items():
        if m == 'sentiment':
            kimp.append(data[m])
        if m == 'probabilities':
            fine.append(n[data['sentiment']])

print(kimp)
print('\n\n\n')
print(fine)

content = [{'mint':m, 'kimp':k, 'fine':f} for m,k,f in zip(mint, kimp, fine)]

headers = content[0].keys()

with open('final.csv','w') as f:
    pen = csv.DictWriter(f, headers)
    pen.writeheader()
    pen.writerows(content)