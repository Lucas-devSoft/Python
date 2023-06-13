import smtplib
from email.mime.text import MIMEText

from colores import *

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

        hosting.login(user=f"{Correo_electronico}",
                      password=f"{Contrasena}",
                      initial_response_ok=True)

        return Correo_electronico

    except smtplib.SMTPAuthenticationError as e:

        return e.args[0]

    except smtplib.SMTPException as e:

        return e.args[0]


def Enviar_Mensaje(retorno_correo):

    Correo_electronico = retorno_correo

    Asunto = input(
        f"{marco+fondo}█           {texto}Ingrese el asunto de su mensaje: {fin}")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Nombre_remitente = input(
        f"{marco+fondo}█           {texto}Ingrese su nombre de remitente: ")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Destinatario = input(
        f"{marco+fondo}█           {texto}Ingrese el correo del destinatario: ")
    print(f"{marco+fondo}█                                                                                       █{fin}")
    Mensaje = input(f"{marco+fondo}█           {texto}Ingrese su mensaje:  ")

    mime = MIMEText(Mensaje)

    mime["Subject"] = f"{Asunto}"
    mime["From"] = f"{Nombre_remitente}"
    mime["To"] = f"{Destinatario}"

    hosting.sendmail(from_addr=f"{Correo_electronico}",
                     to_addrs=f"{Destinatario}", msg=mime.as_string())
