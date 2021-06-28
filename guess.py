import random
words =open("file.txt")
a=list()
for i in words:
		i = i.rstrip()
		a.append(i)
r=random.randint(0,len(a)-1)
a=a[r]
f=list(a)
count=0
g=list()
for i in range(0,len(a)):
  g.append("*")
def enter(count):
  if g==f:
    print("you're the winner")
    print(g)
  else:
    b=input("enter the valeue :")
    check(b,count)
def check(b,count):
  if len(b)==1:
    main(b,count)
  else:
    print("please enter one value")
    enter(count)
def main(b,count):
  if count < 10:
    if b in a:
      g[a.index(b)]=b
      print(g)
      enter(count)
    else:
      print("not found")
      print(g)
      count=count+1
      print("you lost {0} chance and you have {1} chance left".format(count,10-count))
      enter(count)
  else:
    print("you lost the game")
    print(a)
enter(count)
