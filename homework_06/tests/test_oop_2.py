import pytest

from homework_06.oop_2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    Programmist,
    Student,
    Teacher,
)

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")


@pytest.fixture(scope="function")
def create_hw():
    yield opp_teacher.create_homework("Learn OOP", 1)


@pytest.fixture(scope="function")
def clean_homework_done():
    yield
    Teacher.reset_results()


def test_creating_people():
    assert opp_teacher.first_name, opp_teacher.last_name == (
        "Daniil",
        "Shadrin",
    )


def test_people_are_people():
    assert isinstance(opp_teacher, Programmist and Teacher)
    assert isinstance(good_student, Programmist and Student)


def test_creating_homework(create_hw):
    assert isinstance(create_hw, Homework)


def test_exception_not_homework():
    not_hw = "not_hw"
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(lazy_student, not_hw, "result")


def test_doing_homework_before_deadline(create_hw):
    expected_result = lazy_student.do_homework(create_hw, "I did it")
    assert isinstance(expected_result, HomeworkResult)


def test_doing_homework_after_deadline():
    impossible_hw = opp_teacher.create_homework("Not today", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(impossible_hw, "I did it")


def test_done_homework_list_cleaning(create_hw):
    good_result = good_student.do_homework(create_hw, "I have done this hw too")
    opp_teacher.check_homework(good_result)
    assert len(Teacher.homework_done) == 1
    Teacher.reset_results()
    assert Teacher.homework_done == {}


def test_check_good_homework(create_hw, clean_homework_done):
    good_result = good_student.do_homework(create_hw, "I have done this hw too")
    assert opp_teacher.check_homework(good_result)


def test_check_bad_homework(create_hw):
    bad_result = lazy_student.do_homework(create_hw, "done")
    assert not opp_teacher.check_homework(bad_result)


def test_done_homework_list_after_checking_bad_hw(create_hw):
    bad_result = lazy_student.do_homework(create_hw, "done")
    assert Teacher.homework_done[bad_result] == []


def test_done_homework_list_after_checking_good_hw(create_hw, clean_homework_done):
    good_result = good_student.do_homework(create_hw, "I have done this hw too")
    opp_teacher.check_homework(good_result)
    assert Teacher.homework_done["Learn OOP"] == ["I have done this hw too"]


def test_done_homework_list_cleaning_some_result(create_hw, clean_homework_done):
    one_more_hw = opp_teacher.create_homework("Just delete it", 5)

    good_result = good_student.do_homework(create_hw, "I have done this hw too")
    one_more_result = lazy_student.do_homework(one_more_hw, "one more solution")

    opp_teacher.check_homework(good_result)
    opp_teacher.check_homework(one_more_result)

    Teacher.reset_results(one_more_hw)
    assert Teacher.homework_done[good_result.homework.hw_text] == [
        "I have done this hw too"
    ]
    assert Teacher.homework_done[one_more_result.homework.hw_text] == []


def test_checking_by_different_teachers(create_hw, clean_homework_done):
    good_result = good_student.do_homework(create_hw, "I have done this hw too")

    opp_teacher.check_homework(good_result)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(good_result)
    temp_2 = advanced_python_teacher.homework_done

    assert temp_1 == temp_2 == Teacher.homework_done
