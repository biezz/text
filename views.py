# coding:utf-8
from django.shortcuts import render
from block.models import Block


def block_list(request):
    block_info = Block.objects.filter(status=0).order_by("id")
    return render(request, 'block_list.html', {'block_info': block_info})
