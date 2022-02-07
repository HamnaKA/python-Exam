
file= open('prgm2.txt','r+')

s = True


print("Output:")

while s:
    line = file.readline()
    word = line.split(" ")
    if(len(word)>5):
        x = word[0]
        if(x[0].isupper()):
            print(line)
    
