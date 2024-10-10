from collections import deque

class ArtClassScheduler:
    def __init__(self):
        self.available_sessions = ["Watercolor Painting", "Oil Painting", "Sketching", "Pottery"]
        self.scheduled_classes = []
        self.undo_stack = []
        self.request_queue = deque()

    def schedule_class(self, session_name):
        if session_name in self.available_sessions:
            booking = f"Class scheduled: {session_name}"
            self.scheduled_classes.append(booking)
            self.undo_stack.append(booking)  # Push to undo stack
            print(booking)
        else:
            print(f"{session_name} is not available.")

    def undo_booking(self):
        if self.undo_stack:
            last_booking = self.undo_stack.pop()
            self.scheduled_classes.remove(last_booking)
            print(f"Cancelled: {last_booking}")
        else:
            print("No bookings to undo.")

    def request_class(self, session_name):
        if session_name in self.available_sessions:
            self.request_queue.append(session_name)
            print(f"Requested class: {session_name}")
        else:
            print(f"{session_name} is not available.")

    def process_request(self):
        if self.request_queue:
            session_name = self.request_queue.popleft()
            self.schedule_class(session_name)
        else:
            print("No class requests to process.")

    def show_scheduled_classes(self):
        print("Scheduled Classes:")
        for cls in self.scheduled_classes:
            print(cls)

    def show_available_sessions(self):
        print("Available Sessions:")
        for session in self.available_sessions:
            print(session)

# Example usage
if __name__ == "__main__":
    scheduler = ArtClassScheduler()
    scheduler.show_available_sessions()
    
    scheduler.request_class("Watercolor Painting")
    scheduler.process_request()
    scheduler.show_scheduled_classes()
    
    scheduler.request_class("Oil Painting")
    scheduler.process_request()
    scheduler.show_scheduled_classes()
    
    scheduler.undo_booking()
    scheduler.show_scheduled_classes()
