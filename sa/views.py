from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
# Create your views here.

def base(request):
    return render(request,'login.html')

def lr(request):
    return render(request,'log_reg.html')

def login(request):
    return render(request,'dologin.html')

def log(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request,'combination.html')
    else:
        messages.info(request,'Error')
    return render(request,'dologin.html')

def reg(request):
    return render(request,'reg.html')

def areg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1= request.POST['password1']
        password2 = request.POST['password2']

    if password1==password2:
        if User.objects.filter(username=username).exists():
            messages.info(request,'User Taken')
            return render(request,'reg.html')
            return
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return render(request,'reg.html')
        else:
            user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
            user.save();
            messages.info(request,'User created succesfully')
            return render(request,'dologin.html')
    else:
        messages.info(request,'Password does not match')
        return render(request,'reg.html')

    return render(request,'dologin.html')

def generate(request):
    dep,date,sub1,sub2,sub3,time,sSEA,sSEB,sTEA,sTEB,sBEA,sBEB = request.POST['dep'],request.POST['date'],request.POST['subject1'],request.POST['subject2'],request.POST['subject3'],request.POST['time'],int(request.POST['sSEA']),int(request.POST['sSEB']),int(request.POST['sTEA']),int(request.POST['sTEB']),int(request.POST['sBEA']),int(request.POST['sBEB'])
    l1,l2,l3,l4,l5,l6,l7,l8,l9=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6'],request.POST['l7'],request.POST['l8'],request.POST['l9']
    s1,s2,s3,s4,s5,s6,s7,s8,s9=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6'],request.POST['s7'],request.POST['s8'],request.POST['s9']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12'],request.POST['m13'],request.POST['m14'],request.POST['m15']

    teach = [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15]
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =     teach[10];t12 = teach[11];t13 = teach[12];t14 = teach[13];t15 = teach[14];t16 =teach[15];t17 = teach[16];t18 = teach[17]
    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18]

    if sSEA>=35:sa1='1-35'
    if sSEA>=70:sa2='36-70'
    else:sa2='36-'+ str(sSEA)
    if sSEA>70:sa3='71-'+ str(sSEA)
    else:sa3='null'
    if sSEB>=35:sb1='1-35'
    if sSEB>=70:sb2='36-70'
    else:sb2='36-'+ str(sSEB)
    if sSEB>70:sb3='71-'+ str(sSEB)
    else:sb3='null'
    if sTEA>=35:ta1='1-35'
    if sTEA>=70:ta2='36-70'
    else:ta2='36-'+ str(sTEA)
    if sTEA>70:ta3='71-'+ str(sTEA)
    else:ta3='null'
    if sTEB>=35:tb1='1-35'
    if sTEB>=70:tb2='36-70'
    else:tb2='36-'+ str(sTEB)
    if sTEB>70:tb3='71-'+ str(sTEB)
    else:tb3='null'
    if sBEA>=35:ba1='1-35'
    if sBEA>=70:ba2='36-70'
    else:ba2='36-'+ str(sBEA)
    if sBEA>70:ba3='71-'+ str(sBEA)
    else:ba3='null'
    if sBEB>=35:bb1='1-35'
    if sBEB>=70:bb2='36-70'
    else:bb2='36-'+ str(sBEB)
    if sBEB>70:bb3='71-'+ str(sBEB)
    else:bb3='null'
    a=[sa1,sa2,sa3]
    random.shuffle(a)
    sa1=a[0];sa2=a[1];sa3=a[2]
    b=[sb1,sb2,sb3]
    random.shuffle(b)
    sb1=b[0];sb2=b[1];sb3=b[2]
    c=[ta1,ta2,ta3]
    random.shuffle(c)
    ta1=c[0];ta2=c[1];ta3=c[2]
    d=[tb1,tb2,tb3]
    random.shuffle(d)
    tb1=d[0];tb2=d[1];tb3=d[2]
    e=[ba1,ba2,ba3]
    random.shuffle(e)
    ba1=e[0];ba2=e[1];ba3=e[2]
    f=[bb1,bb2,bb3]
    random.shuffle(f)
    bb1=f[0];bb2=f[1];bb3=f[2]

    s=[l1,l2,l3,l4,l5,l6,l7,l8,l9]
    random.shuffle(s)
    cr1=s[0];cr2=s[1];cr3=s[2];cr4=s[3];cr5=s[4];cr6=s[5];cr7=s[6];cr8=s[7];cr9=s[8]
    div = ['A','B']
    random.shuffle(div)
    div0 = div[0];div1 = div[1]

    ### write your logic here ###
    return render(request,'result1.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0})


def generate2(request):
    dep,date,sub1,sub2,time,sSEA,sSEB,sTEA,sTEB = request.POST['dep'],request.POST['date'],request.POST['subject1'],request.POST['subject2'],request.POST['time'],int(request.POST['sSEA']),int(request.POST['sSEB']),int(request.POST['sTEA']),int(request.POST['sTEB'])
    l1,l2,l3,l4,l5,l6=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6']
    s1,s2,s3,s4,s5,s6=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12']

    teach = [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =     teach[10];t12 = teach[11]
    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]

    if sSEA>=35:sa1='1-35'
    if sSEA>=70:sa2='36-70'
    else:sa2='36-'+ str(sSEA)
    if sSEA>70:sa3='71-'+ str(sSEA)
    else:sa3='null'
    if sSEB>=35:sb1='1-35'
    if sSEB>=70:sb2='36-70'
    else:sb2='36-'+ str(sSEB)
    if sSEB>70:sb3='71-'+ str(sSEB)
    else:sb3='null'
    if sTEA>=35:ta1='1-35'
    if sTEA>=70:ta2='36-70'
    else:ta2='36-'+ str(sTEA)
    if sTEA>70:ta3='71-'+ str(sTEA)
    else:ta3='null'
    if sTEB>=35:tb1='1-35'
    if sTEB>=70:tb2='36-70'
    else:tb2='36-'+ str(sTEB)
    if sTEB>70:tb3='71-'+ str(sTEB)
    else:tb3='null'

    a=[sa1,sa2,sa3]
    random.shuffle(a)
    sa1=a[0];sa2=a[1];sa3=a[2]
    b=[sb1,sb2,sb3]
    random.shuffle(b)
    sb1=b[0];sb2=b[1];sb3=b[2]
    c=[ta1,ta2,ta3]
    random.shuffle(c)
    ta1=c[0];ta2=c[1];ta3=c[2]
    d=[tb1,tb2,tb3]
    random.shuffle(d)
    tb1=d[0];tb2=d[1];tb3=d[2]

    s=[l1,l2,l3,l4,l5,l6]
    random.shuffle(s)
    cr1=s[0];cr2=s[1];cr3=s[2];cr4=s[3];cr5=s[4];cr6=s[5]
    div = ['A','B']
    random.shuffle(div)
    div0 = div[0];div1 = div[1]

    ### write your logic here ###
    return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'div1':div1,'div0':div0})

