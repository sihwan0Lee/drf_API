from django.db import models
from django.conf import settings
# Create your models here.


class Booking(models.Model):
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='booking')
    # PROTECT : 해당 요소가 같이 삭제되지 않도록 ProtectedError를 발생시킨다.
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    room = models.CharField(max_length=100)
    note = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber.username + " " + self.room

    # 장고쉘에서 get()이나, all() 혹은 filter()로 값을 읽어낼때 입력한 값 이 아닌 객체로써 표현된다.
    # 내가 입력한 값 그대로를 출력하여 보고싶을때 이 함수를 사용하면 된다.

    class Meta:
        ordering = ['-date_from']
