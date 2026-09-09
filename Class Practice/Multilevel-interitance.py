class Security():
    def protect(self):
        print("System protection is enabled")

class NetworkSecurity(Security):
    def monitor_network(self):
        print("Every packet in network are being monitored")

class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("Unwanted and malicious traffic are blocked")

f = Firewall()
f.protect()
f.monitor_network()
f.block_traffic()
