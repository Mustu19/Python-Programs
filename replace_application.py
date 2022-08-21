letter = '''\n|Python| is the best programming language.
It enables user to write code efficiently and accurately.
Thank you.
'''

letter = letter.replace("best" , "worst")
letter = letter.replace("|Python|" , "Java")
letter = letter.replace("Thank" , "abcd")
print(letter)
