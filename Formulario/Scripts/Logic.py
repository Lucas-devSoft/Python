from datetime import date
from Errors import *
import re, os

def clear_console():

    command = 'clear'
    
    if os.name in ('nt', 'dos'):  # if the machine running in windows, use command cls
    
        command = 'cls'
    
    else:
        
        command
    
    os.system(command)
                
def option_A():
    
    print                                                                                        ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
    print                                                                                        ( '        │--------------->  YOU ARE IN FORMULARY OF DATA PERSONAL  <-----------------│')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤')    
    print                                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │') 
    print                                                                                        ( '        │              ║     YOU ARE A HEAD IN YOUR FAMILY? YES/NO    ║             |')
    print                                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
    Boss                                                               =            input        ( '        │              ║                   ').upper()
    
    if Boss == 'YES' or Boss == 'NO':
    
        print                                                                                    ( '        │              ╔══════════════════════════════════════════════╗             │')
        print                                                                                    ( '        │              ║              INSERT YOUR NAME                ║             |')
        print                                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
        Name                                                                     =        input  ( '        │              ║                   ').upper()
        
        verification = re.search(r"[0-9]+",Name)
        
        if len(Name) > 3 and not verification:                
            
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')                                                                                                  
            print                                                                                ( '        │              ║              INSERT YOUR LASTNAME            ║             |')
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
            LastName                                                               =        input( '        │              ║                   ').upper()

            verification = re.search(r"[0-9]+",LastName)
            
            if len(LastName) > 3 and not verification:

                print                                                                            ( '        │              ╠════════════════════════╦═════════════════════╣             │') 
                print                                                                            ( '        │              ║     UNMARRIED < U >    ║     MARRIED < M >   ║             │')
                print                                                                            ( '        │              ╠════════════════════════╩═════════════════════╣             │') 
                print                                                                            ( '        │              ║      DIVORCED < D >    ║     WIDOWED < W >   ║             │')
                print                                                                            ( '        │              ╠════════════════════════╩═════════════════════╣             │') 
                print                                                                            ( '        │              ║           INSERT YOUR MARITAL STATUS         ║             |')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │') 
                Marital_Status                                                 =            input( '        │              ║                   ').upper()
        
                if Marital_Status == 'U' or Marital_Status == 'M' or Marital_Status == 'D' or Marital_Status == 'W':
            
                    match Marital_Status:
                        
                        case 'U':

                            Marital_Status = 'UNMARRIED'

                        case 'M':

                            Marital_Status = 'MARRIED'

                        case 'D':

                            Marital_Status = 'DIVORCED'

                        case 'W':

                            Marital_Status = 'WIDOWED'

                    try:                          
                        
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        print                                                                    ( '        │              ║          INSERT YOUR DATE OF BIRTH           ║             |')
                        print                                                                    ( '        │              ╠══════════════════════════════╦═══════════════╣             │') 
                        Date_Birth                                       = date       ( int(input( '        │              ║            (1 - 9999) YEAR   ║        ')),
                                                                                        int(input( '        │              ║            (1 - 12)   MONTH  ║        ')),
                                                                                        int(input( '        │              ║            (1 - 31)   DAY    ║        ')))
                        
                        fecha_actual = date.today()
                        age = fecha_actual.year - Date_Birth.year
                        
                    except ValueError: 
                        
                        Message_Error_DataBirth()
                        
                        return False
                         
                    print                                                                        ( '        │              ╠══════════════════════════════╩═══════════════╣             │') 
                    print                                                                        ( '        │              ║          INSERT YOUR NATIONALITY             ║             |')
                    print                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │') 
                    Nationality                                               =            input ( '        │              ║                   ').upper()
                        
                    verification = re.search(r"[0-9]+",Nationality)
                    
                    if len(Nationality) > 4 and not verification:
                    
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        print                                                                    ( '        │              ║          INSERT YOUR CITY / PROVINCE         ║             |')
                        print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                        City                                                 =            input  ( '        │              ║                   ').upper()

                        verification = re.search(r"[0-9]+",City)
                        
                        if len(City) > 4 and not verification:
                    
                            
                            print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
                            print                                                                ( '        │              ║              INSERT YOUR LOCALITY            ║             |')
                            print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
                            Locality                                          =            input ( '        │              ║                   ').upper()    
                            
                            verification = re.search(r"[0-9]+",Locality)

                            if len (Locality) > 4 and not verification : 
                                
                                print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                print                                                            ( '        │              ║              INSERT YOUR ZIP CODE            ║             |')
                                print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                Zip_code                              =           input          ( '        |              ║                   ')         

                                if len(Zip_code) > 3 :
                                
                                    print                                                        ( '        │              ╠════════════════╦════════════════╦════════════╣             │') 
                                    print                                                        ( '        │              ║   MALE < M >   ║  FEMALE < F >  ║ OTHER < O >║             │')
                                    print                                                        ( '        │              ╠════════════════╩════════════════╩════════════╣             │') 
                                    print                                                        ( '        │              ║             INSERT YOUR GENDER               ║             │')
                                    print                                                        ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                    Gender                                 =           input     ( '        |              ║                   ').upper() 
                                    
                                    if Gender == 'M' or Gender == 'F' or Gender == 'O':
                                        
                                        match Gender:
                                            
                                            case 'M':

                                                Gender = 'MALE'

                                            case 'F': 

                                                Gender = 'FEMALE'

                                            case 'O':

                                                Gender = 'OTHER GENDER'  
                                                
                                        print                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                        print                                                    ( '        │              ║           INSERT YOUR PHONE NUMBER           ║             │')
                                        print                                                    ( '        │              ╠══════════════════════════════════════════════╣             │') 
                                        Phone                             =           input      ( '        |              ║                   ') 
                                        
                                        verification = re.search(r"[0-9]+",Phone)
                                        
                                        if not verification:
                                            
                                            Message_Error_Phone()
                                            
                                            return False
                                        
                                        else:
                                            
                                            pass
                                    
                                    else:
                                        
                                        Message_Error_Gender()
                                        
                                        return False
                                    
                                else:
                                    
                                    Message_Error_Zip_Code()
                                    
                                    return False
                                
                            else:
                                
                                Message_Error_Locality()
                                
                                return False
                
                        else:
                            
                            Message_Error_City()
                            
                            return False                    
                                                            
                    else:
                        
                        Message_Error_Nationality()
                        
                        return False                        
                
                else:
                    
                    Message_Error_Marital_Status()
                    
                    return False
                                            
            else:
                
                Message_Error_LastName()
                
                return False
                                            
        else:
            
            Message_Error_Name()
            
            return False                                    
    
    else:
        
        Message_Error_Boss()
        
        return False 
    
    return Boss, Name, LastName, Marital_Status, Date_Birth, age, Nationality, City, Locality, Zip_code, Gender, Phone                   
     
