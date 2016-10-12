import xml.etree.ElementTree as ET
import sys
def countSpace(line):
	count = 0
	if len(line) == 0:
		return -1
	else:
		while line[count] == ' ':
			count += 1
		return count


def noteBlock(lines, lineNum):
	if lines[lineNum].endswith("note -"):
		block = []
		space = countSpace(lines[lineNum])
		num = lineNum
		while countSpace(lines[num]) >= space:
			block.append(lines[num])
			num += 1
		return block
	else:
		return 0

def getAllNote(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	AllNote = []
	for EFFormat in root.findall('EFFormat'):
		RuleID = EFFormat.find('RuleID').text
		OriginRule = EFFormat.findtext('OriginRule')
		lines = OriginRule.lower().split('\n')
		count = 0
		EFNote =[]
		for item in lines:
			if item.endswith("note -"):
				block = noteBlock(lines, count)
				EFNote.append(block)
			count += 1
		AllNote += EFNote

	return AllNote

def main():
	filename = 'result_{}.xml'.format(sys.argv[1])
	AllNote = getAllNote(filename)
	# print (len(AllNote))
#	for i in AllNote:
#		for j in i:
#			print (j)
	output = open('{}_Notes.txt'.format(sys.argv[1]),'w')
	for i in AllNote:
		for j in i:
			output.write(j+'\n')	
	output.close() 

if __name__ == "__main__":
    main()
