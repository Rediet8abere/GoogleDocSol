
"""Find the longest substring of unique letters in a given string of n letters.

input: string
output: string """
s = pneumonoultramicroscopicsilicovolcanoconiosis

def unique_substring(s):
	unique_strings = {}
	unique_letters = []

	for i in range(len(s)):
		if s[i] not unique_letters:
			unique_letters.append(s[i])
		else:
unique_strings[unique_letters] = len(unique_letters)
unique_letters = []
unique_letters.append(s[i])
	max, unique = 0, ‘’
	for uni_str, val_len in unique_strings,items:
		if val_len > max:
			max, unique = val_len, uni_str
	return unique
