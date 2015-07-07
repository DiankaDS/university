from django.core.exceptions import ValidationError
from django.db import models
from student.models import Students


class Groups(models.Model):
    group_name = models.CharField(max_length=10)
    elder = models.OneToOneField(Students, related_name="elder", null=True,
                                 blank=True)

    def __str__(self):
        return self.group_name

    def clean(self):
        if self.elder and self.elder.group != self:
            raise ValidationError(
                "You can not make this student elder, it is from other group")
        return super(Groups, self).clean()
