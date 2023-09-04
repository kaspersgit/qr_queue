from typing import List, Optional

class QueueManager:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, identifier: str) -> None:
        if identifier not in self.queue:
            self.queue.append(identifier)

    def remove_from_queue(self, identifier) -> None:
        if identifier in self.queue:
            self.queue.remove(identifier)

    def get_queue(self) -> List[str]:
        return self.queue

    def get_position(self, user_id: str) -> Optional[int]:
        if user_id in self.queue:
            return self.queue.index(user_id)
        return None