def option_B(): 
                                
    print                                                                                    ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
    print                                                                                    ( '        │--------------->   YOU ARE ON THE FORM ABOUT YOUR WORK   <-----------------│')
    print                                                                                    ( '        ├───────────────────────────────────────────────────────────────────────────┤') 
    print                                                                                    ( '        │              ╔══════════════════════════════════════════════╗             │')                              
    print                                                                                    ( '        │              ║       IS CURRENTLY WORKING < YES / NO >      ║             |')
    print                                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
    work                                                                =          input     ( '        |              ║                   ').upper()
       
    if work == 'YES':
            
        print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │') 
        print                                                                                ( '        │              ║            INSERT THE COMPANY NAME           ║             |')
        print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
        Company_Name                                                 =            input      ( '        |              ║                   ').upper()
        
        verification = re.search(r"[0-9]+",Company_Name)
        
        if len(Company_Name) > 5 and not verification:
            
            print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
            print                                                                            ( '        │              ║       INSERT THE TAX ID NUMBER COMPANY       ║             |')
            print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
            Company_Cuit                                                   =     input       ( '        |              ║                   ')

            verification = re.search(r"[0-9.]+",Company_Cuit)
            
            if len(Company_Cuit) == 13 and verification:
                
                print                                                                        ( '        │              ╠═══════════════╦════════════╦═════════════════╣             │')
                print                                                                        ( '        │              ║   FULL < F >  ║ PART < P > ║ FREELANCER < F >║             │')
                print                                                                        ( '        │              ╠═══════════════╩════════════╩═════════════════╣             │')  
                print                                                                        ( '        │              ║             INSERT YOUR WORK TIME            ║             |')
                print                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
                Working_Time                                            =        input       ( '        |              ║                   ').upper()
            
                if Working_Time == 'C' or Working_Time == 'M' or Working_Time == 'F':
                    
                    match Working_Time:
                        
                        case 'C':
                            Working_Time = 'FULL TIME'
                            
                        case 'M':
                            Working_Time = 'PART TIME'
                            
                        case 'F':
                            Working_Time = 'FREELANCER'
                    
                    print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                    print                                                                    ( '        │              ║           INSERT YOUR AREA OF WORK           ║             |')
                    print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
                    area                                                 =        input      ( '        |              ║                   ').upper()
                    
                    verification = re.search(r"[0-9]+",area)
                    
                    if len (area) > 5 and not verification:
                        
                        try:
                            
                            print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')                           
                            print                                                            ( '        │              ║          INSERT YOUR SALARY IN BRUTOS        ║             |')
                            print                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                            salary                                         =    float(input  ( '        |              ║                   '))
                            
                        except ValueError:
                            
                            Message_Error_Salary()
                            
                            return False
                                                                                            
                    else:
                        
                        Message_Error_area()
                        
                        return False                           
                else:
                    
                    Message_Error_WorkingTime()
                    
                    return False                                                                                         
            else:
                
                Message_Error_CompanyCuit()
                
                return False
        else:
                
            Message_Error_Job()
            
            return False
                                                                                                
    elif work == 'NO':
        
        Company_Name    = 'N/A'
        Company_Cuit    = 'N/A'
        Working_Time    = 'N/A'
        area            = 'N/A'                                           
        salary          =  0.0                                   
                 
    else:
        
        Message_Error_Job()
         
        return False 
        
    return work, Company_Name, Company_Cuit, Working_Time, area, salary
    
