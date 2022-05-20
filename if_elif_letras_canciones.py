from time import sleep
import os

while True:
    print('\n')
    print("""Generador de letras de canciones de Linkin Park

            A continuación escoja una canción. (1 a 10)

            1. Faint
            2. In the end
            3. New divide
            4. One more light
            5. Crawling
            6. Castle of glass
            7. Leave out all the rest
            8. Burn it down
            9. Papercut
            10.Breaking the habit
            
            *El orden no implica que una sea mejor que otra""")
    print('\n')
    try:
        eleccion = int(input('>>> '))
    except:
        os.system('cls')
        print('Solo las opciones numéricas dadas')
        sleep(1)
        continue
    if eleccion < 1 or eleccion > 10:
        os.system('cls')
        print('Elección fuera de rango')
        sleep(1)
        os.system('cls')
        continue
    elif eleccion == 1:
        with open('Faint.txt') as faint:
            os.system('cls')
            sleep(1)
            print(faint.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 2:
        with open('In the end.txt') as in_the_end:
            os.system('cls')
            sleep(1)
            print(in_the_end.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 3:
        with open('New divide.txt') as new_divide:
            os.system('cls')
            sleep(1)
            print(new_divide.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 4:
        with open('One more light.txt') as one_more_light:
            os.system('cls')
            sleep(1)
            print(one_more_light.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 5:
        with open('Crawling.txt') as crawling:
            os.system('cls')
            sleep(1)
            print(crawling.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 5:
        with open('Crawling.txt') as crawling:
            os.system('cls')
            sleep(1)
            print(crawling.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 6:
        with open('Castle of glass.txt') as castle_of_glass:
            os.system('cls')
            sleep(1)
            print(castle_of_glass.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 7:
        with open('Leave out all rest.txt') as Leave_out_all_rest:
            os.system('cls')
            sleep(1)
            print(Leave_out_all_rest.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 8:
        with open('Burn it down.txt') as Burn_it_down:
            os.system('cls')
            sleep(1)
            print(Burn_it_down.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 9:
        with open('Papercut.txt') as Papercut:
            os.system('cls')
            sleep(1)
            print(Papercut.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    elif eleccion == 10:
        with open('Breaking the habit.txt') as Breaking_the_habit:
            os.system('cls')
            sleep(1)
            print(Breaking_the_habit.read())
            print('\n')
            vovler =  input('Quieres volver al menú, (si/no): ').lower()
            if vovler == 'si':
                continue
            elif vovler == 'no':
                os.system('cls')
                print('¡Adios!')
                print('\n')
                break
            else:
                os.system('cls')
                print('Respuesta equivocada')
                sleep(1)
                continue
    else:
        pass
