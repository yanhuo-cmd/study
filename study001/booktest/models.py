from django.db import models

# Create your models here.


# 创建一个名字为booktest_areainfo的表
class AreaInfo(models.Model):
    # 设置一个字段为atitle
    atitle = models.CharField(max_length=20)
    # 设置一个和自己关联的外键
    aParent = models.ForeignKey('self', null=True, blank=True)
    # 改变str方法的返回值

    def __str__(self):
        # 返回标题
        # 1111
        return str(self.id)+':'+self.atitle+':'+str(self.aParent)

