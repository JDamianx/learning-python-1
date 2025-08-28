a=int(input("wprowadz a: "))
b=int(input("wprowadz B: "))
c=int(input("wprowadz c: "))
d=int(input("wprowadz d: "))
e=int(input("wprowadz e: "))

if a>b:a,b=b,a
if b>c:b,c=c,b
if c>d:c,d=d,c
if d>e:d,e=e,d

if a>b:a,b=b,a
if b>c:b,c=c,b
if c>d:c,d=d,c

if a>b:a,b=b,a
if b>c:b,c=c,b

if a>b:a,b=b,a

print(a,b,c,d,e)