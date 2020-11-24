from homework_04.task_3_get_print_output import my_precious_logger


def test_positive_out(capsys):
    my_precious_logger("cheburek")
    captured = capsys.readouterr()
    assert captured.out == "cheburek"
    assert captured.err == ""


def test_positive_err(capsys):
    my_precious_logger("error:cheburek has a salmonella")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "error:cheburek has a salmonella"
