from guizero import App, Text, PushButton, TextBox


app = App(title="ICI App")

def say_hello():
    app.info("Saludo", text = f"Hola {name.value}")
    #message_2.value = "Hola " + name.value 


message = Text(app, text="Como te llamas?", color="blue")
name = TextBox(app, width=30)

message_2 = Text(app, color="red")
button = PushButton(app, text="Click me!", command=say_hello)


app.display()