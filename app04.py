from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks!" #.value es una propiedad que se puede usar para cambiar el texto de un objeto Text

app = App("ICI App")


message = Text(app, text="Welcome to the ICI App!")
message_2 = Text(app) 

button = PushButton(app, text="Click me!", command=say_hello)


app.display()