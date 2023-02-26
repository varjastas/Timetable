from django.db import models
from django.shortcuts import redirect

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    cabinet = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'teachers'

class Lessons_list(models.Model):
    name_of_lesson = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_lesson

    class Meta:
        verbose_name_plural = 'lessons'

class Class(models.Model):
    class_name = models.CharField(max_length=5)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = 'Class'

class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    lesson_name = models.ForeignKey(Lessons_list, on_delete=models.CASCADE)
    day = models.CharField(max_length=15, choices=(
                ("1Понедельник", "Понедельник"),
                ("2Вторник", "Вторник"),
                ("3Среда", "Среда"),
                ("4Четверг", "Четверг"),
                ("5Пятница", "Пятница"),
            )
        )  
    number_lesson = models.CharField(max_length=1, choices=(
                ("1", "1"),
                ("2", "2"),
                ("3", "3"),
                ("4", "4"),
                ("5", "5"),
                ("6", "6"),
                ("7", "7")
            )
        )

    def __str__(self):
        return ' '.join([self.lesson_name.name_of_lesson, self.classroom.class_name, self.teacher.name, self.day[1:], self.number_lesson])

    class Meta:
        verbose_name_plural = 'lesson'
        unique_together = [['classroom', 'day', 'number_lesson'], ['teacher', 'day', 'number_lesson']]


class Zamena(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    catch_up = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self) -> str:
        return ' '.join([str(self.lesson), str(self.catch_up), str(self.date)])