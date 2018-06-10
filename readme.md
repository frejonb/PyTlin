# PyTlin
Module implementing the Kotlin functions `also`, `let`, and `run` in Python. Additionally it includes sh-like (and Mathematica-like) piping syntax.

The Kotlin functions are documented in [here](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/index.html).

# Install
```python
pip install PyTlin
```

# Syntax
```python
from PyTlin import k

k(obj).let(func).also(func)
k.run(func)
k(obj) | func1 | func2 | ...
k(obj) @ func1 @ func2 @ ...
```
Here all expressions (except `k.run(func)`) is wrapped in the class `k`. To recover `obj` one can apply either of these
```python
k(obj).end
k(obj) | 'end'
k(obj) | 0
k(obj) @ 'end'
k(obj) @ 0
```

# Example
```python
from PyTlin import k
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __repr__(self):
		return '%s, %d' % (self.name, self.age)
	def increaseAge(self):
		self.age = self.age + 1
	def nameToUpperCase(self):
		self.name = self.name.upper()

student = Person('Pete', 18)
print(student) #Pete, 18
```

## let
```python
name = k(student).let(lambda x: (print(x),x.name)[1]) #Pete, 18
print(name) #Pete
```

## also
```python
newstudent = k(student).also(lambda x: (x.increaseAge(), x.nameToUpperCase()))
print(newstudent) #PETE, 19
```

## run
```python
mood = 'sad'
k.run(lambda mood = 'happy': print(mood)) #happy
print(mood) #sad
```

## Piping
Piping can be done with either `.let` or with pipe operators `@` (Mathematica-like in reverse order) or `|` (sh-like).

```python
ops=k(4).let(lambda x: x*2).let(lambda x: x+3)
print(ops) #11
print(type(ops)) #<class 'PyTlin.k'>
print(ops.end) #11
print(type(ops.end)) #<class 'int'>

print(ops.end ==
 k(4) @ (lambda x: x*2) @ (lambda x: x+3) @ 'end') #True

print(ops.end ==
 k(4) | (lambda x: x*2) | (lambda x: x+3) | 0) #True
```
