import re
  
# Function to match the string
def match(text):
          
        # regex
        pattern = '[a-z]+[A-Z]+[a-z]'
        pattern1 = '[A-Z]+[a-z]+[A-Z]'
          
        # searching pattern
        if (re.search(pattern1, text)):
        	return('No')
        if re.search(pattern, text):
            return('Yes')
        else:
        	return('No')


if __name__ == "__main__":   
	# Driver Function
	print(match("Sam PrekopJohn McEntire"))
	print(match("Roc MarcianoThe Alchemist"))
	print(match("Roc Marciano The Alchemist"))