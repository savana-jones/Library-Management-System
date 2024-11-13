from models.notification_factory import NotificationFactory
class Observer:
    def __init__(self):
        self.waiting_users = {}

    def add_to_waitlist(self, book_id, user_email):
        if book_id not in self.waiting_users:
            self.waiting_users[book_id] = []
        self.waiting_users[book_id].append(user_email)

    def notify(self, book_id):
        if book_id in self.waiting_users and self.waiting_users[book_id]:
            user_email = self.waiting_users[book_id].pop(0)
            notification = NotificationFactory.create_notification("email")
            notification.send(user_email, f"Book {book_id} is now available for rent.")

"""            self.send_notification(user_email, book_id)

    def send_notification(self, user_email, book_id):
        print(f"Notification sent to {user_email}: Book {book_id} is now available for rent.")"""