def generate3(request):
    dep,date,sub1,sub3,time,sSEA,sSEB,sBEA,sBEB = request.POST['dep'],request.POST['date'],request.POST['subject1'],request.POST['subject3'],request.POST['time'],int(request.POST['sSEA']),int(request.POST['sSEB']),int(request.POST['sBEA']),int(request.POST['sBEB'])
    l1,l2,l3,l4,l5,l6=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6']
    s1,s2,s3,s4,s5,s6=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12']

    teach = [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =     teach[10];t12 = teach[11]
    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]

    if sSEA>=35:sa1='1-35'
    if sSEA>=70:sa2='36-70'
    else:sa2='36-'+ str(sSEA)
    if sSEA>70:sa3='71-'+ str(sSEA)
    else:sa3='null'
    if sSEB>=35:sb1='1-35'
    if sSEB>=70:sb2='36-70'
    else:sb2='36-'+ str(sSEB)
    if sSEB>70:sb3='71-'+ str(sSEB)
    else:sb3='null'
    if sBEA>=35:ba1='1-35'
    if sBEA>=70:ba2='36-70'
    else:ba2='36-'+ str(sBEA)
    if sBEA>70:ba3='71-'+ str(sBEA)
    else:ba3='null'
    if sBEB>=35:bb1='1-35'
    if sBEB>=70:bb2='36-70'
    else:bb2='36-'+ str(sBEB)
    if sBEB>70:bb3='71-'+ str(sBEB)
    else:bb3='null'

    a=[sa1,sa2,sa3]
    random.shuffle(a)
    sa1=a[0];sa2=a[1];sa3=a[2]
    b=[sb1,sb2,sb3]
    random.shuffle(b)
    sb1=b[0];sb2=b[1];sb3=b[2]
    c=[ba1,ba2,ba3]
    random.shuffle(c)
    ba1=c[0];ba2=c[1];ba3=c[2]
    d=[bb1,bb2,bb3]
    random.shuffle(d)
    bb1=d[0];bb2=d[1];bb3=d[2]

    s=[l1,l2,l3,l4,l5,l6]
    random.shuffle(s)
    cr1=s[0];cr2=s[1];cr3=s[2];cr4=s[3];cr5=s[4];cr6=s[5]
    div = ['A','B']
    random.shuffle(div)
    div0 = div[0];div1 = div[1]

    ### write your logic here ###
    return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'div1':div1,'div0':div0})

