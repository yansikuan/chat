def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
 
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for message in s[2:]:
					allen_word_count += len(message)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for message in s[2:]:
					viki_word_count += len(message)
		# print(s)
	print('Allen said', allen_word_count, 'words, and', allen_sticker_count, 'stickers, and', allen_image_count, 'images.')
	print('Viki said', viki_word_count, 'words, and', viki_sticker_count, 'stickers, and', viki_image_count, 'images.')
	# return new 


def write_file(filename,lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('viki.txt')
	lines = convert(lines)
	# wrtie_file('viki_output.txt', lines)


main()