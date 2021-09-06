import pathlib


def test_example_markdown(testdir):
    this_dir = pathlib.Path(__file__).resolve().parent
    testdir.copy_example(this_dir / "example.md")
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=7)


def test_unicode_markdown(testdir):
    this_dir = pathlib.Path(__file__).resolve().parent
    testdir.copy_example(this_dir / "examples_unicode.md")
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=5)
