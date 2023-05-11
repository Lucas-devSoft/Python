import math, os, time
from Colores import *

def Limpieza_consola():
    
    if os.name in ("nt", "dos"):  # si la maquina esta corriendo en Windows, use cls
        
        comando = "cls"
        os.system(comando)
    
    else:
    
        comando = "clear"
        os.system(comando)
    
def Mensaje_de_Agradecimiento():
    
    print()
                
    print                                      (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                      (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                      (f"                   {marco}║{fondo}                    {texto}Muchas gracias por probar mi programa.{fin+fondo}                     {fin+marco}║{fin}")
    print                                      (f"                   {marco}║{fondo}               {texto}El programa se cerrará automaticamente en 5 segundos.{fin+fondo}           {fin+marco}║{fin}")
    print                                      (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                      (f"                   {marco}╚═══════════════════════════════════════════════════════════════════════════════╝{fin}")
    
    time.sleep(5)
    
    exit()  

def Error_Mensaje_de_Nombre():
            
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                                       (f"                   {marco}║{fondo}          {fin+error_texto}Se detecto el campo vacío o con un formato de nombre inválido.{fin}{fondo}       {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
    print                                       (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}            {texto}Salir < salir >{fin+fondo}             {fin+marco}║{fin}")
    print                                       (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
    Opcion = input                              ("\n\t\t\t\t\t\t\t  ").lower()
    
    while Opcion != "volver" and Opcion != "salir":      
        
        print()
                
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                                   (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
        print                                   (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Opcion = input                          ("\n\t\t\t\t\t\t\t  ").lower()
    
    else: 
        
        if Opcion == "volver":
    
            pass

        elif Opcion == "salir":
                
            Mensaje_de_Agradecimiento()                 
                 
def Error_Mensaje_de_BD():
            
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}          {fin+error_texto}Respuesta invalida se espera < si > o < no > como respuesta.{fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
    print                                       (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
    print                                       (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
    Opcion = input                              ("\n\t\t\t\t\t\t\t  ").lower()
        
    while Opcion != "volver" and Opcion != "salir":
        
        print()
        
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        print                                   (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
        print                                   (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Opcion = input                          ("\n\t\t\t\t\t\t\t  ").lower()
    
    else: 
        
        if Opcion == "volver":
    
            pass

        elif Opcion == "salir":
            
            Mensaje_de_Agradecimiento()
    
def Error_Mensaje_de_Conexion():

    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                                       (f"                   {marco}║{fondo}          {fin+error_texto}Respuesta inválida se espera < 1 > o < 2 > como respuesta.{fin}{fondo}           {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
    print                                       (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
    print                                       (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}") 
    Opcion = input                              ("\n\t\t\t\t\t\t\t  ").lower()
    
    while Opcion != "volver" and Opcion != "salir":      
        
        print()
                
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}║{fondo}       {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}     {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
        print                                   (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
        print                                   (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Opcion = input                          ("\n\t\t\t\t\t\t\t  ").lower()
    
    else: 
        
        if Opcion == "volver":
    
            pass

        elif Opcion == "salir":
            
            Mensaje_de_Agradecimiento()
        
def Error_Mensaje_de_Menu():   
            
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}               {fin+error_texto}La Opción que elegiste no esta dentro del Menu{fin+fondo}                  {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
    print                                       (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
    print                                       (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
    Opcion = input                              ("\n\t\t\t\t\t\t\t  ").lower()

    while Opcion != "volver" and Opcion != "salir":
        
        print()
        
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin+fondo}      {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        print                                   (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}") 
        print                                   (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Opcion = input                          ("\n\t\t\t\t\t\t\t  ").lower()
        
    else:
                
        if Opcion == "volver":
            
            pass
        
        elif Opcion == "salir":
            
            Mensaje_de_Agradecimiento()

def Error_Mensaje_pre_Conexion():
        
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}          {fin+error_texto}Respuesta invalida se espera < si > o < no > como respuesta.{fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}") 
    print                                       (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
    print                                       (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
    Opcion = input                              ("\n\t\t\t\t\t\t\t  ").lower()
        
    while Opcion != "volver" and Opcion != "salir":
        
        print()
        
        print                                   (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}║{fondo}      {fin+error_texto}Respuesta inválida se espera < volver > o < salir > como respuesta.{fin}{fondo}      {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin}║{fin}")
        print                                   (f"                   {marco}╠══════════════════════════════════════╦════════════════════════════════════════╣{fin}")
        print                                   (f"                   {marco}║{fondo}     {texto}Volver a intentar < volver >{fin+fondo}     {fin+marco}║{fondo}           {texto}Salir < salir >{fin+fondo}              {fin+marco}║{fin}")
        print                                   (f"                   {marco}╚══════════════════════════════════════╩════════════════════════════════════════╝{fin}")
        Opcion = input                          ("\n\t\t\t\t\t\t\t  ").lower()
    
    else: 
        
        if Opcion == "volver":
    
            pass

        elif Opcion == "salir":
            
            Mensaje_de_Agradecimiento()
    
def option_A():

    Operador = " + "
    
    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                       {texto}A ► Adición{fin+fondo}                        {fin+marco}║{fondo}        {texto}(+){fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")    
    Numero1 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el Primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el Segundo Valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado = Numero1 + Numero2
        
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}║{fondo}                {texto}El resultado de la adición es{fin+fondo}             {fin+marco}║{fin}          {Resultado}         {marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
                    
    return Numero1, Operador, Numero2, Resultado
    
def option_B():
    
    Operador = " - "

    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                       {texto}B ► Substracción{fin+fondo}                   {fin+marco}║{fondo}        {texto}(-){fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero1 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado = Numero1 - Numero2

    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}║{fondo}                {texto}El resultado de la Substracción es{fin+fondo}        {fin+marco}║{fin}          {Resultado}         {marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")       
        
    return Numero1, Operador, Numero2, Resultado    
            
def option_C():
    
    Operador = " * "

    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                       {texto}C ► Multiplicación{fin+fondo}                 {fin+marco}║{fondo}        {texto}(*){fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero1 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el primer valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))

    Resultado =  Numero1 * Numero2
        
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}║{fondo}           {texto}El resultado de la multiplicación es{fin+fondo}           {fin+marco}║{fin}          {Resultado}         {marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")       
        
    return Numero1, Operador, Numero2, Resultado

def option_D():
    
    Operador = " / "
    
    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                    {texto}D ► División{fin+fondo}                          {fin+marco}║{fondo}        {texto}(/){fin+fondo}         {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero1 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el primer Valor{fin+fondo}                   {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el segundo valor{fin+fondo}                  {fin+marco}║{fin}          "))
    
    Resultado = Numero1 / Numero2
        
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}║{fondo}              {texto}El resultado de la división es{fin+fondo}              {fin+marco}║{fin}         {Resultado:.2f}       {marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
    
    return Numero1, Operador, Numero2, Resultado

def option_E():
    
    Operador = " b/e "
    
    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                  {texto}E ► Exponentiation{fin+fondo}                      {fin+marco}║{fondo}        {texto}(b,e){fin+fondo}       {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")  
    Numero1 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el número base{fin+fondo}                    {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    Numero2 = int (input                        (f"                   {marco}║{fondo}                {texto}Inserte el número del exponente{fin+fondo}           {fin+marco}║{fin}          "))
    
    Resultado = Numero1 ** Numero2
    
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}║{fondo}         {texto}El resultado de la exponenciación es{fin+fondo}             {fin+marco}║{fin}         {Resultado}         {marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")    
    
    return Numero1, Operador, Numero2, Resultado    

def option_F():
    
    Operador = " √ "
    
    print                                       (f"                   {marco}╔══════════════════════════════════════════════════════════╦════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                    {texto}F ► Radicación{fin+fondo}                        {fin+marco}║{fondo}          {texto}(√){fin+fondo}       {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                          {fin+marco}║{fondo}                    {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")   
    Numero1 =  int (input                       (f"                   {marco}║{fondo}                {texto}Inserte el número base{fin+fondo}                    {fin+marco}║{fin}          "))
    
    if Numero1 > 0:
        
        print                                   (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")         
        Numero2 = int (input                    (f"                   {marco}║{fondo}                {texto}Inserte el número de la raíz{fin+fondo}              {fin+marco}║{fin}          "))
        
        if Numero2 > 0:
        
            Resultado = math.pow(Numero1,1/Numero2)
        
            print                               (f"                   {marco}╠══════════════════════════════════════════════════════════╬════════════════════╣{fin}")
            print                               (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
            print                               (f"                   {marco}║{fondo}             {texto}El resultado de la radicación es{fin+fondo}             {fin+marco}║{fin}         {Resultado:.2f}       {marco}║{fin}")
            print                               (f"                   {marco}║{fondo}                                                          {fin+marco}║                    ║{fin}")
            print                               (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")
    
    return Numero1, Operador, Numero2, Resultado 
    
def option_G():
    
    Operador = " Par o Impar "
    
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                              {texto}G ► Es Par o Impar{fin}                                  {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}") 
    
    Numero1 = int (input                        (f"                   {marco}║{fondo}               {texto}Inserte el número que quiere verificar{fin}                {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}") 
        
    Resultado = Numero1 % 2

    if Resultado == 0 :
        
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                     {texto}El ({Numero1}) esta dentro de los números pares.{fin}                      {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        
        Conclusión = " Par "
            
    else:
        
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                  {texto}El ({Numero1}) esta dentro de los números impares.{fin}                          {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        
        Conclusión = " Impar "
     
    return Numero1, Operador, Conclusión
            
def option_H():
    
    Operador = " Es un número primo? "

    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                            {texto}H ► Es un número primo ?{fin}                            {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}") 
           
    i=2
    cont = 0
    
    Numero1 = int (input                        (f"                   {marco}║{fondo}         {texto}Inserte el número que quiere verificar si es primo. {fin}          {fin+marco}║{fin}          "))
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╩════════════════════╣{fin}")

    while Numero1 > i and cont == 0:
        
        resto = Numero1 % i 
        
        if resto == 0:
            
            cont += 1
            
        i+=1
        
    if cont != 0 or Numero1 == 1 :
        
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                     {texto}El ({Numero1}) no esta dentro de los números primos{fin}                          {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        
        Conclusion = " No es un número primo"
        
    else:

        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                       {texto}El ({Numero1}) esta dentro de los números primos.{fin}                            {fin+marco}║{fin}")
        print                                   (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
        print                                   (f"                   {marco}╠═══════════════════════════════════════════════════════════════════════════════╣{fin}")
        
        Conclusion = " Es un número primo"
        
    return Numero1, Operador, Conclusion 
       
def option_I():

    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                          {texto}I ► Números primos por rango{fin}                              {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════╦════════════════════╣{fin}") 
        
    hasta = int (input                          (f"                   {marco}║{fondo}                      {texto}Inserte el número de rango que quiere ver en primos.{fin}                {fin+marco}║{fin}          ")) 
    
    primos = []
    
    for numero in range (2,hasta+1):
        
        esPrimo = True
        
        if numero == 2:
            
            primos.append(numero)
        
        else:
            
            i=2
            
            while i < (pow(numero,1/2) + 1):
                
                resto = numero % i
                
                if resto == 0:
                
                    esPrimo = False
                    
                    break
                
                i+=1
            
            if esPrimo == True:
                
                primos.append(numero)

    lugar = 1
    
    print                                       (f"                   {marco}╔═══════════════════════════════════════════════════════════════════════════════╗{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                          {texto}Listado de números primos{fin}                              {fin+marco}║{fin}")
    print                                       (f"                   {marco}║{fondo}                                                                               {fin+marco}║{fin}")
    print                                       (f"                   {marco}╠══════════════════════════════════════════════════════════════╦════════════════╣{fin}") 
    
    for primo in primos:
                   
        if lugar % 3 != 0:  
            
            print                                                   (f"                   {marco}║{fondo}{texto}{primo:^17} {fin}{fin+marco}║{fin}".rstrip(),end="") 
            
        else:
        
            print                                                   (f"{fondo}{texto}{primo:^16}{fin}{fin+marco}║{fin}".rstrip()) 

        lugar += 1
    
    print()