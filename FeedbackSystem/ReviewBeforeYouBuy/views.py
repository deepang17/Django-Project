from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import *
from ReviewBeforeYouBuy.models import *
from django.core.mail import send_mail
from django.conf import settings
import smtplib
import math, random


def Show_Content(request):
    return render(request, "Show_Content.html")


def Welcome(request):
    return render(request, "Welcome.html")


def Mobiles(request):
    return render(request, "Mobile.html")


def Laptops(request):
    return render(request, "Laptop.html")


def Camera(request):
    return render(request, "Camera.html")


def Admin(request):
    return render(request, "Admin.html")


def Computer_Hardwares(request):
    return render(request, "Computer_Hardware.html")


def Electronic_Accessories(request):
    return render(request, "Electronic_Accessories.html")


def Forgot_password(request):
    return render(request, "Forgot_password.html")


def Login(request):
    return render(request, "Login.html")


def New_Password(request):
    return render(request, "New_Password.html")


def OTP_verify(request):
    return render(request, "OTP_verify.html")


def Registration(request):
    return render(request, "Registration.html")


def Smart_Watch(request):
    return render(request, "Smart_Watch.html")


def Contact(request):
    return render(request, "Contact.html")


def Register(request):
    if request.method == "POST":
        if (
            request.POST.get("fname")
            and request.POST.get("lname")
            and request.POST.get("id")
            and request.POST.get("pass")
            and request.POST.get("cpass")
            and request.POST.get("email")
            and request.POST.get("cont-num")
        ):
            if request.POST.get("pass") == request.POST.get("cpass"):
                c = {}
                c.update(csrf(request))
                ud = Users()
                ud.fname = request.POST.get("fname")
                ud.lname = request.POST.get("lname")
                ud.uname = request.POST.get("id")
                ud.password = request.POST.get("pass")
                ud.email = request.POST.get("email")
                ud.mnumber = request.POST.get("cont-num")
                ud.save()
                return render(request, "Login.html")
            else:
                msg = "Your Password Not Matched"
                return render(request, "Registration.html", {"msg": msg})
        else:
            return render(request, "Registration.html")


def Logging(request):
    if request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("pass")
        if id == "DJA" and password == "DJA172504":
            return render(request, "Admin.html")
        else:
            ud = Users.objects.all()
            for user in ud:
                if user.uname == id and user.password == password:
                    request.session["uname"] = id
                    return render(request, "Welcome.html")
            msg = "Invalid Login Credentials"
            return render(request, "Login.html", {"msg": msg})


def Generate_Otp(request):
    if request.POST.get("email-id"):
        email = request.POST.get("email-id")
        ud = Users.objects.all()
        for user in ud:
            if user.email == email:
                request.session["email-id"] = email
                digits = "0123456789"
                OTP = ""
                for i in range(6):
                    OTP += digits[math.floor(random.random() * 10)]
                request.session["otp"] = OTP
                recipient_list = []

                recipient_list.append(email)
                subject = "OTP For Passowrd Changing"
                content = (
                    "Your OTP is " + OTP + "\n Please do not share otp with anyone."
                )
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, content, email_from, recipient_list)
                return render(request, "OTP_verify.html")
        msg = "Email Not Present In Database."
        return render(request, "Forgot_password.html", {"msg": msg})
    msg = "No Input Given As The Email"
    return render(request, "Forgot_password.html", {"msg": msg})


def Verification_OTP(request):
    if request.POST.get("otp"):
        otp = request.session["otp"]
        if request.POST.get("otp") == otp:
            return render(request, "New_Password.html")
    msg = "Incorrect OTP"
    return render(request, "OTP_verify.html", {"msg": msg})


def Change_Password(request):
    if request.POST.get("new_pass") == request.POST.get("rnew_pass"):
        c = {}
        c.update(csrf(request))

        email = request.session["email-id"]
        ud = Users.objects.get(email=email)
        ud.password = request.POST.get("new_pass")
        ud.save()
        request.session["email-id"] = None
        request.session["otp"] = None
        return render(request, "Login.html")
    msg = "Both Passwords Do Not Match !!!"
    return render(request, "New_Password.html", {"msg": msg})


