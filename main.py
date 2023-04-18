def counter(fname):
	# variable to store total word count
	num_words = 0
	# variable to store total line count
	num_lines = 0
	# variable to store total character count
	num_charc = 0
	# variable to store total space count
	num_spaces = 0
	with open(fname, 'r') as f:
		for line in f:
			num_lines += 1
			word = 'Y'
			for letter in line:
				if (letter != ' ' and word == 'Y'):
					num_words += 1
					word = 'N'
				elif (letter == ' '):
					num_spaces += 1
					word = 'Y'
				for i in letter:
					if(i !=" " and i !="\n"):
						
						# incrementing character
						# count by 1
						num_charc += 1
						
	# printing total word count
	print("Кількість слів у текстовому файлі: ",
		num_words)
	
	# printing total line count
	print("Кількість рядків у текстовому файлі: ",
		num_lines)
	
	# printing total character count
	print('Кількість символів у текстовому файлі: ',
		num_charc)
	
	# printing total space count
	print('Кількість пробілів у текстовому файлі: ',
		num_spaces)
	
# Driver Code:
if __name__ == '__main__':
	fname = 'File1.txt'
	try:
		counter(fname)
	except:
		print('File not found')

