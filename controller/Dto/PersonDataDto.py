class PersonDataDto:

    def __init__(self, name, last_name, birtday, phone_number, email, gender, password, second_name=None):
        data = {
            'name': name,
            'second_name': second_name,
            'last_name': last_name,
            'birtday': birtday,
            'phone_number': phone_number,
            'email': email,
            'gender': gender,
            'password': password
        }