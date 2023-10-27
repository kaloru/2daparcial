from guizero import App, Text, PushButton, TextBox


app = App(title="ICI Suma de 2 Numeros")

def sumar ():
   
    app.info("Suma", text= f"La suma es {int (n1.value) + int(n2.value)}")


message_n1 = Text(app, text= "Introduce el primer numero")
n1 = TextBox(app)

message_n2 = Text(app, text= "Introduce el segundo numero")
n2 = TextBox(app)

button = PushButton(app, text= "Sumar", command=sumar)

app.display()