#STRING METHODS

name = 'Hello Timson'
greeting = "it's nice meeting you"
print(name)

slice = name[0:6]
print(slice)

slice = name[0:]
print(slice)

slice = name[0:8:2]
print(slice)

fname = 'Hello'
fnext = 'world'
conc = fname +' '+ fnext
print(conc)

s = 'Learning python is fun!'
l = len(s)
print(l)

s = 'LEARNING PYTHON IS FUN!'
low = s.lower()
print(low)

s = 'Learning python is fun!'
upp = s.upper()
print(upp)

s = 'Learning PYTHON is FUN!'
swap = s.swapcase()
print(swap)

s = 'learning python is fun!'
cap = s.capitalize()
print(cap)

s = 'learning python is fun!'
tit = s.title()
print(tit)

s = '    ---Learning python is fun!'
ls = s.lstrip()
print(ls)

s = 'Learning python is fun!---   '
rs = s.rstrip()
print(rs)

s = 'learningpythonisfun'
maxa = max(s)
mina = min(s)
print(maxa)
print(mina)

s = 'Learning python is fun!'
count_str = s.count('n', 0, len(s))
print(count_str)

s = 'Learning python is fun and Ann is happy about it!'
repl = s.replace('is', 'was')
repl2 = s.replace('is', 'was', 1)
print(repl)
print(repl2)

s = 'Learning python is fun!'
indx = s.index('thon', 0, len(s))
print(indx)

is_lower = s.islower()
is_upper = s.isupper()
print(is_lower)
print(is_upper)
