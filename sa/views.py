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
    eo,unit=request.POST['eo'],request.POST['unit']
    dep,date,sub1,sub2,sub3,time,sSEA,sSEB,sTEA,sTEB,sBEA,sBEB = request.POST['dep'],request.POST['date'],request.POST['subject1'],request.POST['subject2'],request.POST['subject3'],request.POST['time'],int(request.POST['sSEA']),int(request.POST['sSEB']),int(request.POST['sTEA']),int(request.POST['sTEB']),int(request.POST['sBEA']),int(request.POST['sBEB'])
    l1,l2,l3,l4,l5,l6,l7,l8,l9=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6'],request.POST['l7'],request.POST['l8'],request.POST['l9']
    s1,s2,s3,s4,s5,s6,s7,s8,s9=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6'],request.POST['s7'],request.POST['s8'],request.POST['s9']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12'],request.POST['m13'],request.POST['m14'],request.POST['m15']
    num=int(request.POST['num'])

    if num >= 2 :
        date2,sub12,sub22,sub32,time2 = request.POST['date2'],request.POST['subject12'],request.POST['subject22'],request.POST['subject32'],request.POST['time2']
        l12,l22,l32,l42,l52,l62,l72,l82,l92=request.POST['l12'],request.POST['l22'],request.POST['l32'],request.POST['l42'],request.POST['l52'],request.POST['l62'],request.POST['l72'],request.POST['l82'],request.POST['l92']
        s22=[l12,l22,l32,l42,l52,l62,l72,l82,l92]
        random.shuffle(s22)
        cr12=s22[0];cr22=s22[1];cr32=s22[2];cr42=s22[3];cr52=s22[4];cr62=s22[5];cr72=s22[6];cr82=s22[7];cr92=s22[8]
        if num >= 3 :
            date3,sub13,sub23,sub33,time3 = request.POST['date3'],request.POST['subject13'],request.POST['subject23'],request.POST['subject33'],request.POST['time3']
            l13,l23,l33,l43,l53,l63,l73,l83,l93=request.POST['l13'],request.POST['l23'],request.POST['l33'],request.POST['l43'],request.POST['l53'],request.POST['l63'],request.POST['l73'],request.POST['l83'],request.POST['l93']
            s33=[l13,l23,l33,l43,l53,l63,l73,l83,l93]
            random.shuffle(s33)
            cr13=s33[0];cr23=s33[1];cr33=s33[2];cr43=s33[3];cr53=s33[4];cr63=s33[5];cr73=s33[6];cr83=s33[7];cr93=s33[8]
            if num >= 4 :
                date4,sub14,sub24,sub34,time4 = request.POST['date4'],request.POST['subject14'],request.POST['subject24'],request.POST['subject34'],request.POST['time4']
                l14,l24,l34,l44,l54,l64,l74,l84,l94=request.POST['l14'],request.POST['l24'],request.POST['l34'],request.POST['l44'],request.POST['l54'],request.POST['l64'],request.POST['l74'],request.POST['l84'],request.POST['l94']
                s44=[l14,l24,l34,l44,l54,l64,l74,l84,l94]
                random.shuffle(s44)
                cr14=s44[0];cr24=s44[1];cr34=s44[2];cr44=s44[3];cr54=s44[4];cr64=s44[5];cr74=s44[6];cr84=s44[7];cr94=s44[8]
                if num >= 5 :
                    date5,sub15,sub25,sub35,time5 = request.POST['date5'],request.POST['subject15'],request.POST['subject25'],request.POST['subject35'],request.POST['time5']
                    l15,l25,l35,l45,l55,l65,l75,l85,l95=request.POST['l15'],request.POST['l25'],request.POST['l35'],request.POST['l45'],request.POST['l55'],request.POST['l65'],request.POST['l75'],request.POST['l85'],request.POST['l95']
                    s55=[l15,l25,l35,l45,l55,l65,l75,l85,l95]
                    random.shuffle(s55)
                    cr15=s55[0];cr25=s55[1];cr35=s55[2];cr45=s55[3];cr55=s55[4];cr65=s55[5];cr75=s55[6];cr85=s55[7];cr95=s55[8]
                    if num >= 6 :
                        date6,sub16,sub26,sub36,time6 = request.POST['date6'],request.POST['subject16'],request.POST['subject26'],request.POST['subject36'],request.POST['time6']
                        l16,l26,l36,l46,l56,l66,l76,l86,l96=request.POST['l16'],request.POST['l26'],request.POST['l36'],request.POST['l46'],request.POST['l56'],request.POST['l66'],request.POST['l76'],request.POST['l86'],request.POST['l96']
                        s66=[l16,l26,l36,l46,l56,l66,l76,l86,l96]
                        random.shuffle(s66)
                        cr16=s66[0];cr26=s66[1];cr36=s66[2];cr46=s66[3];cr56=s66[4];cr66=s66[5];cr76=s66[6];cr86=s66[7];cr96=s66[8]

    teach = choices(
     [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
     [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
     k=18)
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =     teach[10];t12 = teach[11];t13 = teach[12];t14 = teach[13];t15 = teach[14];t16 =teach[15];t17 = teach[16];t18 = teach[17]

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

    if num == 2:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 =  teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 =     teach[10];t12_2 = teach[11];t13_2 = teach[12];t14_2 = teach[13];t15_2 = teach[14];t16_2 =teach[15];t17_2 = teach[16];t18_2 = teach[17]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]
        random.shuffle(e)
        ba12=e[0];ba22=e[1];ba32=e[2]
        random.shuffle(f)
        bb12=f[0];bb22=f[1];bb32=f[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t13_2,t14_2,t15_2,t16_2,t17_2,t18_2]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(m13)
        count14 = teacher.count(m14)
        count15 = teacher.count(m15)
        count16 = teacher.count(s1)
        count17 = teacher.count(s2)
        count18 = teacher.count(s3)
        count19 = teacher.count(s4)
        count20 = teacher.count(s5)
        count21 = teacher.count(s6)
        count22 = teacher.count(s7)
        count23 = teacher.count(s8)
        count24 = teacher.count(s9)

        return render(request,'result1.html',{'time':time,'date':date,'time2':time2,'date2':date2,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'cr72':cr72,'cr82':cr82,'cr92':cr92,'sub12':sub12,'sub22':sub22,'sub32':sub32,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'ba12':ba12,'ba22':ba22,'ba32':ba32,'bb12':bb12,'bb22':bb22,'bb32':bb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t13_2':t13_2,'t14_2':t14_2,'t15_2':t15_2,'t16_2':t16_2,'t17_2':t17_2,'t18_2':t18_2,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})

    if num == 3:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 =  teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 =     teach[10];t12_2 = teach[11];t13_2 = teach[12];t14_2 = teach[13];t15_2 = teach[14];t16_2 =teach[15];t17_2 = teach[16];t18_2 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 =  teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 =     teach[10];t12_3 = teach[11];t13_3 = teach[12];t14_3 = teach[13];t15_3 = teach[14];t16_3 =teach[15];t17_3 = teach[16];t18_3 = teach[17]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]
        random.shuffle(e)
        ba12=e[0];ba22=e[1];ba32=e[2]
        random.shuffle(f)
        bb12=f[0];bb22=f[1];bb32=f[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]
        random.shuffle(e)
        ba13=e[0];ba23=e[1];ba33=e[2]
        random.shuffle(f)
        bb13=f[0];bb23=f[1];bb33=f[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t13_2,t14_2,t15_2,t16_2,t17_2,t18_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t13_3,t14_3,t15_3,t16_3,t17_3,t18_3]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(m13)
        count14 = teacher.count(m14)
        count15 = teacher.count(m15)
        count16 = teacher.count(s1)
        count17 = teacher.count(s2)
        count18 = teacher.count(s3)
        count19 = teacher.count(s4)
        count20 = teacher.count(s5)
        count21 = teacher.count(s6)
        count22 = teacher.count(s7)
        count23 = teacher.count(s8)
        count24 = teacher.count(s9)

        return render(request,'result1.html',{'time':time,'date':date,'time2':time2,'date2':date2,'time3':time3,'date3':date3,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'cr72':cr72,'cr82':cr82,'cr92':cr92,'sub12':sub12,'sub22':sub22,'sub32':sub32,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'ba12':ba12,'ba22':ba22,'ba32':ba32,'bb12':bb12,'bb22':bb22,'bb32':bb32,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'cr73':cr73,'cr83':cr83,'cr93':cr93,'sub13':sub13,'sub23':sub23,'sub33':sub33,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'ba13':ba13,'ba23':ba23,'ba33':ba33,'bb13':bb13,'bb23':bb23,'bb33':bb33,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t13_2':t13_2,'t14_2':t14_2,'t15_2':t15_2,'t16_2':t16_2,'t17_2':t17_2,'t18_2':t18_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t13_3':t13_3,'t14_3':t14_3,'t15_3':t15_3,'t16_3':t16_3,'t17_3':t17_3,'t18_3':t18_3,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})

    if num == 4:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 =  teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 =     teach[10];t12_2 = teach[11];t13_2 = teach[12];t14_2 = teach[13];t15_2 = teach[14];t16_2 =teach[15];t17_2 = teach[16];t18_2 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 =  teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 =     teach[10];t12_3 = teach[11];t13_3 = teach[12];t14_3 = teach[13];t15_3 = teach[14];t16_3 =teach[15];t17_3 = teach[16];t18_3 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 =  teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 =     teach[10];t12_4 = teach[11];t13_4 = teach[12];t14_4 = teach[13];t15_4 = teach[14];t16_4 =teach[15];t17_4 = teach[16];t18_4 = teach[17]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]
        random.shuffle(e)
        ba12=e[0];ba22=e[1];ba32=e[2]
        random.shuffle(f)
        bb12=f[0];bb22=f[1];bb32=f[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]
        random.shuffle(e)
        ba13=e[0];ba23=e[1];ba33=e[2]
        random.shuffle(f)
        bb13=f[0];bb23=f[1];bb33=f[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]
        random.shuffle(e)
        ba14=e[0];ba24=e[1];ba34=e[2]
        random.shuffle(f)
        bb14=f[0];bb24=f[1];bb34=f[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t13_2,t14_2,t15_2,t16_2,t17_2,t18_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t13_3,t14_3,t15_3,t16_3,t17_3,t18_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4,t13_4,t14_4,t15_4,t16_4,t17_4,t18_4]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(m13)
        count14 = teacher.count(m14)
        count15 = teacher.count(m15)
        count16 = teacher.count(s1)
        count17 = teacher.count(s2)
        count18 = teacher.count(s3)
        count19 = teacher.count(s4)
        count20 = teacher.count(s5)
        count21 = teacher.count(s6)
        count22 = teacher.count(s7)
        count23 = teacher.count(s8)
        count24 = teacher.count(s9)

        return render(request,'result1.html',{'time':time,'date':date,'time2':time2,'date2':date2,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'cr72':cr72,'cr82':cr82,'cr92':cr92,'sub12':sub12,'sub22':sub22,'sub32':sub32,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'ba12':ba12,'ba22':ba22,'ba32':ba32,'bb12':bb12,'bb22':bb22,'bb32':bb32,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'cr73':cr73,'cr83':cr83,'cr93':cr93,'sub13':sub13,'sub23':sub23,'sub33':sub33,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'ba13':ba13,'ba23':ba23,'ba33':ba33,'bb13':bb13,'bb23':bb23,'bb33':bb33,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'cr74':cr74,'cr84':cr84,'cr94':cr94,'sub14':sub14,'sub24':sub24,'sub34':sub34,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'ba14':ba14,'ba24':ba24,'ba34':ba34,'bb14':bb14,'bb24':bb24,'bb34':bb34,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t13_2':t13_2,'t14_2':t14_2,'t15_2':t15_2,'t16_2':t16_2,'t17_2':t17_2,'t18_2':t18_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t13_3':t13_3,'t14_3':t14_3,'t15_3':t15_3,'t16_3':t16_3,'t17_3':t17_3,'t18_3':t18_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'t13_4':t13_4,'t14_4':t14_4,'t15_4':t15_4,'t16_4':t16_4,'t17_4':t17_4,'t18_4':t18_4,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})

    if num == 5:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 =  teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 =     teach[10];t12_2 = teach[11];t13_2 = teach[12];t14_2 = teach[13];t15_2 = teach[14];t16_2 =teach[15];t17_2 = teach[16];t18_2 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 =  teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 =     teach[10];t12_3 = teach[11];t13_3 = teach[12];t14_3 = teach[13];t15_3 = teach[14];t16_3 =teach[15];t17_3 = teach[16];t18_3 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 =  teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 =     teach[10];t12_4 = teach[11];t13_4 = teach[12];t14_4 = teach[13];t15_4 = teach[14];t16_4 =teach[15];t17_4 = teach[16];t18_4 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_5 = teach[0];t2_5 = teach[1];t3_5 = teach[2];t4_5 = teach[3];t5_5 = teach[4];t6_5 =  teach[5];t7_5 = teach[6];t8_5 = teach[7];t9_5 = teach[8];t10_5 = teach[9];t11_5 =     teach[10];t12_5 = teach[11];t13_5 = teach[12];t14_5 = teach[13];t15_5 = teach[14];t16_5 =teach[15];t17_5 = teach[16];t18_5 = teach[17]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]
        random.shuffle(e)
        ba12=e[0];ba22=e[1];ba32=e[2]
        random.shuffle(f)
        bb12=f[0];bb22=f[1];bb32=f[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]
        random.shuffle(e)
        ba13=e[0];ba23=e[1];ba33=e[2]
        random.shuffle(f)
        bb13=f[0];bb23=f[1];bb33=f[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]
        random.shuffle(e)
        ba14=e[0];ba24=e[1];ba34=e[2]
        random.shuffle(f)
        bb14=f[0];bb24=f[1];bb34=f[2]

        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]
        random.shuffle(c)
        ta15=c[0];ta25=c[1];ta35=c[2]
        random.shuffle(d)
        tb15=d[0];tb25=d[1];tb35=d[2]
        random.shuffle(e)
        ba15=e[0];ba25=e[1];ba35=e[2]
        random.shuffle(f)
        bb15=f[0];bb25=f[1];bb35=f[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t13_2,t14_2,t15_2,t16_2,t17_2,t18_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t13_3,t14_3,t15_3,t16_3,t17_3,t18_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4,t13_4,t14_4,t15_4,t16_4,t17_4,t18_4,t1_5,t2_5,t3_5,t4_5,t5_5,t6_5,t7_5,t8_5,t9_5,t10_5,t11_5,t12_5,t13_5,t14_5,t15_5,t16_5,t17_5,t18_5]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(m13)
        count14 = teacher.count(m14)
        count15 = teacher.count(m15)
        count16 = teacher.count(s1)
        count17 = teacher.count(s2)
        count18 = teacher.count(s3)
        count19 = teacher.count(s4)
        count20 = teacher.count(s5)
        count21 = teacher.count(s6)
        count22 = teacher.count(s7)
        count23 = teacher.count(s8)
        count24 = teacher.count(s9)

        return render(request,'result1.html',{'time':time,'date':date,'time2':time2,'date2':date2,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'time5':time5,'date5':date5,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'cr72':cr72,'cr82':cr82,'cr92':cr92,'sub12':sub12,'sub22':sub22,'sub32':sub32,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'ba12':ba12,'ba22':ba22,'ba32':ba32,'bb12':bb12,'bb22':bb22,'bb32':bb32,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'cr73':cr73,'cr83':cr83,'cr93':cr93,'sub13':sub13,'sub23':sub23,'sub33':sub33,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'ba13':ba13,'ba23':ba23,'ba33':ba33,'bb13':bb13,'bb23':bb23,'bb33':bb33,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'cr74':cr74,'cr84':cr84,'cr94':cr94,'sub14':sub14,'sub24':sub24,'sub34':sub34,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'ba14':ba14,'ba24':ba24,'ba34':ba34,'bb14':bb14,'bb24':bb24,'bb34':bb34,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'cr75':cr75,'cr85':cr85,'cr95':cr95,'sub15':sub15,'sub25':sub25,'sub35':sub35,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'ta15':ta15,'ta25':ta25,'ta35':ta35,'tb15':tb15,'tb25':tb25,'tb35':tb35,'ba15':ba15,'ba25':ba25,'ba35':ba35,'bb15':bb15,'bb25':bb25,'bb35':bb35,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t13_2':t13_2,'t14_2':t14_2,'t15_2':t15_2,'t16_2':t16_2,'t17_2':t17_2,'t18_2':t18_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t13_3':t13_3,'t14_3':t14_3,'t15_3':t15_3,'t16_3':t16_3,'t17_3':t17_3,'t18_3':t18_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'t13_4':t13_4,'t14_4':t14_4,'t15_4':t15_4,'t16_4':t16_4,'t17_4':t17_4,'t18_4':t18_4,'t1_5':t1_5,'t2_5':t2_5,'t3_5':t3_5,'t4_5':t4_5,'t5_5':t5_5,'t6_5':t6_5,'t7_5':t7_5,'t8_5':t8_5,'t9_5':t9_5,'t10_5':t10_5,'t11_5':t11_5,'t12_5':t12_5,'t13_5':t13_5,'t14_5':t14_5,'t15_5':t15_5,'t16_5':t16_5,'t17_5':t17_5,'t18_5':t18_5,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})

    if num == 6:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 =  teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 =     teach[10];t12_2 = teach[11];t13_2 = teach[12];t14_2 = teach[13];t15_2 = teach[14];t16_2 =teach[15];t17_2 = teach[16];t18_2 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 =  teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 =     teach[10];t12_3 = teach[11];t13_3 = teach[12];t14_3 = teach[13];t15_3 = teach[14];t16_3 =teach[15];t17_3 = teach[16];t18_3 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 =  teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 =     teach[10];t12_4 = teach[11];t13_4 = teach[12];t14_4 = teach[13];t15_4 = teach[14];t16_4 =teach[15];t17_4 = teach[16];t18_4 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_5 = teach[0];t2_5 = teach[1];t3_5 = teach[2];t4_5 = teach[3];t5_5 = teach[4];t6_5 =  teach[5];t7_5 = teach[6];t8_5 = teach[7];t9_5 = teach[8];t10_5 = teach[9];t11_5 =     teach[10];t12_5 = teach[11];t13_5 = teach[12];t14_5 = teach[13];t15_5 = teach[14];t16_5 =teach[15];t17_5 = teach[16];t18_5 = teach[17]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,s7,s8,s9,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=18)
        random.shuffle(teach)
        t1_6 = teach[0];t2_6 = teach[1];t3_6 = teach[2];t4_6 = teach[3];t5_6 = teach[4];t6_6 =  teach[5];t7_6 = teach[6];t8_6 = teach[7];t9_6 = teach[8];t10_6 = teach[9];t11_6 =     teach[10];t12_6 = teach[11];t13_6 = teach[12];t14_6 = teach[13];t15_6 = teach[14];t16_6 =teach[15];t17_6 = teach[16];t18_6 = teach[17]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]
        random.shuffle(e)
        ba12=e[0];ba22=e[1];ba32=e[2]
        random.shuffle(f)
        bb12=f[0];bb22=f[1];bb32=f[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]
        random.shuffle(e)
        ba13=e[0];ba23=e[1];ba33=e[2]
        random.shuffle(f)
        bb13=f[0];bb23=f[1];bb33=f[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]
        random.shuffle(e)
        ba14=e[0];ba24=e[1];ba34=e[2]
        random.shuffle(f)
        bb14=f[0];bb24=f[1];bb34=f[2]

        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]
        random.shuffle(c)
        ta15=c[0];ta25=c[1];ta35=c[2]
        random.shuffle(d)
        tb15=d[0];tb25=d[1];tb35=d[2]
        random.shuffle(e)
        ba15=e[0];ba25=e[1];ba35=e[2]
        random.shuffle(f)
        bb15=f[0];bb25=f[1];bb35=f[2]

        random.shuffle(a)
        sa16=a[0];sa26=a[1];sa36=a[2]
        random.shuffle(b)
        sb16=b[0];sb26=b[1];sb36=b[2]
        random.shuffle(c)
        ta16=c[0];ta26=c[1];ta36=c[2]
        random.shuffle(d)
        tb16=d[0];tb26=d[1];tb36=d[2]
        random.shuffle(e)
        ba16=e[0];ba26=e[1];ba36=e[2]
        random.shuffle(f)
        bb16=f[0];bb26=f[1];bb36=f[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t13_2,t14_2,t15_2,t16_2,t17_2,t18_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t13_3,t14_3,t15_3,t16_3,t17_3,t18_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4,t13_4,t14_4,t15_4,t16_4,t17_4,t18_4,t1_5,t2_5,t3_5,t4_5,t5_5,t6_5,t7_5,t8_5,t9_5,t10_5,t11_5,t12_5,t13_5,t14_5,t15_5,t16_5,t17_5,t18_5,t1_6,t2_6,t3_6,t4_6,t5_6,t6_6,t7_6,t8_6,t9_6,t10_6,t11_6,t12_6,t13_6,t14_6,t15_6,t16_6,t17_6,t18_6]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(m13)
        count14 = teacher.count(m14)
        count15 = teacher.count(m15)
        count16 = teacher.count(s1)
        count17 = teacher.count(s2)
        count18 = teacher.count(s3)
        count19 = teacher.count(s4)
        count20 = teacher.count(s5)
        count21 = teacher.count(s6)
        count22 = teacher.count(s7)
        count23 = teacher.count(s8)
        count24 = teacher.count(s9)

        return render(request,'result1.html',{'time':time,'date':date,'time2':time2,'date2':date2,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'time5':time5,'date5':date5,'time6':time6,'date6':date6,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'cr72':cr72,'cr82':cr82,'cr92':cr92,'sub12':sub12,'sub22':sub22,'sub32':sub32,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'ba12':ba12,'ba22':ba22,'ba32':ba32,'bb12':bb12,'bb22':bb22,'bb32':bb32,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'cr73':cr73,'cr83':cr83,'cr93':cr93,'sub13':sub13,'sub23':sub23,'sub33':sub33,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'ba13':ba13,'ba23':ba23,'ba33':ba33,'bb13':bb13,'bb23':bb23,'bb33':bb33,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'cr74':cr74,'cr84':cr84,'cr94':cr94,'sub14':sub14,'sub24':sub24,'sub34':sub34,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'ba14':ba14,'ba24':ba24,'ba34':ba34,'bb14':bb14,'bb24':bb24,'bb34':bb34,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'cr75':cr75,'cr85':cr85,'cr95':cr95,'sub15':sub15,'sub25':sub25,'sub35':sub35,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'ta15':ta15,'ta25':ta25,'ta35':ta35,'tb15':tb15,'tb25':tb25,'tb35':tb35,'ba15':ba15,'ba25':ba25,'ba35':ba35,'bb15':bb15,'bb25':bb25,'bb35':bb35,'cr16':cr16,'cr26':cr26,'cr36':cr36,'cr46':cr46,'cr56':cr56,'cr66':cr66,'cr76':cr76,'cr86':cr86,'cr96':cr96,'sub16':sub16,'sub26':sub26,'sub36':sub36,'sa16':sa16,'sa26':sa26,'sa36':sa36,'sb16':sb16,'sb26':sb26,'sb36':sb36,'ta16':ta16,'ta26':ta26,'ta36':ta36,'tb16':tb16,'tb26':tb26,'tb36':tb36,'ba16':ba16,'ba26':ba26,'ba36':ba36,'bb16':bb16,'bb26':bb26,'bb36':bb36,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t13_2':t13_2,'t14_2':t14_2,'t15_2':t15_2,'t16_2':t16_2,'t17_2':t17_2,'t18_2':t18_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t13_3':t13_3,'t14_3':t14_3,'t15_3':t15_3,'t16_3':t16_3,'t17_3':t17_3,'t18_3':t18_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'t13_4':t13_4,'t14_4':t14_4,'t15_4':t15_4,'t16_4':t16_4,'t17_4':t17_4,'t18_4':t18_4,'t1_5':t1_5,'t2_5':t2_5,'t3_5':t3_5,'t4_5':t4_5,'t5_5':t5_5,'t6_5':t6_5,'t7_5':t7_5,'t8_5':t8_5,'t9_5':t9_5,'t10_5':t10_5,'t11_5':t11_5,'t12_5':t12_5,'t13_5':t13_5,'t14_5':t14_5,'t15_5':t15_5,'t16_5':t16_5,'t17_5':t17_5,'t18_5':t18_5,'t1_6':t1_6,'t2_6':t2_6,'t3_6':t3_6,'t4_6':t4_6,'t5_6':t5_6,'t6_6':t6_6,'t7_6':t7_6,'t8_6':t8_6,'t9_6':t9_6,'t10_6':t10_6,'t11_6':t11_6,'t12_6':t12_6,'t13_6':t13_6,'t14_6':t14_6,'t15_6':t15_6,'t16_6':t16_6,'t17_6':t17_6,'t18_6':t18_6,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})

    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t71,t18]
    count1 = teacher.count(m1)
    count2 = teacher.count(m2)
    count3 = teacher.count(m3)
    count4 = teacher.count(m4)
    count5 = teacher.count(m5)
    count6 = teacher.count(m6)
    count7 = teacher.count(m7)
    count8 = teacher.count(m8)
    count9 = teacher.count(m9)
    count10 = teacher.count(m10)
    count11 = teacher.count(m11)
    count12 = teacher.count(m12)
    count13 = teacher.count(m13)
    count14 = teacher.count(m14)
    count15 = teacher.count(m15)
    count16 = teacher.count(s1)
    count17 = teacher.count(s2)
    count18 = teacher.count(s3)
    count19 = teacher.count(s4)
    count20 = teacher.count(s5)
    count21 = teacher.count(s6)
    count22 = teacher.count(s7)
    count23 = teacher.count(s8)
    count24 = teacher.count(s9)

    ### write your logic here ###
    return render(request,'result1.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'cr7':cr7,'cr8':cr8,'cr9':cr9,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'ba1':ba1,'ba2':ba2,'ba3':ba3,'bb1':bb1,'bb2':bb2,'bb3':bb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'t13':t13,'t14':t14,'t15':t15,'t16':t16,'t17':t17,'t18':t18,'div1':div1,'div0':div0,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'count19':count19,'count20':count20,'count21':count21,'count22':count22,'count23':count23,'count24':count24,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'eo':eo,'unit':unit,'num':num})


def generate2(request):
    dep,eo,unit=request.POST['dep'],request.POST['eo'],request.POST['unit']
    date,sub1,sub2,time,sSEA,sSEB,sTEA,sTEB = request.POST['date'],request.POST['subject1'],request.POST['subject2'],request.POST['time'],int(request.POST['sSEA']),int(request.POST['sSEB']),int(request.POST['sTEA']),int(request.POST['sTEB'])
    l1,l2,l3,l4,l5,l6=request.POST['l1'],request.POST['l2'],request.POST['l3'],request.POST['l4'],request.POST['l5'],request.POST['l6']
    s1,s2,s3,s4,s5,s6=request.POST['s1'],request.POST['s2'],request.POST['s3'],request.POST['s4'],request.POST['s5'],request.POST['s6']
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6'],request.POST['m7'],request.POST['m8'],request.POST['m9'],request.POST['m10'],request.POST['m11'],request.POST['m12']
    z1,z2=request.POST['z1'],request.POST['z2']
    num=int(request.POST['num'])

    if num >= 2 :
        date2,sub12,sub22,time2 = request.POST['date2'],request.POST['subject12'],request.POST['subject22'],request.POST['time2']
        l12,l22,l32,l42,l52,l62=request.POST['l12'],request.POST['l22'],request.POST['l32'],request.POST['l42'],request.POST['l52'],request.POST['l62']
        s22=[l12,l22,l32,l42,l52,l62]
        random.shuffle(s22)
        cr12=s22[0];cr22=s22[1];cr32=s22[2];cr42=s22[3];cr52=s22[4];cr62=s22[5]
        if num >= 3 :
            date3,sub13,sub23,time3 = request.POST['date3'],request.POST['subject13'],request.POST['subject23'],request.POST['time3']
            l13,l23,l33,l43,l53,l63=request.POST['l13'],request.POST['l23'],request.POST['l33'],request.POST['l43'],request.POST['l53'],request.POST['l63']
            s33=[l13,l23,l33,l43,l53,l63]
            random.shuffle(s33)
            cr13=s33[0];cr23=s33[1];cr33=s33[2];cr43=s33[3];cr53=s33[4];cr63=s33[5]
            if num >= 4 :
                date4,sub14,sub24,time4 = request.POST['date4'],request.POST['subject14'],request.POST['subject24'],request.POST['time4']
                l14,l24,l34,l44,l54,l64=request.POST['l14'],request.POST['l24'],request.POST['l34'],request.POST['l44'],request.POST['l54'],request.POST['l64']
                s44=[l14,l24,l34,l44,l54,l64]
                random.shuffle(s44)
                cr14=s44[0];cr24=s44[1];cr34=s44[2];cr44=s44[3];cr54=s44[4];cr64=s44[5]
                if num >= 5 :
                    date5,sub15,sub25,time5 = request.POST['date5'],request.POST['subject15'],request.POST['subject25'],request.POST['time5']
                    l15,l25,l35,l45,l55,l65=request.POST['l15'],request.POST['l25'],request.POST['l35'],request.POST['l45'],request.POST['l55'],request.POST['l65']
                    s55=[l15,l25,l35,l45,l55,l65]
                    random.shuffle(s55)
                    cr15=s55[0];cr25=s55[1];cr35=s55[2];cr45=s55[3];cr55=s55[4];cr65=s55[5]
                    if num >= 6 :
                        date6,sub16,sub26,time6 = request.POST['date6'],request.POST['subject16'],request.POST['subject26'],request.POST['time6']
                        l16,l26,l36,l46,l56,l66=request.POST['l16'],request.POST['l26'],request.POST['l36'],request.POST['l46'],request.POST['l56'],request.POST['l66']
                        s66=[l16,l26,l36,l46,l56,l66]
                        random.shuffle(s66)
                        cr16=s66[0];cr26=s66[1];cr36=s66[2];cr46=s66[3];cr56=s66[4];cr66=s66[5]

    #teach = [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    teach = choices(
     [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
     [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
     k=12)
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5];t7 = teach[6];t8 = teach[7];t9 = teach[8];t10 = teach[9];t11 =   teach[10];t12 = teach[11]

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

    if num == 2:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 = teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 = teach[10];t12_2 = teach[11]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(s1)
        count14 = teacher.count(s2)
        count15 = teacher.count(s3)
        count16 = teacher.count(s4)
        count17 = teacher.count(s5)
        count18 = teacher.count(s6)

        return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'z1':z1,'z2':z2,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sub22':sub22,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32})

    if num == 3:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 = teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 = teach[10];t12_2 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 = teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 = teach[10];t12_3 = teach[11]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(s1)
        count14 = teacher.count(s2)
        count15 = teacher.count(s3)
        count16 = teacher.count(s4)
        count17 = teacher.count(s5)
        count18 = teacher.count(s6)

        return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'z1':z1,'z2':z2,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sub22':sub22,'sub13':sub13,'sub23':sub23,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'sub13':sub13,'sub23':sub23,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit})

    if num == 4:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 = teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 = teach[10];t12_2 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 = teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 = teach[10];t12_3 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 = teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 = teach[10];t12_4 = teach[11]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(s1)
        count14 = teacher.count(s2)
        count15 = teacher.count(s3)
        count16 = teacher.count(s4)
        count17 = teacher.count(s5)
        count18 = teacher.count(s6)

        return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'z1':z1,'z2':z2,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sub22':sub22,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'sub13':sub13,'sub23':sub23,'sub14':sub14,'sub24':sub24,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit})

    if num == 5:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 = teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 = teach[10];t12_2 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 = teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 = teach[10];t12_3 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 = teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 = teach[10];t12_4 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_5 = teach[0];t2_5 = teach[1];t3_5 = teach[2];t4_5 = teach[3];t5_5 = teach[4];t6_5 = teach[5];t7_5 = teach[6];t8_5 = teach[7];t9_5 = teach[8];t10_5 = teach[9];t11_5 = teach[10];t12_5 = teach[11]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]

        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]
        random.shuffle(c)
        ta15=c[0];ta25=c[1];ta35=c[2]
        random.shuffle(d)
        tb15=d[0];tb25=d[1];tb35=d[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4,t1_5,t2_5,t3_5,t4_5,t5_5,t6_5,t7_5,t8_5,t9_5,t10_5,t11_5,t12_5]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(s1)
        count14 = teacher.count(s2)
        count15 = teacher.count(s3)
        count16 = teacher.count(s4)
        count17 = teacher.count(s5)
        count18 = teacher.count(s6)

        return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'z1':z1,'z2':z2,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sub22':sub22,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'t1_5':t1_5,'t2_5':t2_5,'t3_5':t3_5,'t4_5':t4_5,'t5_5':t5_5,'t6_5':t6_5,'t7_5':t7_5,'t8_5':t8_5,'t9_5':t9_5,'t10_5':t10_5,'t11_5':t11_5,'t12_5':t12_5,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'ta15':ta15,'ta25':ta25,'ta35':ta35,'tb15':tb15,'tb25':tb25,'tb35':tb35,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'time5':time5,'date5':date5,'sub13':sub13,'sub23':sub23,'sub14':sub14,'sub24':sub24,'sub15':sub15,'sub25':sub25,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit})

    if num == 6:
        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_2 = teach[0];t2_2 = teach[1];t3_2 = teach[2];t4_2 = teach[3];t5_2 = teach[4];t6_2 = teach[5];t7_2 = teach[6];t8_2 = teach[7];t9_2 = teach[8];t10_2 = teach[9];t11_2 = teach[10];t12_2 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_3 = teach[0];t2_3 = teach[1];t3_3 = teach[2];t4_3 = teach[3];t5_3 = teach[4];t6_3 = teach[5];t7_3 = teach[6];t8_3 = teach[7];t9_3 = teach[8];t10_3 = teach[9];t11_3 = teach[10];t12_3 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_4 = teach[0];t2_4 = teach[1];t3_4 = teach[2];t4_4 = teach[3];t5_4 = teach[4];t6_4 = teach[5];t7_4 = teach[6];t8_4 = teach[7];t9_4 = teach[8];t10_4 = teach[9];t11_4 = teach[10];t12_4 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_5 = teach[0];t2_5 = teach[1];t3_5 = teach[2];t4_5 = teach[3];t5_5 = teach[4];t6_5 = teach[5];t7_5 = teach[6];t8_5 = teach[7];t9_5 = teach[8];t10_5 = teach[9];t11_5 = teach[10];t12_5 = teach[11]

        teach = choices(
         [s1,s2,s3,s4,s5,s6,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12],
         [0.025,0.025,0.025,0.025,0.025,0.025,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],
         k=12)
        random.shuffle(teach)
        t1_6 = teach[0];t2_6 = teach[1];t3_6 = teach[2];t4_6 = teach[3];t5_6 = teach[4];t6_6 = teach[5];t7_6 = teach[6];t8_6 = teach[7];t9_6 = teach[8];t10_6 = teach[9];t11_6 = teach[10];t12_6 = teach[11]

        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]
        random.shuffle(c)
        ta12=c[0];ta22=c[1];ta32=c[2]
        random.shuffle(d)
        tb12=d[0];tb22=d[1];tb32=d[2]

        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]
        random.shuffle(c)
        ta13=c[0];ta23=c[1];ta33=c[2]
        random.shuffle(d)
        tb13=d[0];tb23=d[1];tb33=d[2]

        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]
        random.shuffle(c)
        ta14=c[0];ta24=c[1];ta34=c[2]
        random.shuffle(d)
        tb14=d[0];tb24=d[1];tb34=d[2]

        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]
        random.shuffle(c)
        ta15=c[0];ta25=c[1];ta35=c[2]
        random.shuffle(d)
        tb15=d[0];tb25=d[1];tb35=d[2]

        random.shuffle(a)
        sa16=a[0];sa26=a[1];sa36=a[2]
        random.shuffle(b)
        sb16=b[0];sb26=b[1];sb36=b[2]
        random.shuffle(c)
        ta16=c[0];ta26=c[1];ta36=c[2]
        random.shuffle(d)
        tb16=d[0];tb26=d[1];tb36=d[2]

        teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1_2,t2_2,t3_2,t4_2,t5_2,t6_2,t7_2,t8_2,t9_2,t10_2,t11_2,t12_2,t1_3,t2_3,t3_3,t4_3,t5_3,t6_3,t7_3,t8_3,t9_3,t10_3,t11_3,t12_3,t1_4,t2_4,t3_4,t4_4,t5_4,t6_4,t7_4,t8_4,t9_4,t10_4,t11_4,t12_4,t1_5,t2_5,t3_5,t4_5,t5_5,t6_5,t7_5,t8_5,t9_5,t10_5,t11_5,t12_5,t1_6,t2_6,t3_6,t4_6,t5_6,t6_6,t7_6,t8_6,t9_6,t10_6,t11_6,t12_6]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(m7)
        count8 = teacher.count(m8)
        count9 = teacher.count(m9)
        count10 = teacher.count(m10)
        count11 = teacher.count(m11)
        count12 = teacher.count(m12)
        count13 = teacher.count(s1)
        count14 = teacher.count(s2)
        count15 = teacher.count(s3)
        count16 = teacher.count(s4)
        count17 = teacher.count(s5)
        count18 = teacher.count(s6)

        return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'z1':z1,'z2':z2,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sub22':sub22,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'ta12':ta12,'ta22':ta22,'ta32':ta32,'tb12':tb12,'tb22':tb22,'tb32':tb32,'t1_2':t1_2,'t2_2':t2_2,'t3_2':t3_2,'t4_2':t4_2,'t5_2':t5_2,'t6_2':t6_2,'t7_2':t7_2,'t8_2':t8_2,'t9_2':t9_2,'t10_2':t10_2,'t11_2':t11_2,'t12_2':t12_2,'t1_3':t1_3,'t2_3':t2_3,'t3_3':t3_3,'t4_3':t4_3,'t5_3':t5_3,'t6_3':t6_3,'t7_3':t7_3,'t8_3':t8_3,'t9_3':t9_3,'t10_3':t10_3,'t11_3':t11_3,'t12_3':t12_3,'t1_4':t1_4,'t2_4':t2_4,'t3_4':t3_4,'t4_4':t4_4,'t5_4':t5_4,'t6_4':t6_4,'t7_4':t7_4,'t8_4':t8_4,'t9_4':t9_4,'t10_4':t10_4,'t11_4':t11_4,'t12_4':t12_4,'t1_5':t1_5,'t2_5':t2_5,'t3_5':t3_5,'t4_5':t4_5,'t5_5':t5_5,'t6_5':t6_5,'t7_5':t7_5,'t8_5':t8_5,'t9_5':t9_5,'t10_5':t10_5,'t11_5':t11_5,'t12_5':t12_5,'t1_6':t1_6,'t2_6':t2_6,'t3_6':t3_6,'t4_6':t4_6,'t5_6':t5_6,'t6_6':t6_6,'t7_6':t7_6,'t8_6':t8_6,'t9_6':t9_6,'t10_6':t10_6,'t11_6':t11_6,'t12_6':t12_6,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'ta13':ta13,'ta23':ta23,'ta33':ta33,'tb13':tb13,'tb23':tb23,'tb33':tb33,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'ta14':ta14,'ta24':ta24,'ta34':ta34,'tb14':tb14,'tb24':tb24,'tb34':tb34,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'ta15':ta15,'ta25':ta25,'ta35':ta35,'tb15':tb15,'tb25':tb25,'tb35':tb35,'sa16':sa16,'sa26':sa26,'sa36':sa36,'sb16':sb16,'sb26':sb26,'sb36':sb36,'ta16':ta16,'ta26':ta26,'ta36':ta36,'tb16':tb16,'tb26':tb26,'tb36':tb36,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'time5':time5,'date5':date5,'time6':time6,'date6':date6,'sub13':sub13,'sub23':sub23,'sub14':sub14,'sub24':sub24,'sub15':sub15,'sub25':sub25,'sub16':sub16,'sub26':sub26,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'cr16':cr16,'cr26':cr26,'cr36':cr36,'cr46':cr46,'cr56':cr56,'cr66':cr66,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit})

    teacher = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]
    count1 = teacher.count(m1)
    count2 = teacher.count(m2)
    count3 = teacher.count(m3)
    count4 = teacher.count(m4)
    count5 = teacher.count(m5)
    count6 = teacher.count(m6)
    count7 = teacher.count(m7)
    count8 = teacher.count(m8)
    count9 = teacher.count(m9)
    count10 = teacher.count(m10)
    count11 = teacher.count(m11)
    count12 = teacher.count(m12)
    count13 = teacher.count(s1)
    count14 = teacher.count(s2)
    count15 = teacher.count(s3)
    count16 = teacher.count(s4)
    count17 = teacher.count(s5)
    count18 = teacher.count(s6)

    ### write your logic here ###
    return render(request,'result2.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sub2':sub2,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'ta1':ta1,'ta2':ta2,'ta3':ta3,'tb1':tb1,'tb2':tb2,'tb3':tb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10,'t11':t11,'t12':t12,'div1':div1,'div0':div0,'z1':z1,'z2':z2,'num':num,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'count10':count10,'count11':count11,'count12':count12,'count13':count13,'count14':count14,'count15':count15,'count16':count16,'count17':count17,'count18':count18,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,'m11':m11,'m12':m12,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'eo':eo,'unit':unit})

