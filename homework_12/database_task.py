from django.db import models


class Programmist:
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)


class Teacher(Programmist, models.Model):

    # homework_done = defaultdict(list)

    def __str__(self):
        return self.name


class Student(Programmist, models.Model):
    def __str__(self):
        return self.name


class Homework(models.Model):
    hw_text = models.CharField(max_length=200)
    deadline = models.FloatField()  # datetime.timedelta(days=deadline)
    created = models.IntegerField(null=True)  # datetime.datetime.now()
    answer = models.CharField(max_length=200)  # maybe more

    def __str__(self):
        return self.hw_text


class HomeworkResult:
    # if not isinstance(homework, Homework):
    #     raise TypeError("You gave a not Homework object")
    homework = models.CharField(max_length=200)
    solution = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created = models.CharField(max_length=200)  # maybe not Char


"""
class Student(Programmist):     # done
    def do_homework(self, homework, solution):
        if homework.is_active():
            homework.solution = str(solution)
            return HomeworkResult(self, homework, homework.solution)
        raise DeadlineError("You are late")


class Teacher(Programmist): # done
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(hw_text, deadline):
        return Homework(hw_text, deadline, None)

    @staticmethod
    def check_homework(homework_result):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework.hw_text].append(
                homework_result.solution
            )
            return True
        return False

    @staticmethod
    def reset_results(homework=None):
        if homework:
            Teacher.homework_done.__delitem__(homework.hw_text)
        else:
            Teacher.homework_done.clear()


class Homework:
    def __init__(self, hw_text, deadline, answer):
        self.hw_text = hw_text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()
        self.answer = answer

    def is_active(self):
        time = datetime.datetime.today()
        if time - self.created >= self.deadline:
            return False
        return True


class HomeworkResult:
    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = homework.created
"""
