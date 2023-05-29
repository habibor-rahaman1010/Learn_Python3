#class and object create in python progam

class Phone:
    price = 12000
    category = 'phone'
    color = 'black'
    brand = 'samsung'
    features = ['good camera', 'low light image captured', 'water prove', 'good speaker']

    def calling(self):
        print('Hello how are you?')

    def send_sms(self, phone, sms):
        text = f'Sending sms to phone number: {phone}, message: {sms}'
        return text


my_phone = Phone()
print(my_phone)
print(my_phone.features)
my_phone.calling()
print(my_phone.send_sms('01768280237', 'You are very hard worker person'))