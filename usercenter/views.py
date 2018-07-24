# coding: utf-8

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render


def usercenter_register(request):
    error = ""
    if request.method == "GET":
        return render(request, "usercenter_register.html", {})
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()
        if not username or not password or not email:
            error = u"任何字段都不能为空"
        if password != re_password:
            error = u"两次密码不一致"
        if User.objects.filter(username=username).count() > 0:
            error = u"用户已存在"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        else:
            return render(request, "usercenter_register.html", {"error": error})
        return redirect(reverse("login"))
