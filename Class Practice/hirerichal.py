class SecuritySystem:
    def monitor(self):
        print("Network is being monitored.")

class IDS(SecuritySystem):
    def detect(self):
        print("IDS detected a malware")

class IPS(SecuritySystem):
    def prevent(self):
        print("IPS prevents malicious activity")

