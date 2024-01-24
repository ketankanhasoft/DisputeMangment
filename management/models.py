from django.db import models

from common.constants import CASTSTATUS

# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=200)
    item = models.CharField(max_length=500)
    customer_details = models.CharField(max_length=500)


class Return(models.Model):
    order_id = models.CharField(max_length=200)
    return_reason = models.TextField(null=True)
    return_tracking = models.CharField(max_length=50)
    original_order_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.order_id} - {self.return_reason}"


class CaseManagement(models.Model):
    return_info = models.ForeignKey(
        Return,
        to_field="id",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="return_id",
    )
    reason = models.TextField(null=True)
    status = models.PositiveSmallIntegerField(
        choices=CASTSTATUS.CHOICES,
        default=CASTSTATUS.OPEN,
    )
