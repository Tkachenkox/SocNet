class PersonAuthDataDto:

    def __init__(self, password: str, email: str):
        self.data = {
            'email': email,
            'password': password
        }