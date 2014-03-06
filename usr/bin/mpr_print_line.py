import sys

s = str(sys.argv[1])

# k is a list
k = s.split(' -')

# length of list
n = len(k)

post_noncomp = 0
compound = 0
first = 1
# for loop
for item in k:
	try:	
		if item[0] == 'I' and item[1] != 'n' or item[0] == 'L' and item[1] != 'D':
			if compound:
				sys.stdout.write('\n')
				compound = 0
			sys.stdout.write('        ' + '-' + item + '\n')
			first = 0
			post_noncomp = 1
		else:
			if post_noncomp:
				sys.stdout.write('    ')
				post_noncomp = 0
			if first != 1:
				sys.stdout.write('-' + item + ' ')
			else:
				sys.stdout.write(item + ' ')
				first = 0
			compound = 1
	except IndexError:
		sys.stdout.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + item + '\n')
	except SyntaxError:
		sys.stdout.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + item + '\n')
sys.stdout.write('\n')
