from homework_09.file_counter import universal_file_counter


def test_one_file_2_rows(tmp_path):
    tmppath = tmp_path

    file_3x2 = tmppath / "1_2_3__4_5_6.txt"
    file_3x2.write_text("first second third\nfourth fifth sixth\n")

    assert universal_file_counter(tmppath, "txt") == 2


def test_one_file_2_rows_with_tokenizer(tmp_path):
    tmppath = tmp_path

    file_3x2 = tmppath / "1_2_3__4_5_6.txt"
    file_3x2.write_text("first second third\nfourth fifth sixth\n")

    assert universal_file_counter(tmppath, "txt", str.split) == 6


def test_two_files_3x2_and_1x3(tmp_path):
    tmppath = tmp_path

    file_3x2 = tmppath / "1_2_3__4_5_6.txt"
    file_3x2.write_text("first second third\n4 5 6\n")
    file_1x3 = tmppath / "1__2__3.txt"
    file_1x3.write_text("first\n second\n third")

    assert universal_file_counter(tmppath, "txt") == 5


def test_two_files_3x2_and_1x3_with_tokenizer(tmp_path):
    tmppath = tmp_path

    file_3x2 = tmppath / "1_2_3__4_5_6.txt"
    file_3x2.write_text("first second third\n4 5 6\n")
    file_1x3 = tmppath / "1__2__3.txt"
    file_1x3.write_text("first\n second\n third")

    assert universal_file_counter(tmppath, "txt", str.split) == 9


def test_without_files(tmp_path):
    tmppath = tmp_path

    assert universal_file_counter(tmppath, "txt", str.split) == 0


def test_file_in_subfolder(tmp_path):
    tmppath = tmp_path / "sub"
    tmppath.mkdir()
    file_3x2 = tmppath / "1_2_3__4_5_6.txt"
    file_3x2.write_text("first second third\n4 5 6\n")

    assert universal_file_counter(tmp_path, "txt") == 2
