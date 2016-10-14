from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000/')
text = (
  'I love you She is a bitch If you need to get a refund, please contact me ')
output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
print(output['sentences'][0]['parse'])
