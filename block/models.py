# coding:utf-8
from django.db import models


class Block(models.Model):
    title = models.CharField(u"标题", max_length=30)
    desc = models.CharField(u"描述", max_length=150)
    manager = models.CharField(u"管理员", max_length=100)
    status = models.IntegerField("状态", choices=((0, "正常"), (1, "删除")))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "版块"
        verbose_name_plural = "版块"
