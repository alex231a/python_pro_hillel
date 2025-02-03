from abc import ABC, abstractmethod
from typing import List


class MessageSender(ABC):
    """
    Interface for sending messages. Classes implementing this interface
    should define the `send_message` method.
    """

    @abstractmethod
    def send_message(self, message: str):
        """
        Abstract method to send a message.

        :param message: The message content to be sent.
        """
        pass


class SMSService:
    """
    Service for sending SMS messages.
    """

    def send_sms(self, phone_number: str, message: str):
        """
        Sends an SMS message to a given phone number.

        :param phone_number: Recipient's phone number.
        :param message: The message content to be sent.
        """
        print(f"Send SMS to {phone_number}: {message}")


class EmailService:
    """
    Service for sending email messages.
    """

    def send_email(self, email_address: str, message: str):
        """
        Sends an email message to a given email address.

        :param email_address: Recipient's email address.
        :param message: The message content to be sent.
        """
        print(f"Send Email to {email_address}: {message}")


class PushService:
    """
    Service for sending push notifications.
    """

    def send_push(self, device_id: str, message: str):
        """
        Sends a push notification to a given device.

        :param device_id: Identifier of the recipient's device.
        :param message: The message content to be sent.
        """
        print(f"Send Push message to {device_id}: {message}")


class SMSAdapter(MessageSender):
    """
    Adapter for sending SMS messages using SMSService.
    """

    def __init__(self, sms_service: SMSService, phone_number: str):
        """
        Initializes the SMS adapter with a service instance and recipient phone number.

        :param sms_service: Instance of SMSService.
        :param phone_number: Recipient's phone number.
        """
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        """
        Sends an SMS message using the SMSService.

        :param message: The message content to be sent.
        """
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Error during sending SMS: {e}")


class EmailAdapter(MessageSender):
    """
    Adapter for sending email messages using EmailService.
    """

    def __init__(self, email_service: EmailService, email_address: str):
        """
        Initializes the Email adapter with a service instance and recipient email address.

        :param email_service: Instance of EmailService.
        :param email_address: Recipient's email address.
        """
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        """
        Sends an email message using the EmailService.

        :param message: The message content to be sent.
        """
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Error during sending Email: {e}")


class PushAdapter(MessageSender):
    """
    Adapter for sending push notifications using PushService.
    """

    def __init__(self, push_service: PushService, device_id: str):
        """
        Initializes the Push adapter with a service instance and recipient device ID.

        :param push_service: Instance of PushService.
        :param device_id: Identifier of the recipient's device.
        """
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        """
        Sends a push notification using the PushService.

        :param message: The message content to be sent.
        """
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Error during sending Push-messages: {e}")


class MessageDispatcher:
    """
    Dispatcher responsible for sending messages through multiple adapters.
    """

    def __init__(self, senders: List[MessageSender]):
        """
        Initializes the dispatcher with a list of message senders.

        :param senders: List of MessageSender instances.
        """
        self.senders = senders

    def dispatch_message(self, message: str):
        """
        Sends a message to all registered senders.

        :param message: The message content to be sent.
        """
        for sender in self.senders:
            sender.send_message(message)


if __name__ == "__main__":
    # Initialize messaging services
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    # Create adapters for messaging services
    sms_adapter = SMSAdapter(sms_service, "+380673456789")
    email_adapter = EmailAdapter(email_service, "test@example.com")
    push_adapter = PushAdapter(push_service, "deviceiphone")

    # Initialize message dispatcher with multiple senders
    message_dispatcher = MessageDispatcher([
        sms_adapter, email_adapter, push_adapter
    ])

    # Dispatch a test message
    message = "Test message."
    message_dispatcher.dispatch_message(message)
