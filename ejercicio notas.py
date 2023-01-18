ALUMNO = 0; ASIGNATURA = 1; PRACTICA = 2; NOTAS = 3

notas = [
    ['Brutus', 'Algebra', 'mal', [3.2, 5.1, 0.8]],
    ['Brutus', 'Discreta', 'regular', [5.2, 3.7, 5.0]],
    ['Brutus', 'Programacion', 'mal', [0.5, 3.2, 4.0]],
    ['Flavia', 'Algebra', 'bien', [7.2, 5.6, 7.1]],
    ['Flavia', 'Discreta', 'regular', [4.9, 8.5, 5.2]],
    ['Flavia', 'Programacion', 'bien', [9.5, 8.3, 10.0]],
    ['Jovina', 'Programacion', 'bien', [7.4, 9.3, 8.2]],
    ['Secundus', 'Algebra', 'mal', [3.1, 5.5, 6.1]],
    ['Secundus', 'Discreta', 'bien', [7.3, 6.7, 8.5]],
    ['Secundus', 'Programacion', 'mal', [4.5, 3.3, 4.2]],
    ['Sextus', 'Algebra', 'bien', [9.3, 9.8, 9.9]],
    ['Sextus', 'Programacion', 'bien', [8.9, 9.3, 8.9]]    
]

def nombres():
    l1=[]
    l2=[]
    for i in range(len(notas)):
        if notas[i][0] not in l1:
            l1.append(notas[i][0])

        if notas[i][1] not in l2:
            l2.append(notas[i][1])
    return l1, l2

print(nombres())

def numeros():
    l=set()
    for i in range(len(notas)):
        if notas[i][2] == 'bien':
            for j in range(len(notas[i][3])):
                if notas[i][3][j]>=9:
                    l.add(notas[i][0])
    return l

print(numeros())

def buscar():
    while True:
        print('1 por nombre')
        print('2 por asignatura')
        print('3 por calificación')
        print('4 por notas')
        print('5 Salir')
        opcion = int(input('Que opción quieres: '))
    
        if opcion == 1:
            n = input('Dime el nombre que quieres buscar: ')
            dic = {}
            d = {}
            d['Asignaturas'] = []
            d['Calificaciones'] = []
            d['Notas'] = []
            for i in range(len(notas)):
                if n in notas[i][0]:
                    d['Asignaturas'].append(notas[i][1])
                    d['Calificaciones'].append(notas[i][2])
                    d['Notas'].append(notas[i][3])
        
            dic[notas[i][0]] = d
            print(dic)
        
        elif opcion == 2:
            n = input('Dime que asignatura quieres buscar: ')
            dic={}
            d={}

            for l in notas:
                if l[ASIGNATURA]==n:
                    lista2=[]
                    lista2.append(l[NOTAS])
                    lista2.append(l[PRACTICA])
                    d[l[ALUMNO]]=lista2
            
            dic[n]=d
            print(dic)
        
        elif opcion == 3:
            n = input('Dime la calificación que quieres buscar: ')
            dic = {}
            l = []

            for i in notas:
                if i[PRACTICA]==n:
                    t = (i(ALUMNO), i(ASIGNATURA))
                    l.append(t)

            dic[i] = l
            print(dic)

        elif opcion == 4:
            n = int(input('Dime que nota quieres buscar: '))
            dic = {}
            l = []

            for i in notas:
                l2 = []
                for j in i[NOTAS]:
                    if j >= n:
                        l2.append(j)
                        t = (i[ALUMNO], i[ASIGNATURA], l2)
                        l.append(t)

            dic[n] = l
            print(dic)

        elif opcion == 5:
            break

print(buscar())