def generate3(request):
    dep = request.POST['dep']
    eo,unit = request.POST['eo'],request.POST['unit']
    date,sub1,time,sSEA,sSEB = request.POST['date1'],request.POST['subject11'],request.POST['time1'],int(request.POST['sSEA']),int(request.POST['sSEB'])
    l1,l2,l3,l4,l5,l6=request.POST['l11'],request.POST['l21'],request.POST['l31'],request.POST['l41'],request.POST['l51'],request.POST['l61']
    s1,s2,s3=request.POST['s1'],request.POST['s2'],request.POST['s3']
    m1,m2,m3,m4,m5,m6=request.POST['m1'],request.POST['m2'],request.POST['m3'],request.POST['m4'],request.POST['m5'],request.POST['m6']
    z1=request.POST['z1']
    num=int(request.POST['num'])
    if num >= 2:
        date2,sub12,time2 = request.POST['date2'],request.POST['subject12'],request.POST['time2']
        l12,l22,l32,l42,l52,l62=request.POST['l12'],request.POST['l22'],request.POST['l32'],request.POST['l42'],request.POST['l52'],request.POST['l62']
        s22=[l12,l22,l32,l42,l52,l62]
        random.shuffle(s22)
        cr12=s22[0];cr22=s22[1];cr32=s22[2];cr42=s22[3];cr52=s22[4];cr62=s22[5]
        if num >= 3:
            date3,sub13,time3 = request.POST['date3'],request.POST['subject13'],request.POST['time3']
            l13,l23,l33,l43,l53,l63=request.POST['l13'],request.POST['l23'],request.POST['l33'],request.POST['l43'],request.POST['l53'],request.POST['l63']
            s33=[l13,l23,l33,l43,l53,l63]
            random.shuffle(s33)
            cr13=s33[0];cr23=s33[1];cr33=s33[2];cr43=s33[3];cr53=s33[4];cr63=s33[5]
            if num >= 4:
                date4,sub14,time4 = request.POST['date4'],request.POST['subject14'],request.POST['time4']
                l14,l24,l34,l44,l54,l64=request.POST['l14'],request.POST['l24'],request.POST['l34'],request.POST['l44'],request.POST['l54'],request.POST['l64']
                s44=[l14,l24,l34,l44,l54,l64]
                random.shuffle(s44)
                cr14=s44[0];cr24=s44[1];cr34=s44[2];cr44=s44[3];cr54=s44[4];cr64=s44[5]
                if num >= 5:
                    date5,sub15,time5 = request.POST['date5'],request.POST['subject15'],request.POST['time5']
                    l15,l25,l35,l45,l55,l65=request.POST['l15'],request.POST['l25'],request.POST['l35'],request.POST['l45'],request.POST['l55'],request.POST['l65']
                    s55=[l15,l25,l35,l45,l55,l65]
                    random.shuffle(s55)
                    cr15=s55[0];cr25=s55[1];cr35=s55[2];cr45=s55[3];cr55=s55[4];cr65=s55[5]
                    if num >= 6:
                        date6,sub16,time6 = request.POST['date6'],request.POST['subject16'],request.POST['time6']
                        l16,l26,l36,l46,l56,l66=request.POST['l16'],request.POST['l26'],request.POST['l36'],request.POST['l46'],request.POST['l56'],request.POST['l66']
                        s6=[l16,l26,l36,l46,l56,l66]
                        random.shuffle(s6)
                        cr16=s6[0];cr26=s6[1];cr36=s6[2];cr46=s6[3];cr56=s6[4];cr66=s6[5]

    #teach = [s1,s2,s3,m1,m2,m3,m4,m5,m6]
    teach = choices(
     [s1,s2,s3,m1,m2,m3,m4,m5,m6],
     [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
     k=6)
    random.shuffle(teach)
    t1 = teach[0];t2 = teach[1];t3 = teach[2];t4 = teach[3];t5 = teach[4];t6 =  teach[5]

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


    a=[sa1,sa2,sa3]
    random.shuffle(a)
    sa1=a[0];sa2=a[1];sa3=a[2]
    b=[sb1,sb2,sb3]
    random.shuffle(b)
    sb1=b[0];sb2=b[1];sb3=b[2]

    s=[l1,l2,l3,l4,l5,l6]
    random.shuffle(s)
    cr1=s[0];cr2=s[1];cr3=s[2];cr4=s[3];cr5=s[4];cr6=s[5]
    if num== 2:
        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t12 = teach[0];t22 = teach[1];t32 = teach[2];t42 = teach[3];t52 = teach[4];t62 =  teach[5]
        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]

        teacher = [t1,t2,t3,t4,t5,t6,t12,t22,t32,t42,t52,t62]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(s1)
        count8 = teacher.count(s2)
        count9 = teacher.count(s3)

        return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t12':t12,'t22':t22,'t32':t32,'t42':t42,'t52':t52,'t62':t62,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})
    if num== 3:
        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t12 = teach[0];t22 = teach[1];t32 = teach[2];t42 = teach[3];t52 = teach[4];t62 =  teach[5]
        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t13 = teach[0];t23 = teach[1];t33 = teach[2];t43 = teach[3];t53 = teach[4];t63 =  teach[5]
        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]

        teacher = [t1,t2,t3,t4,t5,t6,t12,t22,t32,t42,t52,t62,t13,t23,t33,t43,t53,t63]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(s1)
        count8 = teacher.count(s2)
        count9 = teacher.count(s3)

        return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t12':t12,'t22':t22,'t32':t32,'t42':t42,'t52':t52,'t62':t62,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'sub13':sub13,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'t13':t13,'t23':t23,'t33':t33,'t43':t43,'t53':t53,'t63':t63,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})

    if num== 4:
        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t12 = teach[0];t22 = teach[1];t32 = teach[2];t42 = teach[3];t52 = teach[4];t62 =  teach[5]
        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t13 = teach[0];t23 = teach[1];t33 = teach[2];t43 = teach[3];t53 = teach[4];t63 =  teach[5]
        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t14 = teach[0];t24 = teach[1];t34 = teach[2];t44 = teach[3];t54 = teach[4];t64 =  teach[5]
        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]

        teacher = [t1,t2,t3,t4,t5,t6,t12,t22,t32,t42,t52,t62,t13,t23,t33,t43,t53,t63,t14,t24,t34,t44,t54,t64]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(s1)
        count8 = teacher.count(s2)
        count9 = teacher.count(s3)

        return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t12':t12,'t22':t22,'t32':t32,'t42':t42,'t52':t52,'t62':t62,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'sub13':sub13,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'t13':t13,'t23':t23,'t33':t33,'t43':t43,'t53':t53,'t63':t63,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'time4':time4,'date4':date4,'sub14':sub14,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'t14':t14,'t24':t24,'t34':t34,'t44':t44,'t54':t54,'t64':t64,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})

    if num== 5:
        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t12 = teach[0];t22 = teach[1];t32 = teach[2];t42 = teach[3];t52 = teach[4];t62 =  teach[5]
        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t13 = teach[0];t23 = teach[1];t33 = teach[2];t43 = teach[3];t53 = teach[4];t63 =  teach[5]
        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t14 = teach[0];t24 = teach[1];t34 = teach[2];t44 = teach[3];t54 = teach[4];t64 =  teach[5]
        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t15 = teach[0];t25 = teach[1];t35 = teach[2];t45 = teach[3];t55 = teach[4];t65 =  teach[5]
        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]

        teacher = [t1,t2,t3,t4,t5,t6,t12,t22,t32,t42,t52,t62,t13,t23,t33,t43,t53,t63,t14,t24,t34,t44,t54,t64,t15,t25,t35,t45,t55,t65]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(s1)
        count8 = teacher.count(s2)
        count9 = teacher.count(s3)

        return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t12':t12,'t22':t22,'t32':t32,'t42':t42,'t52':t52,'t62':t62,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'sub13':sub13,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'t13':t13,'t23':t23,'t33':t33,'t43':t43,'t53':t53,'t63':t63,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'time4':time4,'date4':date4,'sub14':sub14,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'t14':t14,'t24':t24,'t34':t34,'t44':t44,'t54':t54,'t64':t64,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'time5':time5,'date5':date5,'sub15':sub15,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'t15':t15,'t25':t25,'t35':t35,'t45':t45,'t55':t55,'t65':t65,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})

    if num== 6:
        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t12 = teach[0];t22 = teach[1];t32 = teach[2];t42 = teach[3];t52 = teach[4];t62 =  teach[5]
        random.shuffle(a)
        sa12=a[0];sa22=a[1];sa32=a[2]
        random.shuffle(b)
        sb12=b[0];sb22=b[1];sb32=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t13 = teach[0];t23 = teach[1];t33 = teach[2];t43 = teach[3];t53 = teach[4];t63 =  teach[5]
        random.shuffle(a)
        sa13=a[0];sa23=a[1];sa33=a[2]
        random.shuffle(b)
        sb13=b[0];sb23=b[1];sb33=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t14 = teach[0];t24 = teach[1];t34 = teach[2];t44 = teach[3];t54 = teach[4];t64 =  teach[5]
        random.shuffle(a)
        sa14=a[0];sa24=a[1];sa34=a[2]
        random.shuffle(b)
        sb14=b[0];sb24=b[1];sb34=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t15 = teach[0];t25 = teach[1];t35 = teach[2];t45 = teach[3];t55 = teach[4];t65 =  teach[5]
        random.shuffle(a)
        sa15=a[0];sa25=a[1];sa35=a[2]
        random.shuffle(b)
        sb15=b[0];sb25=b[1];sb35=b[2]

        teach = choices(
         [s1,s2,s3,m1,m2,m3,m4,m5,m6],
         [0.05,0.05,0.05,0.15,0.15,0.15,0.2,0.1,0.1],
         k=6)
        random.shuffle(teach)
        t16 = teach[0];t26 = teach[1];t36 = teach[2];t46 = teach[3];t56 = teach[4];t66 =  teach[5]
        random.shuffle(a)
        sa16=a[0];sa26=a[1];sa36=a[2]
        random.shuffle(b)
        sb16=b[0];sb26=b[1];sb36=b[2]

        teacher = [t1,t2,t3,t4,t5,t6,t12,t22,t32,t42,t52,t62,t13,t23,t33,t43,t53,t63,t14,t24,t34,t44,t54,t64,t15,t25,t35,t45,t55,t65,t16,t26,t36,t46,t56,t66]
        count1 = teacher.count(m1)
        count2 = teacher.count(m2)
        count3 = teacher.count(m3)
        count4 = teacher.count(m4)
        count5 = teacher.count(m5)
        count6 = teacher.count(m6)
        count7 = teacher.count(s1)
        count8 = teacher.count(s2)
        count9 = teacher.count(s3)

        return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'cr12':cr12,'cr22':cr22,'cr32':cr32,'cr42':cr42,'cr52':cr52,'cr62':cr62,'time2':time2,'date2':date2,'sub12':sub12,'sa12':sa12,'sa22':sa22,'sa32':sa32,'sb12':sb12,'sb22':sb22,'sb32':sb32,'t12':t12,'t22':t22,'t32':t32,'t42':t42,'t52':t52,'t62':t62,'cr13':cr13,'cr23':cr23,'cr33':cr33,'cr43':cr43,'cr53':cr53,'cr63':cr63,'time3':time3,'date3':date3,'time4':time4,'date4':date4,'sub13':sub13,'sa13':sa13,'sa23':sa23,'sa33':sa33,'sb13':sb13,'sb23':sb23,'sb33':sb33,'t13':t13,'t23':t23,'t33':t33,'t43':t43,'t53':t53,'t63':t63,'cr14':cr14,'cr24':cr24,'cr34':cr34,'cr44':cr44,'cr54':cr54,'cr64':cr64,'sub14':sub14,'sa14':sa14,'sa24':sa24,'sa34':sa34,'sb14':sb14,'sb24':sb24,'sb34':sb34,'t14':t14,'t24':t24,'t34':t34,'t44':t44,'t54':t54,'t64':t64,'cr15':cr15,'cr25':cr25,'cr35':cr35,'cr45':cr45,'cr55':cr55,'cr65':cr65,'time5':time5,'date5':date5,'sub15':sub15,'sa15':sa15,'sa25':sa25,'sa35':sa35,'sb15':sb15,'sb25':sb25,'sb35':sb35,'t15':t15,'t25':t25,'t35':t35,'t45':t45,'t55':t55,'t65':t65,'cr16':cr16,'cr26':cr26,'cr36':cr36,'cr46':cr46,'cr56':cr56,'cr66':cr66,'time6':time6,'date6':date6,'sub16':sub16,'sa16':sa16,'sa26':sa26,'sa36':sa36,'sb16':sb16,'sb26':sb26,'sb36':sb36,'t16':t16,'t26':t26,'t36':t36,'t46':t46,'t56':t56,'t66':t66,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})

    teacher = [t1,t2,t3,t4,t5,t6]

    count1 = teacher.count(m1)
    count2 = teacher.count(m2)
    count3 = teacher.count(m3)
    count4 = teacher.count(m4)
    count5 = teacher.count(m5)
    count6 = teacher.count(m6)
    count7 = teacher.count(s1)
    count8 = teacher.count(s2)
    count9 = teacher.count(s3)

    ### write your logic here ###
    return render(request,'result3.html',{'time':time,'date':date,'dep':dep,'cr1':cr1,'cr2':cr2,'cr3':cr3,'cr4':cr4,'cr5':cr5,'cr6':cr6,'sub1':sub1,'sa1':sa1,'sa2':sa2,'sa3':sa3,'sb1':sb1,'sb2':sb2,'sb3':sb3,'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'z1':z1,'num':num,'count1':count1,'count2':count2,'count3':count3,'count4':count4,'count5':count5,'count6':count6,'count7':count7,'count8':count8,'count9':count9,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'s1':s1,'s2':s2,'s3':s3,'eo':eo,'unit':unit})

def choices(population, weights, k=1):
    population = list(population)
    weigths = list(weights)
    result = []
    for n in range(k):
        pos = random.choices(
            range(len(population)),
            weights,
            k=1
        )[0]
        result.append(population[pos])
        del population[pos], weights[pos]
    return result

def combination(request):
    if request.method == 'POST':
        comb = request.POST['com1']
        num = request.POST['com2']
    if comb == 'SE,TE,BE':
        return render(request,'logedin1.html',{'num':num})
    if comb == 'SE,TE':
        z1='SE';z2='TE'
        return render(request,'logedin2.html',{'z1':z1,'z2':z2,'num':num})
    if comb == 'SE,BE':
        z1='SE';z2='BE'
        return render(request,'logedin2.html',{'z1':z1,'z2':z2,'num':num})
    if comb == 'TE,BE':
        z1='TE';z2='BE'
        return render(request,'logedin2.html',{'z1':z1,'z2':z2,'num':num})
    if comb == 'SE':
        z1='SE'
        return render(request,'logedin3.html',{'z1':z1,'num':num})
    if comb == 'TE':
        z1='TE'
        return render(request,'logedin3.html',{'z1':z1,'num':num})
    if comb == 'BE':
        z1='BE'
        return render(request,'logedin3.html',{'z1':z1,'num':num})
    return render(request,'logedin1.html',{'comb':comb})


def logout(request):
    return render(request,'login.html')
