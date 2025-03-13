#prompt a input from the user
txt = input()

#convert ":)" and ":(" into emoji`s
txt = txt.replace(':)', '🙂')
txt = txt.replace(':(', '🙁')

#print the user`s text convert
print(txt)
