import pywhatkit as kit
import datetime

class WhatsAppMessageScheduler:
    def __init__(self, phone_numbers, common_message, wait_time=10, tab_close_time=3):
        self.phone_numbers = phone_numbers
        self.common_message = common_message
        self.wait_time = wait_time
        self.tab_close_time = tab_close_time

    def schedule_messages(self):
        # Get the current time
        now = datetime.datetime.now()
        print(f"Starting message scheduling at {now}")

        for phone_number in self.phone_numbers:
            # Calculate the time to send the message (e.g., 1 minute apart for each message)
            send_time = now + datetime.timedelta(minutes=1)
            hour = send_time.hour
            minute = send_time.minute

            try:
                print(f"Scheduling message to be sent to {phone_number} at {hour}:{minute}")
                kit.sendwhatmsg(phone_number, self.common_message, hour, minute, wait_time=self.wait_time, tab_close=True, close_time=self.tab_close_time)
                print(f"Message scheduled successfully to {phone_number}.")
            except Exception as e:
                print(f"An error occurred while scheduling message to {phone_number}: {e}")

            # Update the current time for the next message
            now = send_time