def generate4(request):
    dep,date,sub3,sub2,time,sBEA,sBEB,sTEA,sTEB = request.POST['dep'],request.POST['date'],request.POST['subject3'],request.POST['subject2'],request.POST['time'],int(request.POST['sBEA']),int(request.POST['sBEB']),int(request.POST['sTEA']),int(request.POST['sTEB'])
    l1,l2,l3,l4,l5,l6=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6']
    s1,s2,s3,s4,s5,s6=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12']

    teach = [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =     teach[10];t12 = teach[11]
    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]

    if sBEA>=35:ba1='1-35'
    if sBEA>=70:ba2='36-70'
    else:ba2='36-'+ str(sBEA)
    if sBEA>70:ba3='71-'+ str(sBEA)
    else:ba3='null'
    if sBEB>=35:bb1='1-35'
    if sBEB>=70:bb2='36-70'
    else:bb2='36-'+ str(sBEB)
    if sBEB>70:bb3='71-'+ str(sBEB)
    else:bb3='null'
    if sTEA>=35:ta1='1-35'
    if sTEA>=70:ta2='36-70'
    else:ta2='36-'+ str(sTEA)
    if sTEA>70:ta3='71-'+ str(sTEA)
    else:ta3='null'
    if sTEB>=35:tb1='1-35'
    if sTEB>=70:tb2='36-70'
    else:tb2='36-'+ str(sTEB)
    if sTEB>70:tb3='71-'+ str(sTEB)
    else:tb3='null'

    a=[ba1,ba2,ba3]
    random.shuffle(a)
    ba1=a[0];ba2=a[1];ba3=a[2]
    b=[bb1,bb2,bb3]
    random.shuffle(b)
    bb1=b[0];bb2=b[1];bb3=b[2]
    c=[ta1,ta2,ta3]
    random.shuffle(c)
    ta1=c[0];ta2=c[1];ta3=c[2]
    d=[tb1,tb2,tb3]
    random.shuffle(d)
    tb1=d[0];tb2=d[1];tb3=d[2]

    s=[l1,l2,l3,l4,l5,l6]
    random.shuffle(s)
    cr1=s[0];cr2=s[1];cr3=s[2];cr4=s[3];cr5=s[4];cr6=s[5]
    div = ['A','B']
    random.shuffle(div)
    div0 = div[0];div1 = div[1]

    ### write your logic here ###
    return render(request,'result4.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub3':sub3,'sub2':sub2,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'div1':div1,'div0':div0})



def combination(request):
    if request.method == 'POST':
        comb = request.POST['com1']
    if comb == 'SE,TE,BE':
        return render(request,'logedin1.html')
    if comb == 'SE,TE':
        return render(request,'logedin2.html')
    if comb == 'SE,BE':
        return render(request,'logedin3.html')
    if comb == 'TE,BE':
        return render(request,'logedin4.html')


    return render(request,'logedin1.html',{'comb':comb})


def logout(request):
    return render(request,'login.html')