def option_C():
                                                    
    print                                                                                        ( '        ┌───────────────────────────────────────────────────────────────────────────┐')
    print                                                                                        ( '        │--------------->  YOU ARE IN THE FORM ABOUT YOUR ACADEMY  <----------------│')
    print                                                                                        ( '        ├───────────────────────────────────────────────────────────────────────────┤') 
    print                                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │')  
    print                                                                                        ( '        |              ║    YOU ARE A STUDENT GRADUATE  < YES / NO >  ║             |')
    print                                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
    graduate                                                                    =      input     ( '        |              ║                  ').upper()

    if graduate == 'YES':
                
        print                                                                                    ( '        │              ╔══════════════════════════════════════════════╗             │')  
        print                                                                                    ( '        |              ║   INSERT NAME OF INSTITUTE WHERE GRADUATE    ║             |')
        print                                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
        Name_Institute                                                 =           input         ( '        |              ║   ').upper()                                                                                   

        verification = re.search(r"[a-zA-Z\s]+[0-9]+",Name_Institute)
        
        if verification and len(Name_Institute) > 5 :

            print                                                                                ( '        │              ╠═══════════════════════╦══════════════════════╣             │')
            print                                                                                ( '        │              ║      SECONDARY < S >  ║     TERTIARY < T >   ║             │')
            print                                                                                ( '        │              ╠═══════════════════════╬══════════════════════╣             │')
            print                                                                                ( '        │              ║     UNIVERCITY < U >  ║ TEACHING STAFF < TS >║             |')
            print                                                                                ( '        │              ╠═══════════════════════╩══════════════════════╣             │')      
            print                                                                                ( '        |              ║        INSERT THE RANK TO GRADUATION         ║             |')
            print                                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
            rank_academic                                                =           input       ( '        |              ║                  ').upper()                                       

            match rank_academic:

                case 'S':
                    
                    rank_academic = 'SECONDARY'
                
                case 'T':

                    rank_academic = 'TERTIARY'

                case 'F':

                    rank_academic = 'UNIVERCITY'
                
                case 'P':

                    rank_academic = 'TEACHING STAFF'

            if rank_academic == 'S' or rank_academic == 'T' or rank_academic == 'U' or rank_academic == 'TS': 
            
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                print                                                                            ( '        │              ║           INSERT THE YEAR OF ENTRY           ║             │')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                Entry                                                          =     input       ( '        │              ║                    ')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                print                                                                            ( '        │              ║          INSERT THE YEAR OF GRADUATION       ║             │')
                print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
                Graduation                                                     =     input       ( '        |              ║                    ')
                                     
            else:
                    
                Message_Error_RankAcademic()
                
                return False                   
        else:
                
            Message_Error_NameInstitute()   
            
            return False         
                
    elif graduate == 'NO':
        
        Name_Institute      = 'N/A'
        rank_academic       = 'N/A'
        Entry               = '0'
        Graduation          = '0'
    
    
        
    print                                                                            ( '        │              ╔══════════════════════════════════════════════╗             │')  
    print                                                                            ( '        |              ║    YOU ARE CURRENTLY STUDING  < YES / NO >   ║             |')
    print                                                                            ( '        │              ╠══════════════════════════════════════════════╣             │')
    Student                                                        =      input      ( '        |              ║                  ').upper()
    
    if Student == 'YES':
    
        print                                                                        ( '        │              ╔══════════════════════════════════════════════╗             │')  
        print                                                                        ( '        |              ║   INSERT NAME OF INSTITUTE WHERE GRADUATE    ║             |')
        print                                                                        ( '        │              ╠══════════════════════════════════════════════╣             │')
        Institute                                                 =       input      ( '        |              ║   ').upper()                                                                                   

        verification = re.search(r"[a-zA-Z\s]+[0-9]+",Institute)
        
        if verification and len(Institute) > 5 :

            print                                                                    ( '        │              ╠═══════════════════════╦══════════════════════╣             │')
            print                                                                    ( '        │              ║      SECONDARY < S >  ║     TERTIARY < T >   ║             │')
            print                                                                    ( '        │              ╠═══════════════════════╬══════════════════════╣             │')
            print                                                                    ( '        │              ║     UNIVERCITY < U >  ║ TEACHING STAFF < TS >║             |')
            print                                                                    ( '        │              ╠═══════════════════════╩══════════════════════╣             │')      
            print                                                                    ( '        |              ║        INSERT THE RANK TO GRADUATION         ║             |')
            print                                                                    ( '        │              ╠══════════════════════════════════════════════╣             │')
            Academic                                               =          input  ( '        |              ║                  ').upper()                                       

            match Academic:

                case 'S':
                    
                    Academic = 'SECONDARY'
                
                case 'T':

                    Academic = 'TERTIARY'

                case 'F':

                    Academic = 'UNIVERCITY'
                
                case 'P':

                    Academic = 'TEACHING STAFF'
                        
            if Academic == 'S' or Academic == 'T' or Academic == 'U' or Academic == 'TS':
                            
                print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
                print                                                                ( '        │              ║           INSERT THE YEAR OF ENTRY           ║             │')
                print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
                Entry_currently                             =     input              ( '        │              ║                    ')
                print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
                print                                                                ( '        │              ║      INSERT APPROXIMATE GRADUATION YEAR      ║             │')
                print                                                                ( '        │              ╠══════════════════════════════════════════════╣             │')
                Graduation_currently                        =     input              ( '        |              ║                    ')

                verification_1 = re.search(r"[0-9]+",Entry_currently)
                verification_2 = re.search(r"[0-9]+",Graduation_currently)

                if verification_1 and verification_2 and len(Entry_currently) == 4 and len(Graduation_currently) == 4:
                    
                    pass
                
                else:
                    
                    Message_Error_Year()
                    
                    return False 
                                                        
            else:
                
                Message_Error_Academic()
                
                return False
                                    
        else:
            
            Message_Error_Institute()
            
            return False

    elif Student == 'NO':
        
        Institute            = 'N/A'
        Academic             = 'N/A'
        Entry_currently      = '0'
        Graduation_currently = '0'
            
    else:
            
        Message_Error_Graduate()

        return False
    
    return graduate, Name_Institute, rank_academic, Entry, Graduation, Student, Institute, Academic, Entry_currently, Graduation_currently 