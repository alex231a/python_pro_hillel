from abc import ABC, abstractmethod
from typing import List


class MessageSender(ABC):
    """Interface MessageSender"""

    @abstractmethod
    def send_message(self, message: str):
        pass


class SMSService:
    """Class SMSService"""

    def send_sms(self, phone_number, message):
        print(f"Send SMS to {phone_number}: {message}")


class EmailService:
    """Class EmailService"""

    def send_email(self, email_address, message):
        print(f"Send Email to {email_address}: {message}")


class PushService:
    """Class PushService"""

    def send_push(self, device_id, message):
        print(f"Send Push message to {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Class SMSAdapter"""

    def __init__(self, sms_service: SMSService, phone_number: str):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Error during sending SMS: {e}")


class EmailAdapter(MessageSender):
    """Class EmailAdapter"""

    def __init__(self, email_service: EmailService, email_address: str):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Error during sending Email: {e}")


class PushAdapter(MessageSender):
    """Class EmailAdapter"""

    def __init__(self, push_service: PushService, device_id: str):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Error during sending Push-messages: {e}")


class MessageDispatcher:
    def __init__(self, senders: List[MessageSender]):
        self.senders = senders

    def dispatch_message(self, message: str):
        """dispatcher"""
        for sender in self.senders:
            sender.send_message(message)


if __name__ == "__main__":
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()
    sms_adapter = SMSAdapter(sms_service, "+380673456789")
    email_adapter = EmailAdapter(email_service, "test@example.com")
    push_adapter = PushAdapter(push_service, "deviceiphone")

    message_dispatcher = MessageDispatcher(
        [sms_adapter, email_adapter, push_adapter])
    message = "Test message."

    message_dispatcher.dispatch_message(message)
