def notas():
    while True:
        print('1 Añadir alumno')
        print('2 Añadir asignatura')
        print('3 Borrar')
        print('4 Salir')
        opcion = int(input('Que quieres hacer: '))

        dic = {}
        if opcion == 1:
            n = input('Que nombre quieres añadir: ')
            dic[n] = {}

        if opcion == 2:
            n = input('Que nombre quieres añadir: ')
            if n not in dic:
                dic[n] = {}
            
            n2 = input('Que asignatura quieres añadir: ')
            l = []
            parar = True
            while parar:
                nota = input('Introduce una nota: ')
                if nota != 'x':
                    l.append(int(nota))
                else:
                    parar = False
            
            dic[n][n2] = l
        
        if opcion == 3:
            n = input('Que alumno quieres borrar: ')
            if n in dic:
                del dic[n]
            else:
                print('No existe')
    
        if opcion == 4:
            return dic

print(notas())