import pytest

from homework_09.merge_sorted_files import merge_sorted_files


def test_sample_sort(tmp_path):
    tmppath = tmp_path

    file_135 = tmppath / "test_1_3_5.txt"
    file_135.write_text("1\n3\n5\n")

    file_246 = tmppath / "test_2_4_6.txt"
    file_246.write_text("2\n4\n6\n")

    assert list(merge_sorted_files([file_135, file_246])) == [1, 2, 3, 4, 5, 6]


def test_one_file_sort(tmp_path):
    tmppath = tmp_path

    file_135 = tmppath / "test_1_3_5.txt"
    file_135.write_text("1\n3\n5\n")

    assert list(merge_sorted_files([file_135])) == [1, 3, 5]


def test_three_files(tmp_path):
    tmppath = tmp_path

    file_135 = tmppath / "test_1_3_5.txt"
    file_135.write_text("1\n3\n5\n")

    file_246 = tmppath / "test_2_4_6.txt"
    file_246.write_text("2\n4\n6\n")

    file_107 = tmppath / "test_1_0_7.txt"
    file_107.write_text("1\n0\n7\n")

    assert list(merge_sorted_files([file_135, file_246, file_107])) == [
        0,
        1,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
    ]


def test_empty_file(tmp_path):
    tmppath = tmp_path

    file_empty = tmppath / "test_empty_file.txt"
    file_empty.write_text("")

    assert list(merge_sorted_files([file_empty])) == []


def test_wrong_filename():
    with pytest.raises(FileNotFoundError):
        list(merge_sorted_files(["not_exist_file.txt"]))


def test_not_ints_in_file(tmp_path):
    tmppath = tmp_path

    file_3x2 = tmppath / "test_not_int_file.txt"
    file_3x2.write_text("a\nb\n3.0\n")

    with pytest.raises(ValueError, match="invalid literal ..."):
        list(merge_sorted_files([file_3x2]))
