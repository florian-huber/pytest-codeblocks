```
>>> “five” + “five”

>>> “five” + 5

>>> 2 * “five”

>>> “five” - “ive”
```
Nope, no solutions here... just try it out yourself.


### Handling strings (very basics)
There is a huge amount of things to know and to learn about handling strings in Python. Most of it will come later, so let's just look at some basics for now.

Strings can be added to other strings.

But additing a string to an integer or a float won't work:
<!--pytest-codeblocks:expect-error-->
```python
"100" + 5  # => TypeError
```
Makes sense.
But wait... why does Python now what is an `integer (int)`, a `float`, or a `string (str)`?

Well, that's called **duck typing** which essentially means that Python automatically assigns the type that the input resembles to.
(*"When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck."*, see [Duck test (wikipedia](https://en.wikipedia.org/wiki/Duck_test#History)

### Changing types
In some cases you might want to change the type, for instance make an `integer` from a `float`:
```python
print(5 + int(7.00001))
```
<!--pytest-codeblocks:expected-output-->
```
12
```
Only be careful that this is **NOT** the same as rounding!
```
>>> int(12.9)
12
```
(if you want to round properly run `int(round(12.9))`, but we'll cover more math functions later in the course)

Or you might want to get a number from a string:
```
>>> 5 + int("19")
24
```