def Logout(request):
    if request.session["uname"]:
        del request.session["uname"]
    return render(request, "Welcome.html")


def Notified(request):
    if request.POST.get("notify_email"):
        c = {}
        c.update(csrf(request))
        ud = Notify()
        ud.notify_email = request.POST.get("notify_email")
        ud.save()
    return render(request, "Welcome.html")


def M_Show_Content(request):
    m_info = Mobile.objects.all()
    return render(request,"M_Show_Content.html", {"m_info": m_info})


def L_Show_Content(request):
    l_info = Laptop.objects.all()
    return render_to_response("L_Show_Content.html", {"l_info": l_info})


def C_Show_Content(request):
    c_info = Cameras.objects.all()
    return render_to_response("C_Show_Content.html", {"c_info": c_info})


def S_Show_Content(request):
    s_info = Smart_Watches.objects.all()
    return render_to_response("S_Show_Content.html", {"s_info": s_info})


def E_Show_Content(request):
    e_info = Electronic_Accessory.objects.all()
    return render_to_response("E_Show_Content.html", {"e_info": e_info})


def H_Show_Content(request):
    h_info = Computer_Hardware.objects.all()
    return render_to_response("H_Show_Content.html", {"h_info": h_info})

def M_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Mobile.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.m_name:
                mf=Mobile_Feedback.objects.all()
                print(mf)
                return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : mf })
    return render(request,'M_Show_Content.html')

def L_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Laptop.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.l_name:
                mf=Laptop_Feedback.objects.all()
                for mobf in mf : 
                    if mobf.l_id == mobile: 
                        feedback.append(mobf)
        return render(request,"L_INFO.html", {"pinfo": mobile , "finfo" : feedback })
    return render(request,'L_Show_Content.html')

def C_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Camera.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.c_name:
                mf=Camera_Feedback.objects.all()
                for mobf in mf : 
                    if mobf.c_id == mobile: 
                        feedback.append(mobf)
        return render(request,"C_INFO.html", {"pinfo": mobile , "finfo" : feedback })
    return render(request,'C_Show_Content.html')

def S_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Smart_Watches.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.s_name:
                mf=Smart_Watches_Feedback.objects.all()
                for mobf in mf : 
                    if mobf.s_id == mobile: 
                        feedback.append(mobf)
        return render(request,"S_INFO.html", {"pinfo": mobile , "finfo" : feedback })
    return render(request,'S_Show_Content.html')

def H_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Computer_Hardware.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.h_name:
                mf=Computer_Hardware_Feedback.objects.all()
                for mobf in mf : 
                    if mobf.h_id == mobile: 
                        feedback.append(mobf)
        return render(request,"H_INFO.html", {"pinfo": mobile , "finfo" : feedback })
    return render(request,'H_Show_Content.html')

def E_INFO(request):
    print(request.POST.get("b1"))
    feedback=[]
    if request.method == "POST":
        submit_list=Electronic_Accessory.objects.all()
        for mobile in submit_list :
            if request.POST.get("b1") == mobile.e_name:
                mf=Electronic_Accessory_Feedback.objects.all()
                for mobf in mf : 
                    if mobf.e_id == mobile: 
                        feedback.append(mobf)
        return render(request,"E_INFO.html", {"pinfo": mobile , "finfo" : feedback })
    return render(request,'E_Show_Content.html')




# def M_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Mobile.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.m_name:
#                 mf=Mobile_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#                     print(request.POST.get("mob.m_id"))
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

# def L_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Laptop.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.l_name:
#                 mf=Laptop_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

# def C_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Mobile.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.m_name:
#                 mf=Mobile_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#                     print(request.POST.get("mob.m_id"))
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

# def S_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Mobile.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.m_name:
#                 mf=Mobile_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#                     print(request.POST.get("mob.m_id"))
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

