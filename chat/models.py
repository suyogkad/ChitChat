from django.db import models
from django.conf import settings


# Define the Message model
class Message(models.Model):
    # A foreign key to Django's built-in User model. This represents the sender of the message.
    # 'on_delete=models.CASCADE' means if a User is deleted, their messages are also deleted.
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)

    # A foreign key to Django's built-in User model for the receiver of the message.
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)

    # The actual message content. 'TextField' is used for longer text without a character limit.
    message = models.TextField()

    # A timestamp indicating when the message was sent. 'auto_now_add=True' automatically sets this field to the current date/time when a message is first created.
    timestamp = models.DateTimeField(auto_now_add=True)

    # Meta options to order messages by timestamp
    class Meta:
        ordering = ['timestamp']

    # String representation of the Message model.
    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.message[:50]}"
