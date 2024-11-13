class EmailNotification:
    def send(self, user_email, message):
        print(f"Email sent to {user_email}: {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(method="email"):
        if method == "email":
            return EmailNotification()