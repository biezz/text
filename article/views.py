# coding:utf-8

from django.shortcuts import render
from block.models import Block
from .models import Article
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from  django.core.paginator import Paginator


def paginate_queryset(objs, page_no, count_per_page=10, half_show_length=2):
    p = Paginator(objs, count_per_page)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no <= 0:
        page_no = 1
    page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1)
                  if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0] - 1
    next_link = page_links[-1] + 1
    pagination_data = {"has_previous": previous_link > 0,
                       "has_next": next_link <= p.num_pages,
                       "previous_link": previous_link,
                       "next_link": next_link,
                       "page_cnt": p.num_pages,
                       "current_no": page_no,
                       "page_links": page_links}
    return (page.object_list, pagination_data)


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block, status=0).order_by('-id')

    page_no = int(request.GET.get("page_no", "1"))
    object_list, pagination_data = paginate_queryset(article_objs, page_no, count_per_page=1)
    return render(request, "article_list.html",
                  {"articles": object_list, "b": block, "pagination_data": pagination_data})


def create_article(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    elif request.method == "POST":
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request, messages.ERROR, u'标题和内容均不能为空')
            return render(request, "article_create.html", {"b": block, "title": title, "content": content})

        owner = request.user
        new_article = Article(block=block, owner=owner, title=title, content=content, status=0)
        new_article.save()
        messages.add_message(request, messages.INFO, u'成功发布文章.')
        return redirect(reverse("article_list", args=[block.id]))


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)

    return render(request, "article_detail.html", {"article": article})




