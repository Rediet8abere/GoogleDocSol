
"""Find the longest substring of unique letters in a given string of n letters.

input: string
output: string """
s = 'pneumonoultramicroscopicsilicovolcanoconiosis'

def unique_substring(s):
	""" Running-Time: 2*O(n)
		Space-Complexity: O(k) + O(v) --> k represents the key in our case is the length of a string
										  v represents the value which is list in this case 
	"""
	unique_strings = {}
	unique_letters = []

	for i in range(len(s)):
		if s[i] not in unique_letters:
			unique_letters.append(s[i])
		else:
			unique_strings[len(unique_letters)] = unique_letters
			unique_letters = []
			unique_letters.append(s[i])
	print("unique_strings: ", unique_strings)
	max, unique = 0, ""
	for val_len, uni_str in unique_strings.items():
		if val_len > max:
			max, unique = val_len, ''.join(uni_str)
	return unique

print("longest substring: ", unique_substring(s))
