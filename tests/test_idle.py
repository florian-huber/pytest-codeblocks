def test_expected_output_w_print(testdir):
    string = """
    Lorem ipsum
    ```idle
    >>> print(1 + 3)
    ```
    dolor sit amet
    <!--pytest-codeblocks:expected-output-->
    ```
    4
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)


def test_expected_output_w_print(testdir):
    string = """
    Lorem ipsum
    ```idle
    >>> 1 + 3
    ```
    dolor sit amet
    <!--pytest-codeblocks:expected-output-->
    ```
    4
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)


def test_expected_output_fail(testdir):
    string = """
    Lorem ipsum
    ```idle
    >>> 1 + 3
    ```
    dolor sit amet
    <!--pytest-codeblocks:expected-output-->
    ```
    5
    ```
    """
    testdir.makefile(".md", string)
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(failed=1)
