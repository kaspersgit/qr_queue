Based on the requirements, here are the core classes, functions, and methods that will be necessary:

1. `QueueManager` class:
   - `add_to_queue(phone_id: str) -> None`: Adds a phone to the queue.
   - `remove_from_queue() -> None`: Removes the first phone from the queue.
   - `get_queue() -> List[str]`: Returns the current queue.
   - `get_position(phone_id: str) -> Optional[int]`: Returns the position of a phone in the queue.

2. `QRCodeGenerator` class:
   - `generate_qr_code(data: str, file_path: str) -> None`: Generates a QR code with the given data and saves it to the specified file path.

3. `Server` class:
   - `start() -> None`: Starts the server and listens for incoming requests.
   - `handle_scan_request(phone_id: str) -> None`: Handles the request when a QR code is scanned.

Now, let's proceed with creating the necessary files and implementing the code.

**1. queue_manager.py**

