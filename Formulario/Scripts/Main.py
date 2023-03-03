from Logic import *
from MongoDB import *

status_A ='INCOMPLETE'
status_B ='INCOMPLETE'
status_C ='INCOMPLETE'

cont = 0

while True:

    MongoConnection()

    clear_console()
    print('\n\n')
    
    print                                                                   ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
    print                                                                   ( '        │            ╔═════════════════════════════════════════════════╗            │')
    print                                                                   ( '        │            ║ PYTHON - FORMULARIES WITH SAVE INFO IN MONGODB  ║            │')
    print                                                                   ( '        │            ╚═════════════════════════════════════════════════╝            │')   
    print                                                                   ( '        │                                                                           │')
    print                                                                   ( '        │            ╔════════════════════════════════════╦════════════╗            │')
    print                                                                   (f'        │            ║ A ► FORMULARY OF PERSONAL DATA     ║ {status_A} ║            │')
    print                                                                   ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                   (f'        │            ║ B ► FORMULARY OF JOB DATA          ║ {status_B} ║            │')
    print                                                                   ( '        │            ╠════════════════════════════════════╬════════════╣            │')
    print                                                                   (f'        │            ║ C ► FORMULARY OF ACADEMIC DATA     ║ {status_C} ║            │')
    print                                                                   ( '        │            ╚════════════════════════════════════╩════════════╝            │')
    print                                                                   ( '        |                                                                           |')
    print                                                                   ( '        │            ╔═════════════════════════════════════════════════╗            │')
    print                                                                   ( '        │            ║ PLEASE CHOISE THE OPTION YOU GOING TO COMPLETE  ║            │')
    print                                                                   ( '        │            ╚═════════════════════════════════════════════════╝            │')
    option = input                                                          ( '\t\t\t\t\t      ').upper()
                
    if option == 'A' and not status_A == ' COMPLETE ':
    
        clear_console()
        
        print('\n\n')
        
        return_A = option_A()
        
        if return_A: 
            
            global Boss,Name,LastName,Marital_Status,Date_Birth,age,Nationality,City,Locality,Zip_code,Gender,Phone
            
            Boss            = return_A[0]
            Name            = return_A[1]
            LastName        = return_A[2]
            Marital_Status  = return_A[3]
            Date_Birth      = str(return_A[4])
            age             = return_A[5]
            Nationality     = return_A[6]
            City            = return_A[7]
            Locality        = return_A[8]
            Zip_code        = return_A[9]
            Gender          = return_A[10]
            Phone           = return_A[11]
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │                 THE FORMULARY IS SUCCESFULLY COMPLETE                     │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             BACK TO MENU  < M >     │    < S >  EXIT THE PROGRAM          │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back =                                            input ('\t\t\t\t\t      ').upper()
            
            if back == 'M':
                
                status_A = ' COMPLETE '
                
                continue
            
            elif back == 'S':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()
            
        else:
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │        THE FORM WAS INTERRUPTED FOR PROVIDING ERRONEOUS INFORMATION       │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             TRY AGAIN  < T >        │     < E >  EXIT THE PROGRAM         │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                            ( '\t\t\t\t\t      ').upper()
            
            
            if back == 'T':
                
                status_A = 'INCOMPLETE'
                
                continue
                
            elif back == 'E':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()

    elif option == 'B' and not status_B == ' COMPLETE ':

        clear_console() 
        print('\n\n')
    
        return_B = option_B()
        
        if return_B: 
                    
            global work,Company_Name,Company_Cuit,Working_Time,area,salary         
                    
            work                = return_B[0]
            Company_Name        = return_B[1]
            Company_Cuit        = return_B[2]
            Working_Time        = return_B[3]
            area                = return_B[4]
            salary              = return_B[5]
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │                 THE FORMULARY IS SUCCESFULLY COMPLETE                     │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             BACK TO MENU  < M >     │    < S >  EXIT THE PROGRAM          │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back =                                            input ('\t\t\t\t\t      ').upper()
            
            if back == 'M':
                
                status_B = ' COMPLETE '
                
                continue
            
            elif back == 'S':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()
            
        else:
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │        THE FORM WAS INTERRUPTED FOR PROVIDING ERRONEOUS INFORMATION       │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             TRY AGAIN  < T >        │     < E >  EXIT THE PROGRAM         │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                            ( '\t\t\t\t\t      ').upper()
            
            if back == 'T':
                
                status_B = 'INCOMPLETE'
                
                continue
                
            elif back == 'E':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()

    elif option == 'C' and not status_C == ' COMPLETE ':
        
        clear_console() 
        print('\n\n')
    
        return_C = option_C()
        
        if return_C: 
                    
            global graduate,Name_Institute,rank_academic,Entry,Graduation,Student,Institute,Academic,Entry_currently,Graduation_currently         
                    
            graduate                    = return_C[0]
            Name_Institute              = return_C[1]
            rank_academic               = return_C[2]
            Entry                       = return_C[3]
            Graduation                  = return_C[4]
            Student                     = return_C[5]
            Institute                   = return_C[6]
            Academic                    = return_C[7]
            Entry_currently             = return_C[8]
            Graduation_currently        = return_C[9]
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │                 THE FORMULARY IS SUCCESFULLY COMPLETE                     │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             BACK TO MENU  < M >     │    < S >  EXIT THE PROGRAM          │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back =                                            input ('\t\t\t\t\t      ').upper()
            
            if back == 'M':
                
                status_C = ' COMPLETE '
                
                continue
            
            elif back == 'S':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()
            
        else:
            
            print                                                   ( '        │              ╚══════════════════════════════════════════════╝             │')
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │        THE FORM WAS INTERRUPTED FOR PROVIDING ERRONEOUS INFORMATION       │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             TRY AGAIN  < T >        │     < E >  EXIT THE PROGRAM         │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            back = input                                            ( '\t\t\t\t\t      ').upper()
            
            if back == 'T':
                
                status_C = 'INCOMPLETE'
                
                continue
                
            elif back == 'E':
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()

    else: 
        
        if option == 'A' and status_A in ' COMPLETE ' or  option == 'B' and status_B in ' COMPLETE ' or option == 'C' and status_C in ' COMPLETE ':
            
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   (f'        |                   THE FORM {option} HAS ALREADY BEEN COMPLETED                   |')
            print                                                   ( '        └───────────────────────────────────────────────────────────────────────────┘')
            input  ()    
        
        elif status_A in ' COMPLETE ' and status_B in ' COMPLETE ' and status_C in ' COMPLETE ':          
            
            cont += 1
           
            Personal_data = {   "_id"                     : str(cont),
                                "HEAD IN YOUR FAMILY"     : Boss,
                                "NAME"                    : Name,
                                "LASTNAME"                : LastName,
                                "MARITAL_STATUS"          : Marital_Status,
                                "DATE_BIRTH"              : Date_Birth,
                                "AGE"                     : age,
                                "NATIONALITY"             : Nationality,
                                "CITY"                    : City,
                                "LOCALITY"                : Locality,
                                "ZIP CODE"                : Zip_code,
                                "GENDER"                  : Gender,
                                "PHONE NUMBER"            : Phone, 
                                "IS CURRENTLY WORKING"    : work,
                                "COMPANY_NAME"            : Company_Name,
                                "TAX_ID_COMPANY"          : Company_Cuit,
                                "JORNAL_TIME"             : Working_Time,
                                "AREA_WORK"               : area,
                                "SALARY"                  : salary,
                                "IS A GRADUATE STUDENT"   : graduate,
                                "INSTITUTE_NAME"          : Name_Institute,
                                "RANK ACADEMIC"           : rank_academic,
                                "YEAR OF ENTRY"           : Entry,
                                "YEAR OF GRADUATE"        : Graduation,
                                "IS STUDY CURRENTLY"      : Student,
                                "NAME INSTITUT CURRENT"   : Institute,
                                "RANK ACADEMIC CURRENT"   : Academic,
                                "YEAR ENTRY"              : Entry_currently,
                                "YEAR APROXIMATE GRADUATE": Graduation_currently}                
                
            MongoInsert(Personal_data)    
                    
            print                                                   ( '        ├───────────────────────────────────────────────────────────────────────────┤')
            print                                                   ( '        │                CONGRATULATIONS ALL FORMS HAVE BEEN COMPLETED              │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │           RESET ALL FORMS  < R >    │    < E >  EXIT THE PROGRAM          │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            reset = input                                           ( '\t\t\t\t\t      ').upper()

            if reset == 'R':
                
                status_A = 'INCOMPLETO'
                status_B = 'INCOMPLETO'
                status_C = 'INCOMPLETO'
                
                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               (f'        │    HI {Name.capitalize()}, ¿ DO YOU WANT TO SEE YOUR SAVED INFORMATION ?  │')
                print                                               ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                print                                               ( '        │           YES, I WANT  < YES >      │    < N0 >  NO, I WANT NOT           │')
                print                                               ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
                request = input                                     ( '\t\t\t\t\t      ').upper()
                
                if request == 'YES':
                    
                    MongoShow()
                    input()
                
                elif request == 'NO':
                    
                    continue
                
                else:
                    
                    print('pasa por el pass')
                    input()
                    pass
            
            elif reset == 'E':
                
                print                                           ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                           ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                           ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                           ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                           ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                           ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()     
            
            else:
            
                Message_Error_Reset()
                input()  
                
        else:
            
            clear_console()
            print('\n\n') 

            print                                                   ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
            print                                                   ( '        │                                                                           │')
            print                                                   ( '        │              ╔═════════════════════════════════════════════╗              │')
            print                                                   ( '        │              ║    THE OPTION CHOICE IS NOT IN THE MENU     ║              │')
            print                                                   ( '        │              ╚═════════════════════════════════════════════╝              │')
            print                                                   ( '        │                                                                           │')
            print                                                   ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
            print                                                   ( '        │             TRY AGAIN  < T >        │     < E >  EXIT THE PROGRAM         │')
            print                                                   ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
            question = input                                        ( '\t\t\t\t\t      ').upper()

            if question == 'T':
                    
                continue

            elif question == 'E':

                print                                               ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                print                                               ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                print                                               ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                print                                               ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                print                                               ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                input                                               ( '        └───────────────────────────────────────────────────────────────────────────┘')
                
                exit()
            
            else:
                
                print                                               ( '        │              ╔═════════════════════════════════════════════╗              │')
                print                                               ( '        │              ║    THE ANSWER WAITED IS < T > OR < E >      ║              │')
                print                                               ( '        │              ╚═════════════════════════════════════════════╝              │')
                print                                               ( '        ├─────────────────────────────────────┬─────────────────────────────────────┤')
                print                                               ( '        │             TRY AGAIN  < T >        │     < E >  EXIT THE PROGRAM         │')
                print                                               ( '        └─────────────────────────────────────┴─────────────────────────────────────┘')
                question = input                                    ( '\t\t\t\t\t      ').upper()
                
                if question == 'T':
                    
                    continue

                elif question == 'E':

                    print                                           ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
                    print                                           ( '        │       ╔══════════════════════════════════════════════════════════╗        │')
                    print                                           ( '        │       ║          THANK YOU FOR USE MY PERSONAL PROJECT           ║        │')
                    print                                           ( '        │       ║             PRESS ENTER TO EXIT THE PROGRAM              ║        │')
                    print                                           ( '        │       ╚══════════════════════════════════════════════════════════╝        │')
                    input                                           ( '        └───────────────────────────────────────────────────────────────────────────┘')
                    
                    exit()  