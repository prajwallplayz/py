introstring='helo my name is prajwal.hello'
words=introstring.split()
print(words)
def greet(name):
    print('hello ' +name+ ' how are you')
greet('prajwal')

def countwordsfromfile():
    numofwords=0
    filename=input('enter the file name : ')
    file=open(filename,'r')
    for  line in file :
        words=line.split()
        numofwords=numofwords+len(words)
    print(numofwords)
countwordsfromfile()
