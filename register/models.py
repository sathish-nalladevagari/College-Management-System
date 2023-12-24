from django import forms
from django.db import models
# Create your models here.
class regis(models.Model):
    class branch(models.TextChoices):
        CSE = 'CSE', ('COMPUTER SCIENCE AND ENGINEERING')
        CIV = 'CIV', ('CIVIL ENGINEERING')
        MECH = 'MECH', ('MECHANICAL ENGINEERING')
        ECE = 'ECE', ('ELECTRONICS AND COMMUNICATION ENGINEERING')
        EEE = 'EEE',('ELECTRICAL AND ELECTRONIC ENGINEERING')
    class years(models.TextChoices):
        I="I",("I ST YEAR")
        II="II",("II ND YEAR")
        III="III",("III RD YEAR")
        IV="IV",("IV TH YEAR")
    class r(models.TextChoices):
        r19="r19",("r19")
        r20="r20",("r20")
        r21="r21",("r21")
        r22="r22",("r22")
    name=models.CharField(max_length=20)
    email=models.EmailField()
    rollno=models.CharField(max_length=10)
    year=models.CharField(max_length=6,choices=years.choices,)
    regulation=models.CharField(max_length=6,choices=r.choices)
    BRANCH = models.CharField(
        max_length=6,
        choices=branch.choices,
    )
    password=models.CharField(max_length=20)
    def __str__(self):
        return"{0.name}{0.email}{0.year}{0.regulation}{0.branch}{0.password}".format(self)
class teach(models.Model):
    class branch(models.TextChoices):
        CSE = 'CSE', ('COMPUTER SCIENCE AND ENGINEERING')
        CIV = 'CIV', ('CIVIL ENGINEERING')
        MECH = 'MECH', ('MECHANICAL ENGINEERING')
        ECE = 'ECE', ('ELECTRONICS AND COMMUNICATION ENGINEERING')
        EEE = 'EEE',('ELECTRICAL AND ELECTRONIC ENGINEERING')
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dept_roll_id=models.CharField(max_length=10)
    #year=models.CharField(max_length=6,choices=years.choices,)
    #regulation=models.CharField(max_length=6,choices=r.choices)
    dept= models.CharField(
        max_length=6,
        choices=branch.choices,
    )
    password=models.CharField(max_length=20)
    def __str__(self):
        return"{0.name}{0.email}{0.dept}{0.password}".format(self)
class keys(models.Model):
    subject=models.CharField(max_length=20)
    class branchs(models.TextChoices):
        CSE = 'CSE', ('COMPUTER SCIENCE AND ENGINEERING')
        CIV = 'CIV', ('CIVIL ENGINEERING')
        MECH = 'MECH', ('MECHANICAL ENGINEERING')
        ECE = 'ECE', ('ELECTRONICS AND COMMUNICATION ENGINEERING')
        EEE = 'EEE',('ELECTRICAL AND ELECTRONIC ENGINEERING')
    class years(models.TextChoices):
        I="I",("I ST YEAR")
        II="II",("II ND YEAR")
        III="III",("III RD YEAR")
        IV="IV",("IV TH YEAR")
    class r(models.TextChoices):
        r19="r19",("r19")
        r20="r20",("r20")
        r21="r21",("r21")
        r22="r22",("r22")
    branch=models.TextField(choices=branchs.choices)
    year=models.CharField(max_length=6,choices=years.choices,)
    regulation=models.CharField(max_length=6,choices=r.choices)
    subject=models.CharField(max_length=35)
    key=models.CharField(max_length=6)
    def __str__(self):
        return "{0.subject}{0.branch}{0.year}{0.regulation}{0.key}".format(self)

class score(models.Model):
    se=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    participated=models.CharField(max_length=10)
    def __str__(self):
        return"{0.se}{0.name}{0.participated}".format(self)
class assignments(models.Model):
    subject=models.CharField(max_length=20)
    class branchs(models.TextChoices):
        CSE = 'CSE', ('COMPUTER SCIENCE AND ENGINEERING')
        CIV = 'CIV', ('CIVIL ENGINEERING')
        MECH = 'MECH', ('MECHANICAL ENGINEERING')
        ECE = 'ECE', ('ELECTRONICS AND COMMUNICATION ENGINEERING')
        EEE = 'EEE',('ELECTRICAL AND ELECTRONIC ENGINEERING')
    class years(models.TextChoices):
        I="I",("I ST YEAR")
        II="II",("II ND YEAR")
        III="III",("III RD YEAR")
        IV="IV",("IV TH YEAR")
    class r(models.TextChoices):
        r19="r19",("r19")
        r20="r20",("r20")
        r21="r21",("r21")
        r22="r22",("r22")
    branch=models.TextField(choices=branchs.choices)
    year=models.CharField(max_length=6,choices=years.choices,)
    regulation=models.CharField(max_length=6,choices=r.choices)
    question=models.CharField(max_length=35)
    def __str__(self):
        return "{0.subject}{0.branch}{0.year}{0.regulation}{0.question}".format(self)
class Form(models.Model):
    subject=models.CharField(max_length=15)
    teacher=models.CharField(max_length=7)
    file = models.FileField(null=True)
    student=models.CharField(max_length=15)
    def __str__(self):
        return '{0.subject}{0.file}{0.teacher}{0.student}'.format(self)
class questions(models.Model):
    question=models.CharField(max_length=20)
    question1=models.CharField(max_length=20)
    question2=models.CharField(max_length=20)
    question3=models.CharField(max_length=20)
    question4=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)
    key=models.CharField(max_length=10)
    def __str__(self):
        return"{0.question}{0.question1}{0.question2}{0.question3}{0.question4}{0.answer}{0.key}".format(self)
class doubt(models.Model):
    teacher_id=models.CharField(max_length=6)
    subject=models.CharField(max_length=25)
    doubt=models.CharField(max_length=90)
    student=models.CharField(max_length=20)
    def __str__(self):
        return"{0.teacher_id}{0.subject}{0.doubt}{0.student}".format(self)
class co(models.Model):
    subject=models.CharField(max_length=20)
    class branchs(models.TextChoices):
        CSE = 'CSE', ('COMPUTER SCIENCE AND ENGINEERING')
        CIV = 'CIV', ('CIVIL ENGINEERING')
        MECH = 'MECH', ('MECHANICAL ENGINEERING')
        ECE = 'ECE', ('ELECTRONICS AND COMMUNICATION ENGINEERING')
        EEE = 'EEE',('ELECTRICAL AND ELECTRONIC ENGINEERING')
    class years(models.TextChoices):
        I="I",("I ST YEAR")
        II="II",("II ND YEAR")
        III="III",("III RD YEAR")
        IV="IV",("IV TH YEAR")
    class r(models.TextChoices):
        r19="r19",("r19")
        r20="r20",("r20")
        r21="r21",("r21")
        r22="r22",("r22")
    branch=models.TextField(choices=branchs.choices)
    year=models.CharField(max_length=6,choices=years.choices,)
    regulation=models.CharField(max_length=6,choices=r.choices)
    subject=models.CharField(max_length=35)
    date=models.DateTimeField()
    #key=models.CharField(max_length=6)
    def __str__(self):
        return "{0.subject}{0.branch}{0.year}{0.regulation}{0.date}".format(self)














