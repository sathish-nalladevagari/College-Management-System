from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
m=0
counts=0
dg={}
def home(request):
    return render(request,"a.html")
def reg(request):
    d=rw()
    if request.method=="POST":
        t=request.POST["name"]
        y=request.POST["email"]
        u=request.POST["password"]
        c=request.POST["rollno"]
        b=request.POST["BRANCH"]
        ys=request.POST["year"]
        ree=request.POST["regulation"]
        q=User.objects.create_user(username=c,email=y,password=u)
        l=regis(name=t,rollno=c,email=y,password=u,BRANCH=b,regulation=ree,year=ys)
        l.save()
        q.save()
        return redirect("accounts/login")
    return render(request,"b.html",{"d":d})
def homes(request):
    sm=0
    qa=teach.objects.all().values_list()
    for i in qa:
        print(request.user.username)
        if request.user.username in i:
            sm=1
            print(sm)
    if sm==1:
        aq=keys.objects.all()
        az=score.objects.all().values_list()
        az=list(az)
        print(az)
        xq=[]
        kel=[]
        cor=[]
        kl=[]
        for i in az:
            if request.user.username in i:
                print("d,j")
                xq.append(i[0])
                kel.append(i[3])
                cor.append(i[1])
        for i in az:
            qa=i[1]
            i=list(i)
            i.pop(0)
            i.insert(0,qa)
            print(i)
            kl.append(i)
        kl.sort()
        #print(kl)
        #print(az)
        mnb=3
        if len(kl)<=mnb:
            mnb=len(kl)
        for i in range(0,len(kl)):
            xq.append(kl[i][2])
        #print(aq)
        f=list(aq)
        #print("f=================================",f)
        #print("kel=====================",kel)
        return render(request,"c.html",{"f":f,"xq":xq,"kel":kel})
    else:
        aq=keys.objects.all()
        az=score.objects.all().values_list()
        az=list(az)
        print(az)
        xq=[]
        kel=[]
        cor=[]
        kl=[]
        for i in az:
            if request.user.username in i:
                print("d,j")
                xq.append(i[0])
                kel.append(i[3])
                cor.append(i[1])
        for i in az:
            qa=i[1]
            i=list(i)
            i.pop(0)
            i.insert(0,qa)
            print(i)
            kl.append(i)
        kl.sort()
        print(kl)
        print(az)
        mnb=3
        if len(kl)<=mnb:
            mnb=len(kl)
        for i in range(0,len(kl)):
            xq.append(kl[i][2])
        print(aq)
        f=list(aq)
        #print("f=================================",f)
        #print("kel=====================",kel)
        #return render(request,"c.html")
        return render(request,"s.html",{"f":f,"xq":xq,"kel":kel})
def create(request):
    h=k()
    if request.method=="POST":
        g=request.POST["key"]
        s=request.POST["subject"]
        re=request.POST["regulation"]
        y=request.POST["year"]
        b=request.POST["branch"]
        #l=request.POST["j"]
        print(g)
        o=keys.objects.all().values_list()
        r=list(o)
        print(r)
        for i in r:
            if g in i:
                o=1
            else:
                o=0
        #print(o)
        if o:
            return redirect("create")
        else:
            u=keys(key=g,subject=s,year=y,regulation=re,branch=b)
            u.save()
           # print("data saved")
            return redirect("t", g=g)
    return render(request,"d.html",{"h":h})
def t(request,g):
#    print(g)
    w=questions.objects.filter(key=g)
#    print(w)
    n=quest()
    if request.method=="POST":
        a=request.POST["question"]
        s=request.POST["question1"]
        d=request.POST["question2"]
        f=request.POST["question3"]
        gn=request.POST["question4"]
        h=request.POST["answer"]
        z=questions(question=a,question1=s,question2=d,question3=f,question4=gn,answer=h,key=g)
        z.save()
        return redirect("t", g=g)
    return render(request,"e.html",{'n':n,"w":w,"g":g})
def update(request,g,pk):
    f=questions.objects.filter(id=pk).first()
    print(f)
    o=quest(instance=f)
    if request.method=="POST":
        a=request.POST["question"]
        s=request.POST["question1"]
        d=request.POST["question2"]
        f=request.POST["question3"]
        gn=request.POST["question4"]
        h=request.POST["answer"]
        questions.objects.filter(id=pk).update(question=a,question1=s,question2=d,question3=f,question4=gn,answer=h,key=g)
        return redirect("t", g=g)
    return render(request,"t.html",{"form":o,"g":g})
def dele(request,g,pk):
    f=questions.objects.filter(id=pk)
    f.delete()
    return redirect("t",g=g)
def delete(request,p):
    print(p)
    f=keys.objects.filter(id=p)
    g=questions.objects.all().values_list()
    print(g)
    print(f)
    f.delete()
    #print("deleted")
    g=questions.objects.all().values_list()
    print(g)
    l=[]
    for i in g:
        w=i[len(l)-1]
        print(w)
        s=i[0]
        if w==p:
            r=questions.objects.filter(pk=s)
            print(r)
            r.delete()
    return redirect("homes")
def r(request):
    return redirect("/homes")
def par(request):
    if request.method=="POST":
        g=request.POST["ke"]
        qw=regis.objects.filter(rollno=request.user.username).values_list()
        qw=(list(qw))
        o=keys.objects.all().values_list()
        r=list(o)
        print(r)
        for i in r:
            if (g in i and qw[0][4] in i and qw[0][5] in i and qw[0][6] in i):
                o=1
            else:
                o=0
        print(o)
        if o:
            return redirect("quiz", g=g)
        else:
            return redirect("par")

    return render(request,"z.html")