# def H_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Mobile.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.m_name:
#                 mf=Mobile_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#                     print(request.POST.get("mob.m_id"))
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

# def E_INFO(request):
#     print(request.POST.get("b1"))
#     feedback=[]
#     if request.method == "POST":
#         submit_list=Mobile.objects.all()
#         for mobile in submit_list :
#             if request.POST.get("b1") == mobile.m_name:
#                 mf=Mobile_Feedback.objects.all()
#                 for mobf in mf : 
#                     if mobf.m_id == mobile: 
#                         feedback.append(mobf)
#                     print(request.POST.get("mob.m_id"))
#         return render(request,"M_INFO.html", {"pinfo": mobile , "finfo" : feedback })
#     return render(request,'M_Show_Content.html')

def Add_Product(request):
    if request.method == "POST":
        c = {}
        c.update(csrf(request))
        category = request.POST.get("category")
        device_name = request.POST.get("pname")
        if category == "Mobile":
            pd = Mobile()
            pd.m_name = request.POST.get("pname")
            pd.m_price = request.POST.get("price")
            pd.m_photo_link = request.POST.get("pro_img")
            pd.m_content_link = request.POST.get("pro_desc")
            pd.save()
        if category == "Laptop":
            pd = Laptop()
            pd.l_name = request.POST.get("pname")
            pd.l_price = request.POST.get("price")
            pd.l_photo_link = request.POST.get("pro_img")
            pd.l_content_link = request.POST.get("pro_desc")
            pd.save()
        if category == "Camera":
            pd = Cameras()
            pd.c_name = request.POST.get("pname")
            pd.c_price = request.POST.get("price")
            pd.c_photo_link = request.POST.get("pro_img")
            pd.c_content_link = request.POST.get("pro_desc")
            pd.save()
        if category == "Smart_Watch":
            pd = Smart_Watches()
            pd.s_name = request.POST.get("pname")
            pd.s_price = request.POST.get("price")
            pd.s_photo_link = request.POST.get("pro_img")
            pd.s_content_link = request.POST.get("pro_desc")
            pd.save()
        if category == "Com_Hardware":
            pd = Computer_Hardware()
            pd.h_name = request.POST.get("pname")
            pd.h_price = request.POST.get("price")
            pd.h_photo_link = request.POST.get("pro_img")
            pd.h_content_link = request.POST.get("pro_desc")
            pd.save()
        if category == "Elec_Accessories":
            pd =  Electronic_Accessory()
            pd.e_name = request.POST.get("pname")
            pd.e_price = request.POST.get("price")
            pd.e_photo_link = request.POST.get("pro_img")
            pd.e_content_link = request.POST.get("pro_desc")
            pd.save()
        ud = Notify.objects.all()
        recipient_list = []
        for user in ud:
            email = user.notify_email
            recipient_list.append(email)
        subject = "New Device Alert"
        content = (
            "New Device Alert\n \t New Device In Category : "
            + category
            + "\n \tDevice Name : "
            + device_name
            + "\nVisit The Website For More Information."
        )
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, content, email_from, recipient_list)
        return render(request, "Welcome.html")
    msg = "You Have To Be Admin To Access This Page"
    return render(request, "Login.html", {"msg": msg})

def M_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Mobile_Feedback()
    mf.m_feedback = review
    mf.save()
    return render(request,"Welcome.html")

def L_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Laptop_Feedback()
    mf.h_feedback = review
    mf.save()
    return render(request,"Welcome.html")

def C_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Camera_Feedback()
    mf.c_feedback = review
    mf.save()
    return render(request,"Welcome.html")

def S_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Smart_Watches_Feedback()
    mf.s_feedback = review
    mf.save()
    return render(request,"Welcome.html")

def E_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Electronic_Accessory_Feedback()
    mf.e_feedback = review
    mf.save()
    return render(request,"Welcome.html")

def H_Save_FeedBack(request):
    review = request.POST.get('review')
    mf = Computer_Hardware_Feedback()
    mf.h_feedback = review
    mf.save()
    return render(request,"Welcome.html")