class PersonDataDto:

    def __init__(self, first_name: str, last_name: str, birthday: str,
                    phone_number: str, email: str, gender: int, password: str, position: str, second_name=None):
        self.data = {
            'first_name': first_name,
            'second_name': second_name,
            'last_name': last_name,
            'birthday': birthday,
            'phone_number': phone_number,
            'email': email,
            'gender': gender,
            'password': password,
            'position': position,
        }