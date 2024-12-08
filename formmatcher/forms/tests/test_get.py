import requests

url = 'http://127.0.0.1:8000/get_form'

user_regisration_form = {
    'username': 'testuser',
    'email': 'testuser@example.com',
    'password': 'password123',
    'birthdate': '1990-01-01'
}

contact_form = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'phone': '+7 123 456 78 90',
    'message': 'Hello, I have a question.'
}

order_form = {
    'customer_name': 'Alice',
    'email': 'alice@example.com',
    'phone': '+7 123 456 78 90',
    'order_date': '2023-12-01'
}

feedback_form = {
    'username': 'feedbackuser',
    'email': 'feedbackuser@example.com',
    'feedback': 'Great service!',
    'submission_date': '2023-12-01'
}

appointment_form = {
    'patient_name': 'Bob Smith',
    'email': 'bobsmith@example.com',
    'phone': '+7 123 456 78 90',
    'appointment_date': '2023-12-01'
}

response = [requests.post(url, data=user_regisration_form), 
            requests.post(url, data=contact_form),
            requests.post(url, data=order_form),
            requests.post(url, data=feedback_form),
            requests.post(url, data=appointment_form),
            ]
for i in response:
    print(i.json())  # -> {'template_name': 'User Registration Form'}
                        # {'template_name': 'Contact Form'}
                        # {'template_name': 'Order Form'}
                        # {'template_name': 'Feedback Form'}
                        # {'template_name': 'Appointment Form'}
