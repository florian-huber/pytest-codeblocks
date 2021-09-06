def test_expected_output(testdir):
    string = """
    ```python
    print("Take this!" + " And that!")
    ```
    will return a single string:
    <!--pytest-codeblocks:expected-output-->
    ```
    Take this! And that!
    ```
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
    Or you might want to make a string of a number, for instance to add it to another string.
    ```python
    print("7 + 5 = " + str(7 + 5))
    ```
    <!--pytest-codeblocks:expected-output-->
    ```
    7 + 5 = 12
    ```
    Lorem ipsum
    ```python
    print(1 + 3)
    print(1 - 3)
    print(1 * 3)
    ```
    dolor sit amet
    <!--pytest-codeblocks:expected-output-->
    ```
    4
    -2
    3
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)
