def main():
    input_string = input("EQUIPO A INSTALAR: ")
    if input_string == "Radios":
        string = "Radio ALOHA AFIG Total 6,\n1. 6 Lug 90',\n2. Heat Shrink,\n3. 80FT Ground #6,\n4. lugs for bussbar Total 12,\n5. bussbar Total 3,\n6. Hibrid Jumpers total 3,\n7 Ret-cable total Total3"
        print(string)
    
        input_string = input("EQUIPO A INSTALAR: ")
    elif input_string == "Antenas": 
        string = "Antena 65C 8 puertos total 3, \n1. RF Jumpers mimi to mimi Total 32 \n2. Snapping Total 180, \n3. 3 way Total 10 \n4. \n4.Angle Adapter"
        print(string)
        
        input_string = input("EQUIPO A INSTALAR: ")
    elif input_string == "AEHC": 
        string = "5G Antena 3 Total, \n1. Hybrid Jumpers Total 3, \n2. Lugs 90' Total 3, \n3. ground #2 Total 30FT"
        print(string)
        
        input_string = input("EQUIPO A INSTALAR: ")
    elif input_string == "Booster": 
        string = "Booster PSU/ \n1. lug para cable grueso #3"
        print(string)
        
        input_string = input("EQUIPO A INSTALAR: ")
    elif input_string == "Router": 
        string = "7250_ixr, \n1. Tarjetas  SFP, \n2. cables HDMI "
        print(string)
        
        input_string = input("EQUIPO A INSTALAR: ") 
    elif input_string == "OVP": 
        string = "Raycap, \n1. Liquid counduit \n2. cup, \n3. Ground #6"
        print(string)
        
        input_string = input("EQUIPO A INSTALAR: ") 
    elif input_string == "Caja de Alarmas": 
        string = "Caja de alarma,  \n1. mucho cut 5"
        print(string) 
        
        input_string = input("EQUIPO A INSTALAR: ") 
    elif input_string == "Reforzamiento": 
        string = "Reforzamiento,  \n1. todo el set"
        print(string) 
        
    else:
        print("Entrada no válida.")

if __name__ == '__main__':
    main()
