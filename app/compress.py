VALID_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'
OUT_CHARS = '.123456789'
L_v = len(VALID_CHARS)
L_o = len(OUT_CHARS)

def compress_code(code):
	'''code should consist of characters: 1-9, other (10 options)'''

	i = 0
	for c in code[80::-1]:
		i *= 10
		if c in '123456789':
			i += int(c)

	out = ''
	while i:
		out += VALID_CHARS[i%L_v]
		i /= L_v

	out = out[::-1]

	if code.length <= 81: return out
	return out+'_'+code[81:]

def decompress_code(code):

	i = 0
	for c in code.split('_')[0]:
		i *= L_v
		i += VALID_CHARS.index(c)

	out = ''
	while i:
		out += OUT_CHARS[i%L_o]
		i /= L_o

	while len(out) < 81: out += '.'

	return out+''.join(code.split('_')[1:])