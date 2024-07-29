from whatsApp_Scheduler.scheduler import WhatsAppMessageScheduler

# List of phone numbers in the format "+[country code][phone number]"
phone_numbers = [
    "+919740017751",
    "+919483185675"
    # Add more phone numbers as needed
]

# Common message to be sent
common_message = "Hello, OOPs way of writing, just to send message from laptop - trial_5."

# Instantiate the scheduler
scheduler = WhatsAppMessageScheduler(phone_numbers, common_message)

# Schedule the messages
scheduler.schedule_messages()