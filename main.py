def c(s1):
	if s1[::-1]==s1:
		return True
	return False
str=input()
if c(s1):
	print("given number is palindrome")
else:
	print("given number is not a palindrome")