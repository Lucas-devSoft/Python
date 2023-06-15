import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from colores import *
from errores import Error_Respuesta
from menu_desplazamiento import Menu_de_reconfirmacion


hosting = smtplib.SMTP(host="smtp.gmail.com", port=587)
hosting.starttls()


def Cuenta_de_acceso():

    try:

        print(f"{marco+fondo}█                                                                                       █{fin}")
        Correo_electronico = input(
            f"{marco+fondo}█                 {texto}Ingrese su cuenta de gmail : {fin}      ")
        print(f"{marco+fondo}█                                                                                       █{fin}")
        Contrasena = input(
            f"{marco+fondo}█ {texto}Ingrese la clave de 16 digitos para uso de app de terceros : {fin}      ")

        cuenta = hosting.login(user=f"{Correo_electronico}",
                               password=f"{Contrasena}",
                               initial_response_ok=True)

        if cuenta[0] == 235:

            return Correo_electronico

        else:

            return cuenta[0]

    except smtplib.SMTPAuthenticationError as e:

        return e.args[0]

    except smtplib.SMTPException as e:

        return e.args[0]


def Envio_del_mensaje(Correo_electronico, Datos: dict):

    try:

        Asunto = "Envio de Formularios"
        Nombre_remitente = input(
            f"{marco+fondo}█           {texto}Ingrese su nombre de remitente: {fin}   ")
        print(f"{marco+fondo}█                                                                                       █{fin}")
        Destinatario = input(
            f"{marco+fondo}█       {texto}Ingrese el correo del destinatario: {fin}   ")
        print(f"{marco+fondo}█                                                                                       █{fin}")

        Datos_personales = Datos.get("Datos Personales")
        Datos_laborales = Datos.get("Datos Laborales")
        Datos_academicos = Datos.get("Datos Académicos")

        Resultado = f"""
        <html>
        <head></head>
        <body>
        <div style="text-align: center;">
            <h1 style="color: #333;">Datos Personales</h1>
            <p style="font-size: 16px;">{str(Datos_personales).replace("{","").replace("}","").replace("'","").replace(",","<br>").replace(".","",10)}</p>
        </div>
        <div style="text-align: center;">
            <h1 style="color: #333;">Datos Laborales</h1>
            <p style="font-size: 16px;">{str(Datos_laborales).replace("{","").replace("}","").replace("'","").replace(",","<br>").replace(".","",5)}</p>
        </div>
        <div style="text-align: center;">
            <h1 style="color: #333;">Datos Académicos</h1>
            <p style="font-size: 16px;">{str(Datos_academicos).replace("{","").replace("}","").replace("'","").replace(",","<br>").replace(".","",5)}</p>
        </div>
        </body>
        </html>
        """

        Mensaje = Resultado

        mime = MIMEMultipart()

        mime["Subject"] = f"{Asunto}"
        mime["From"] = f"{Nombre_remitente}"
        mime["To"] = f"{Destinatario}"
        mime.attach(MIMEText(f"{Mensaje}", "html"))

        print(f"{marco+fondo}█       {texto}Se enviara el mensaje a la casilla de correo : {texto_correcto}{Destinatario:^20}    {fin+marco}█{fin}")
        retorno_reconfirmacion = Menu_de_reconfirmacion()

        if retorno_reconfirmacion == "si":

            hosting.sendmail(from_addr=f"{Correo_electronico}",
                             to_addrs=f"{Destinatario}", msg=mime.as_string())

            hosting.quit()

            return True

        elif retorno_reconfirmacion == "no":

            pass

        else:

            Error_Respuesta()  # errores.py

    except smtplib.SMTPException as e:

        return False
