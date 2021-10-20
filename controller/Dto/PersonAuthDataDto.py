class PersonAuthDataDto:

    def __init__(self, password: str, phone_number=None, email=None):
        data = {
            'phone_number': phone_number,
            'email': email,
            'password': password
        }