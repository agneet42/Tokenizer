from nltk.tokenize import TweetTokenizer			# importing the TweetTokenizer	
T=TweetTokenizer()									# Creating object
s=raw_input("Enter your string")					# Taking the input
print(T.tokenize(s))								# Printing the output