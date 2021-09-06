```
>>> "five" + "five"

>>> "five" + 5

>>> 2 * "five"

>>> "five" - "ive"
```

<!--pytest-codeblocks:expect-error-->
```python
"100" + 5  # => TypeError
```

```python
print(5 + int(7.00001))
```
<!--pytest-codeblocks:expected-output-->
```
12
```
