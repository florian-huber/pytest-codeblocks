def test_idle(testdir):
    string = """
    Lorem ipsum
    ```idle
    >>> 5 + 7
    12
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)


def test_idle_fail(testdir):
    string = """
    ```idle
    >>> print("abc)
    SyntaxError: 
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(failed=1)


def test_idle_expect_fail_passed(testdir):
    string = """
    <!--pytest-codeblocks:expect-error-->
    ```idle
    >>> print("abc)
    SyntaxError: 
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)


def test_idle_expected_return_fail(testdir):
    string = """
    ```idle-return
    >>> 5 + 7
    13
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(failed=1)

    
def test_idle_expected_return(testdir):
    string = """
    ```idle-return
    >>> 5 + 7
    12
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)
