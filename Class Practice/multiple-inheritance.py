class Encryption:
    def encrypt(self):
        print("Data is encrypted.")

class Authentication:
    def authenticate(self):
        print("User authentication is performed.")

class SecureSystem(Encryption, Authentication):
    def secure_data(self):
        print("System provides secure data access.")

s = SecureSystem()
s.encrypt()
s.authenticate()
s.secure_data()