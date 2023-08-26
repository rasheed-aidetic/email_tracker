from django.db import models
import uuid

# Create your models here.


class SendMail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.EmailField()
    reciever = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.reciever}"
    

class TrackMail(models.Model):
    mail = models.ForeignKey(SendMail, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)
    opened_time_diff = models.TimeField(null=True)

    def __str__(self):
        return f"{self.mail}"