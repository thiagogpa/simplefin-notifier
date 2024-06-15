class NotificationService:
    def __init__(self):
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def notify(self, title, message, priority=0):
        for service in self.services:
            service.notify(title, message, priority)