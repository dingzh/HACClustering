from sys import argv
import re
import codecs

def ruleClean(rule):
	rule = re.sub(r'--.*--', r' ', rule)
	rule = re.sub(r'--+', r' ', rule)
	rule = re.sub(r'(\w)-', r'\1 ', rule)
	rule = re.sub(r'-(\w)', r' \1', rule)
	rule = re.sub(r'[\t ]-', r' ', rule)
	rule = re.sub(r'[1-9a-z]\. *(\w)', r'\1', rule)
	rule = re.sub(r'\.\.\.', r' ', rule)
	rule = re.sub(r'\.[ \.]*\.', r' . ', rule)
	rule = re.sub(r'xpf', r'.', rule)

	return rule
	
with codecs.open(argv[1]) as f:
	rule = f.read()
	rule = ruleClean(rule)
	print(rule)