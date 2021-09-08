import pathlib


def test_example_markdown(testdir):
    this_dir = pathlib.Path(__file__).resolve().parent
    testdir.copy_example(this_dir / "example_unicode_issues.md")
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=0)
