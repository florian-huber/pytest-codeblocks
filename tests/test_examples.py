import pathlib


def test_markdowns_in_test_folder(testdir):
    this_dir = pathlib.Path(__file__).resolve().parent
    testdir.copy_example(this_dir / "example.md")
    result = testdir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)
