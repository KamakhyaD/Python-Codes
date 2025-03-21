class Messenger:
    def send_message(self):
        print("Message sent")
    def receive_message(self):
        print("Message received")

# Inheritance
class InternalMessenger(Messenger):
    pass

class WhatsappMessenger:
    # Overriding
    def send_message(self):
        print("Whatsapp message sent")
    def receive_message(self):
        print("Whatsapp message received")
    # Specialized
    def set_dp(self):
        print("Display picture set")
    def set_status(self):
        print("Status set")

lm=WhatsappMessenger()
lm.send_message()
lm.receive_message()
lm.set_dp()
lm.set_status()