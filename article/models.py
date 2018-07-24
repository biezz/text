# coding:gbk
from django.db import models
from block.models import Block
from django.contrib.auth.models import User


class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name="���ID")
    title = models.CharField("��������", max_length=100)
    content = models.CharField("��������", max_length=10000)
    status = models.IntegerField("״̬", choices=((0, "����"), (1, "ɾ��")))

    create_timestamp = models.DateTimeField("����ʱ��", auto_now_add=True)
    last_update_timestamp = models.DateTimeField("�������ʱ��", auto_now=True)
    owner = models.ForeignKey(User, verbose_name="����")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "����"
        verbose_name_plural = "����"