def quiz(request,g):
    l=[]
    print("inquiz")
    global m
    global counts
    print(m,counts)
    f=questions.objects.all().values_list()
    print(f)
    c=[]
    for i in f:
        if g in i:
            c.append(i[0])
    print(c)
    for i in f:
        if g in i and len(c)-1>=m:
            s=questions.objects.filter(id=c[m])
            qw=s.values_list()
            #print(qw[0])
            acd=qw[0][6]
            m+=1
            return render(request,"y.html",{"s":qw[0][1],"d":qw[0][2],"l":qw[0][3],"k":qw[0][4],"j":qw[0][5],"g":g,"acd":acd})

    print(m,counts)
    das=score(se=counts,name=request.user.username,participated=g)
    das.save()
    print(das)
    print("quiz completed")
    m=0
    counts=0
    print(m,counts)
    return redirect("homes")
def analyse(request,g,acd):
    global counts
    if request.method=="POST":
                xc=request.POST["name"]
                xc=xc.lower()
                if xc==acd:
                    counts+=1
                    print("counts"+str(counts))
                return redirect(quiz, g=g)
def u(request,i):
    qa=keys.objects.filter(id=i).values_list()
    pr=(qa[0][1])
    h=questions.objects.all().values_list()
    l=[]
    for s in h:
        if pr in s:
            s="question  :"+s[1]+'  =======  '+"option1    :"+s[2]+"   =====   "+"option2    :"+s[3]+'   ====    '+"option3     :"+s[4]+"option4     :"+s[5]+'   ====   '+"answer     :"+s[6]
            l.append(s)
    return render(request,"q.html",{"f":l})
def sees(request,xq):
    print(xq)
    xq=xq[1:len(xq)-1]
    xq=xq.split(",")
    print(xq[0])
    if len(xq)<5:
        g="there are no enough participants to dispaly leader board"
    else:
        g="the first position is by"+str(xq[len(xq)-1])+"the second position is "+str(xq[len(xq)-2])+"the last position is"+str(xq[len(xq)-3])

    return render(request,"x.html",{"a":xq[0],"s":xq[len(xq)-1],"g":g})
def profile(request):
    r=regis.objects.filter(rollno=request.user.username)
    #print(r)
    h=r.values_list()
    print(h)
    return render(request,"p.html",{"n":h[0][1],"e":h[0][2],"r":h[0][3],"y":h[0][4],"re":h[0][5],"b":h[0][6]})
def assignment(request):
    t=assignments.objects.all().values_list()
    q=[]
    r=regis.objects.filter(rollno=request.user.username)
    print(r)
    h=r.values_list()
    print(h)
    for i in t:
        if (h[0][6] in i) and (h[0][5] in i) and (h[0][4] in i):
            q.append(i[5])
    print(q)
    return render(request,"re.html",{"q":q})
def uo(request):
    es=e()
    #print(es)
    if request.method=="POST":
        s=request.POST["subject"]
        t=request.POST["teacher"]
        f=request.POST["file"]
        print(s,t,f)
        g=Form(subject=s,teacher=t,file=f,student=request.user.username)
        g.save()
        return redirect("/assignments")
    return render(request,"ts.html",{'form':es})
def fees(request):
    return redirect("/homes")
def attendance(request):
    h=n()
    if request.method=="POST":
        s=request.POST["subject"]
        y=request.POST["year"]
        r=request.POST["regulation"]
        b=request.POST["branch"]
        d=request.POST["date"]
        return redirect("/uohomes")
    return render(request,"index.html",{"h":h})
def c(request):
    u=do()
    if request.method=="POST":
        t=request.POST["teacher_id"]
        s=request.POST["subject"]
        d=request.POST['doubt']
        h=doubt.objects.create(teacher_id=t,subject=s,doubt=d,student=request.user.username)
        h.save()
        return redirect("/homes")
    return render(request,"dx.html",{"u":u})
def myc(request):
    h=teach.objects.all().values_list()
    m=doubt.objects.all().values_list()
    z=""
    for i in h:
        if request.user.username in i:
            z=i
    id=z[3]
    print(id,z)
    p=[]
    for i in m:
        if id in i:
            p.append(i)
    print(p)
    return render(request,"kjg.html",{"p":p})
def fr(request,i):
    print(i)
    return HTTPResponse("hello")
def answer(request,ip):
    u=ip.split(",")
    print(u[3])
    b="http://127.0.0.1:8000/media/"+u[3][2:len(u[3])-1]
    #print(b)
    return redirect(b)
def mya(request):
    h=teach.objects.all().values_list()
    m=Form.objects.all().values_list()
    z=""
    for i in h:
        if request.user.username in i:
            z=i
    id=z[3]
    p=[]
    for i in m:
        if id in i:
            p.append(i)
    return render(request,"kj.html",{"p":p})
def asa(request):
    m=d()
    print(m)
    if request.method=="POST":
        s=request.POST["subject"]
        b=request.POST["branch"]
        y=request.POST['year']
        r=request.POST["regulation"]
        q=request.POST["question"]
        l=assignments(subject=s,branch=b,year=y,regulation=r,question=q)
        l.save()
        qw=regis.objects.all().values_list()
        k=[]
        for i in qw:
            if b in i and (y in i and r in i):
                k.append(i[2])
        print(k)
        for i in k:
            email=EmailMessage("A NEW ASSIGNMENT IS ASSIGNED","the subject is   -->"+s,settings.EMAIL_HOST_USER,[i],)
            email.fail_silently=False
            email.send()
        return redirect("/uohomes")
    return render(request,"ts.html",{"form":m})