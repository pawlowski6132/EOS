# import requests
# import json
from guizero import App, Text, TextBox, PushButton, Slider

# response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
#     'field_offices': 'detroit'
# })
# data = json.loads(response.content)
# print(data['total'])
# print(data['items'][0]['title'])

def change_text_size(slider_value):
    welcome_message.size = slider_value

def say_my_name():
    welcome_message.value = my_name.value


app = App(title="Hello world")
welcome_message = Text(app, text = "Welcome little Mutha's", size=30, font="Times New Roman", color="blue")
my_name = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)


app.display()