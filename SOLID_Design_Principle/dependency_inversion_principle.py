from abc import ABC, abstractmethod

# Abstraction
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Low-Level Modules
class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSSender(MessageSender):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

# High-Level Module
class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# Usage
email_sender = EmailSender()
sms_sender = SMSSender()

notification = Notification(email_sender)
notification.notify("Hello, Email!")

notification = Notification(sms_sender)
notification.notify("Hello, SMS!")
