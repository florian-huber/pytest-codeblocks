import pathlib


def test_markdowns_in_test_folder():
    this_dir = pathlib.Path(__file__).resolve()
    result = this_dir.runpytest("--codeblocks")
    result.assert_outcomes(passed=1)
