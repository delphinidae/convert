import convert_func
import pytest


class TestClassCut():

    def test_space(self):
        assert convert_func.cut_line("a \n", 0) == "a "  # mmm...?

    def test_new_line(self):
        assert convert_func.cut_line("a\n", 0) == "a"

    def test_tab(self):
        assert convert_func.cut_line("a\t", 0) == "a\t"


class TestClassSplit():

    def test_positive1(self):
        assert convert_func.split_line("a\tb\tc", 3, 0) == ["a", "b", "c"]

    def test_positive2(self):
        assert convert_func.split_line("a\tb\tc\t", 4, 0) == ["a", "b", "c", ""]

    def test_positive3(self):
        assert convert_func.split_line("a\tb\t\tc\t", 5, 0) == ["a", "b", "", "c", ""]

    def test_negative1(self):
        with pytest.raises(Exception) as excinfo:
            convert_func.split_line("a\tb\tc", 4, 0)
        assert "The wrong column number in line 0. There shoud be 4 columns, 3 found" in str(excinfo)

    def test_negative2(self):
        with pytest.raises(Exception) as excinfo:
            convert_func.split_line("a\tb\tc", 2, 0)
        assert "The wrong column number in line 0. There shoud be 2 columns, 3 found" in str(excinfo)


class TestColumns():

    def test_positive(self):
        assert convert_func.process_columns("a\tb\tc") == {"a": "", "b": "", "c": ""}

    def test_negative(self):
        with pytest.raises(Exception) as excinfo:
            convert_func.process_columns("a\tb\ta")
        assert "Columns should be unique!" in str(excinfo)
