from ast import Try
from operator import le
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, datetime, timedelta
# Create your views here.

def sort_lesson(lessons, days):
    for i in days:
        temp = []
        for y in range(7):
            costil_nomer_789789789789 = False
            timer = 0
            for q in lessons[i[1:]]:
                try:
                    # print(q.number_lesson, q, str(y+1))
                    if q.number_lesson == str(y+1):
                        temp.append(lessons[i[1:]][timer]) 
                        costil_nomer_789789789789 = True
                        break
                    else:
                        raise Exception
                
                except Exception as Err:
                    pass
                timer += 1
            if not costil_nomer_789789789789:
                temp.append(1)
        lessons[i[1:]] = temp
    return lessons

def index(request):
    data = request.POST
    try:
        teacher = data['by_teacher']
        return redirect('by_teacher', teacher = teacher)

    except Exception as E:
        try:
            clas = data['by_class']
            return redirect('by_class', clas = clas)
        except Exception as E:
            pass
    return render(request, 'main/index.html')

def by_class(request, clas):
    
    days = ["1Понедельник",
            "2Вторник",
            "3Среда",
            "4Четверг",
            "5Пятница"]

    lessons = Lesson.objects.filter(classroom = Class.objects.get(class_name=clas)).order_by('day', 'number_lesson')
    lessons_sorted = {}
    zamenas = Zamena.objects.all()
    
    
    for i in days:  
        temp = list(lessons.filter(day = i))
        lessons_sorted[i[1:]]= temp
    
    datelist = []
    if datetime.now().weekday() in [5,6]:
        now_day_1 = now_day_1 = datetime.now() - timedelta(days=datetime.now().weekday()-7)
    else:
            now_day_1 = datetime.now() - timedelta(days=datetime.now().weekday())
    for i in range(5):
        day = now_day_1 + timedelta(days=i)
        datelist.append(day.strftime('%Y-%m-%d'))

    for i in zamenas:
        if str(i.date) in datelist:
            for j in range(len(lessons)):
                if i.lesson == lessons[j]:
                    for q in range(len(lessons_sorted[lessons[j].day[1:]])):
                        if i.lesson == lessons_sorted[lessons[j].day[1:]][q]:
                            lessons_sorted[lessons[j].day[1:]][q].teacher = i.catch_up
    print(lessons_sorted)
    lessons_sorted = sort_lesson(lessons_sorted, days)
    context = {'clas':clas, 'lessons':lessons_sorted, 'class_or_teacher':True}
    return render(request, 'main/index.html', context)

def by_teacher(request, teacher):
    days = ["1Понедельник",
            "2Вторник",
            "3Среда",
            "4Четверг",
            "5Пятница"]

    lessons = Lesson.objects.filter(teacher = Teacher.objects.get(name=teacher)).order_by('day', 'number_lesson')
    lessons_sorted = {}
    zamenas = Zamena.objects.all()
    
    datelist = []
    if datetime.now().weekday() in [5,6]:
        now_day_1 = now_day_1 = datetime.now() - timedelta(days=datetime.now().weekday()-7)
    else:
        now_day_1 = datetime.now() - timedelta(days=datetime.now().weekday())
    for i in range(5):
        day = now_day_1 + timedelta(days=i)
        datelist.append(day.strftime('%Y-%m-%d'))
    s = None
    for i in zamenas:
        if i.catch_up == Teacher.objects.get(name=teacher):
            s = Lesson.objects.get(pk=i.lesson.pk)
    
    for i in days:
        zamena = False
        if s:
            try:
                if s.day == Lesson.objects.filter(day = i)[0].day:
                    temp = list(lessons.filter(day = i))
                    temp.append(s)
                    zamena = True
            except: 
                pass
        if not zamena:
            temp = list(lessons.filter(day = i))
        lessons_sorted[i[1:]]= temp
    for i in zamenas:
        if str(i.date) in datelist:
            for j in range(len(lessons)):
                if i.lesson == lessons[j]:
                    for q in range(len(lessons_sorted[lessons[j].day[1:]])):
                        if i.lesson == lessons_sorted[lessons[j].day[1:]][q]:
                            del lessons_sorted[lessons[j].day[1:]][q]
                            break
    lessons_sorted = sort_lesson(lessons_sorted, days)
    context = {'teacher':teacher, 'lessons':lessons_sorted, 'class_or_teacher':False}
    return render(request, 'main/index.html', context)
