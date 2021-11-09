class PersonUpdateDto:

    def __init__(self, name=None, last_name=None, birtday=None, phone_number=None, 
                    email=None, gender=None, password=None, second_name=None):
        self.data = {
            'name': name,
            'second_name': second_name,
            'last_name': last_name,
            'birtday': birtday,
            'phone_number': phone_number,
            'email': email,
            'gender': gender,
            'password': password
        }