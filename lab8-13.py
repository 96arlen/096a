class EmailNotify:
    def send(self, msg): return f"Email: {msg}"

class SMSNotify:
    def send(self, msg): return f"SMS: {msg}"

class PushNotify:
    def send(self, msg): return f"Push: {msg}"


for n in [EmailNotify(), SMSNotify(), PushNotify()]:
    print(n.send("Привет"))
