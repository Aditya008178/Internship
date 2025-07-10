# 15.	Create an abstract class Notification:
# o	Abstract method: send_message()
# o	Subclasses:
# 	EmailNotification
# 	SMSNotification
# 	PushNotification


from abc import ABC, abstractmethod
class Notification(ABC):
    def __init__(self, msg):
        self.msg = msg
   
    @abstractmethod
    def send_message(self):
        pass


class EmailNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)

    def send_message(self):
        print(f"Email Received: {self.msg}")


class SMSNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)

    def send_message(self):
        print(f"SMS Received: {self.msg}")


class PushNotification(Notification):
    def __init__(self, msg):
        super().__init__(msg)
    def send_message(self):
        print(f"Push Received: {self.msg}")


email = EmailNotification("Hello, this is an email notification.")
sms = SMSNotification("Hello, this is an SMS notification.")
push = PushNotification("Hello, this is a push notification.")

email.send_message()
sms.send_message()
push.send_message()
