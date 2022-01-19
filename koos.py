from datetime import date
import mysql.connector

#conexion con mi db
midb = mysql.connector.connect(
    host='localhost',
    user='sergiorobledo',
    password='28821243',
    database='koos'
)

cursor = midb.cursor()


#esquema de la base de datos (de la tabla)

esquemaDB = [
    'edad', 
    'nombre', 
    'profesional', 
    'respuesta1', 
    'respuesta2', 
    'respuesta3', 
    'respuesta4', 
    'respuesta5', 
    'resultadosintoma',
    'respuesta6',
    'respuesta7',
    'resultadoR',
    'respuesta8',
    'respuesta9',
    'respuesta10',
    'respuesta11',
    'respuesta12',
    'respuesta13',
    'respuesta14',
    'respuesta15',
    'respuesta16',
    'resultadoP',
    'respuesta17',
    'respuesta18',
    'respuesta19',
    'respuesta20',
    'respuesta21',
    'respuesta22',
    'respuesta23',
    'respuesta24',
    'respuesta25',
    'respuesta26',
    'respuesta27',
    'respuesta28',
    'respuesta29',
    'respuesta30',
    'respuesta31',
    'respuesta32',
    'respuesta33',
    'resultadoAVD',
    'respuesta34',
    'respuesta35',
    'respuesta36',
    'respuesta37',
    'respuesta38',
    'resultadoSP',
    'respuesta39',
    'respuesta40',
    'respuesta41',
    'respuesta42',
    'resultadoQoL'
]

#array to string para reemplazar en la consulta a sql "instert into Usuario(es la tabla)(edad, nombre..estructura de tabla"
# tomar el esquema de la base de datos y retornar un string que se pueda usar en el insert

def array_to_string(array):
    result = ''
    for field in array:
        result += field +','
    result = result[:-1]
    return result

camposDeDB = array_to_string(esquemaDB)

#diccionario respuesta

respuesta = {
    'Edad': 45,
    'Nombre': 'PEPe',
    'profesionalAcargo': 'El Sergei',
    'respuesta1': 1,
    'respuesta2': 2.0,
    'respuesta3': 3,
    'respuesta4': 4.0,
    'respuesta5': 5,
    'resultadoS': '',
    'respuesta6': '',
    'respuesta7': '',
    'resultadoR': '',
    'respuesta8': '',
    'respuesta9': '',
    'respuesta10': '',
    'respuesta11': '',
    'respuesta12': '',
    'respuesta13': '',
    'respuesta14': '',
    'respuesta15': '',
    'respuesta16': '',
    'resultadoP': '',
    'respuesta17': '',
    'respuesta18': '',
    'respuesta19': '',
    'respuesta20': '',
    'respuesta21': '',
    'respuesta22': '',
    'respuesta23': '',
    'respuesta24': '',
    'respuesta25': '',
    'respuesta26': '',
    'respuesta27': '',
    'respuesta28': '',
    'respuesta29': '',
    'respuesta30': '',
    'respuesta31': '',
    'respuesta32': '',
    'respuesta33': '',
    'resultadoAVD': '',
    'respuesta33': '',
    'respuesta34': '',
    'respuesta35': '',
    'respuesta36': '',
    'respuesta37': '',
    'respuesta38': '',
    'resultadoSP': '',
    'respuesta39': '',
    'respuesta40': '',
    'respuesta41': '',
    'respuesta42': '',
    'resultadoQoL': '',
}

#diccionario to string para reemplazar en el insert

def dictionary_to_string(dictionary):
    keys = list(dictionary.keys())
    result = ''
    # ['Edad','Nombre','profesionalAcargo','respuesta1','respuesta2','respuesta3','respuesta4','respuesta5','resultadoS']
    for key in keys:
        result += f"'{str(dictionary[key])}'" +','
    result = result[:-1]
    return result


print('ENCUESTA KOOS PARA LA EVALUACION DE RODILLA')

Fecha = date.today()
print(Fecha)

respuesta['Edad'] = input('Ingrese su edad: ')

respuesta['Nombre'] = input('Ingrese su nombre completo: ')

respuesta['profesionalAcargo'] = input('Ingrese su Profesional: ')

print('Instrucciones: Esta encuesta recoge su opinión sobre su rodilla intervenida o lesionada. La información que nos proporcione, servirá para saber como se encuentra y la capacidad para realizar diferentes actividades. Responda a cada pregunta marcando la casilla apropiada y solo una casilla por pregunta. Señale siempre la respuesta que mejor refleja su situación.')

print('Síntomas: \n Responda a estas preguntas considerando los síntomas que ha notado en la rodilla durante la última semana. (Ingrese el número) \n')

print('¿Se le hincha la rodilla? \n 1 Nunca \n 2 Rara vez \n 3 A veces \n 4 Frecuentemente \n 5 Siempre \n')
respuesta['respuesta1'] = float (input('Ingrese su respuesta: '))

print('¿Siente crujidos, chasquidos u otro tipo de ruidos cuando mueve la rodilla? \n 1) Nunca \n 2) Rara vez \n 3) A veces \n 4) Frecuentemente \n 5) Siempre \n')

respuesta['respuesta2'] = float (input('Ingrese su respuesta: '))

print('Al moverse, ¿siente que la rodilla falla o se bloquea? \n 1) Nunca \n 2) Rara vez \n 3) A veces \n 4) Frecuentemente \n 5) Siempre \n')
respuesta['respuesta3'] = float (input('Ingrese su respuesta: '))

print('¿Puede estirar completamente la rodilla? \n 1) Siempre \n 2) Frecuentemente \n 3) A veces \n 4) Rara vez \n 5) Nunca \n')
respuesta['respuesta4'] = float (input('Ingrese su respuesta: '))

print('¿Puede doblar completamente la rodilla? \n 1) Siempre \n 2) Frecuentemente \n 3) A veces \n 4) Rara vez \n 5) Nunca \n')
respuesta['respuesta5'] = float (input('Ingrese su respuesta: '))

##intente arreglar la cuenta resultadoS con un get, obteniendo los datos del diccionario, funciona bien menos
##el dato que se carga en la base sql, problema en el dato6

dato1 = respuesta.get('respuesta1')
dato2 = respuesta.get('respuesta2')
dato3 = respuesta.get('respuesta3')
dato4 = respuesta.get('respuesta4')
dato5 = respuesta.get('respuesta5')

respuesta['resultadoS'] = (100 - (((dato1 + dato2 + dato3 + dato4 + dato5) /5) * 100) / 4)
datoSint = respuesta.get('resultadoS')
print('Resultado para Síntomas es:', datoSint)  

print('Rigidez aricular: \n La rigidez o entumecimiento es una sensación de limitación o lentitud en el movimiento de la rodilla. Las siguientes preguntas indagan el grado de rigidez que ha experimentado, en la rodilla, durante la última semana. (Ingrese el número) \n')

print('¿Cuál es el grado de rigidez de su rodilla al levantarse por la mañana? \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta6'] = float (input('Ingrese su respuesta: '))

print('¿Cuál es el grado de rigidez de la rodilla después de estar sentado, recostado o descansando? \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta7'] = float (input('Ingrese su respuesta: '))

dato6 = respuesta.get('respuesta6')
dato7 = respuesta.get('respuesta7')

respuesta['resultadoR'] = (100 - (((dato6 + dato7) /2) * 100) / 4)
datoRig = respuesta.get('resultadoR')
print('Resultado para Rigidez es:', datoRig)  

##############################DOLOR

print('¿Con qué frecuencia ha tenido dolor en su rodilla? \n 1) Nunca \n 2) Mensual \n 3) Semanal\n 4) Diario\n 5) Continuo\n')
respuesta['respuesta8'] = float (input('Ingrese su respuesta: '))

print('¿Cuánto dolor ha tenido en la rodilla en la última semana al realizar las siguientes actividades? \n  . (Ingrese el número) \n')

print('Girar o pivotar sobre su rodilla \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta9'] = float (input('Ingrese su respuesta: '))

print('Estirar completamente la rodilla \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta10'] = float (input('Ingrese su respuesta: '))

print('Doblar completamente la rodilla \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta11'] = float (input('Ingrese su respuesta: '))

print('Al caminar, sobre una superficie plana \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta12'] = float (input('Ingrese su respuesta: '))

print('Al subir o bajar escaleras \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta13'] = float (input('Ingrese su respuesta: '))

print('Por la noche, en la cama \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta14'] = float (input('Ingrese su respuesta: '))

print('Al estar sentado o recostado \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta15'] = float (input('Ingrese su respuesta: '))

print('Al estar de pie \n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta16'] = float (input('Ingrese su respuesta: '))

dato8 = respuesta.get('respuesta8')
dato9 = respuesta.get('respuesta9')
dato10 = respuesta.get('respuesta10')
dato11 = respuesta.get('respuesta11')
dato12 = respuesta.get('respuesta12')
dato13 = respuesta.get('respuesta13')
dato14 = respuesta.get('respuesta14')
dato15 = respuesta.get('respuesta15')
dato16 = respuesta.get('respuesta16')


respuesta['resultadoP'] = (100 - (((dato8 + dato9 + dato10 + dato11 + dato12 + dato13 + dato14 + dato15 + dato16 ) /9) * 100) / 4)
datoP = respuesta.get('resultadoP')
print('Resultado para Dolor es:', datoP)


#########################AVD

print('Actividades cotidianas Las siguientes preguntas indagan sobre sus actividades físicas, es decir, su capacidad para moverse y valerse por sí mismo. Para cada una de las actividades mencionadas a continuación, indique el grado de dificultad experimentado en la última semana a causa de su rodilla. (ingrese el número)\n')

print('Al bajar escaleras\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta17'] = float (input('Ingrese su respuesta: '))

print('Al subir escaleras\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta18'] = float (input('Ingrese su respuesta: '))

print('Al levantarse de una silla o sillón\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta19'] = float (input('Ingrese su respuesta: '))

print('Al estar de pie\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta20'] = float (input('Ingrese su respuesta: '))

print('Al agacharse o recoger algo del suelo\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta21'] = float (input('Ingrese su respuesta: '))

print('Al caminar, sobre una superficie plana\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta22'] = float (input('Ingrese su respuesta: '))

print('Al subir o bajar del coche\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta23'] = float (input('Ingrese su respuesta: '))

print('Al ir de compras\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta24'] = float (input('Ingrese su respuesta: '))

print('Al ponerse los calcetines o las medias\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta25'] = float (input('Ingrese su respuesta: '))

print('Al levantarse de la cama\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta26'] = float (input('Ingrese su respuesta: '))

print('Al quitarse los calcetines o las medias\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta27'] = float (input('Ingrese su respuesta: '))

print('Estando acostado, al dar la vuelta en la cama o cuando mantiene la rodilla en una posición fija\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta28'] = float (input('Ingrese su respuesta: '))

print('Al entrar o salir de la bañera\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta29'] = float (input('Ingrese su respuesta: '))

print('Al estar sentado\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta30'] = float (input('Ingrese su respuesta: '))

print('Al sentarse o levantarse del inodoro\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta31'] = float (input('Ingrese su respuesta: '))

print('Realizando trabajos pesados de la casa (mover objetos pesados, lavar al suelo, etc.)\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta32'] = float (input('Ingrese su respuesta: '))

print('Realizando trabajos ligeros de la casa (cocinar, barrer, etc)\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta33'] = float (input('Ingrese su respuesta: '))

dato17 = respuesta.get('respuesta17')
dato18 = respuesta.get('respuesta18')
dato19 = respuesta.get('respuesta19')
dato20 = respuesta.get('respuesta20')
dato21 = respuesta.get('respuesta21')
dato22 = respuesta.get('respuesta22')
dato23 = respuesta.get('respuesta23')
dato24 = respuesta.get('respuesta24')
dato25 = respuesta.get('respuesta25')
dato26 = respuesta.get('respuesta26')
dato27 = respuesta.get('respuesta27')
dato28 = respuesta.get('respuesta28')
dato29 = respuesta.get('respuesta29')
dato30 = respuesta.get('respuesta30')
dato31 = respuesta.get('respuesta31')
dato32 = respuesta.get('respuesta32')
dato33 = respuesta.get('respuesta33')


respuesta['resultadoAVD'] = (100 - (((dato17 + dato18 + dato19 + dato20 + dato21 + dato22 + dato23 + dato24 + dato25 + dato26 + dato27 + dato28 + dato29 + dato30 + dato31 + dato32 + dato33 ) /17) * 100) / 4)
datoAVD = respuesta.get('resultadoAVD')
print('Resultado para las actividades de vida diaria es:', datoAVD)


############################DEPORTE


print('Función, actividades deportivas y recreacionales: Las siguientes preguntas indagan sobre su función al realizar actividades que requieran un mayor nivel de esfuerzo. Las preguntas deben responderse pensando en el grado de dificultad experimentado con su rodilla, en la última semana. (ingrese el número)\n')

print('Ponerse en cuclillas\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta34'] = float (input('Ingrese su respuesta: '))

print('Correr\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta35'] = float (input('Ingrese su respuesta: '))

print('Saltar\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta36'] = float (input('Ingrese su respuesta: '))

print('Girar o pivotar sobre la rodilla afectada\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta37'] = float (input('Ingrese su respuesta: '))

print('Arrodillarse\n 1) No tengo \n 2) Leve \n 3) Moderado\n 4) Intenso\n 5) Muy intenso\n')
respuesta['respuesta38'] = float (input('Ingrese su respuesta: '))

dato34 = respuesta.get('respuesta34')
dato35 = respuesta.get('respuesta35')
dato36 = respuesta.get('respuesta36')
dato37 = respuesta.get('respuesta37')
dato38 = respuesta.get('respuesta38')

respuesta['resultadoSP'] = (100 - (((dato34 + dato35 + dato36 + dato37 + dato38 ) /5) * 100) / 4)
datoSP = respuesta.get('respuesta37')
print('Resultado para Deporte es:', datoSP)



######################CALIDAD DE VIDA

print('Calidad de vida\n')

print('¿Con qué frecuencia es consciente del problema de su rodilla?\n 1) Nunca \n 2) Mensualmente \n 3) Semanalmente\n 4) A Diario\n 5) Siempre\n')
respuesta['respuesta39'] = float (input('Ingrese su respuesta: '))

print('¿Ha modificado su estilo de vida para evitar actividades que puedan lesionar su rodilla?\n 1) No \n 2) Levemente \n 3) Moderadamente \n 4) Drásticamente\n 5) Totalmente\n \n')
respuesta['respuesta40'] = float (input('Ingrese su respuesta: '))

print('¿En qué medida está preocupado por la falta de seguridad en su rodilla?\n 1) Nunca \n 2) Levemente \n 3) Moderadamente\n 4) Mucho\n 5) Excesivamente\n')
respuesta['respuesta41'] = float (input('Ingrese su respuesta: '))

print('En general, ¿cuántas dificultades le crea su rodilla?\n 1) Ninguna \n 2) Algunas \n 3) Pocas\n 4) Muchas\n 5) Todas\n')
respuesta['respuesta42'] = float (input('Ingrese su respuesta: '))

dato39 = respuesta.get('respuesta39')
dato40 = respuesta.get('respuesta40')
dato41 = respuesta.get('respuesta41')
dato42 = respuesta.get('respuesta42')


respuesta['resultadoQoL'] = (100 - (((dato39 + dato40 + dato41 + dato42 ) /4) * 100) / 4)
datoQoL = respuesta.get('resultadoQoL')
print('Resultado para Calidad de vida es:', datoQoL)

print('Muchas gracias por responder el cuestionario KOOS para la evaluación de rodilla')

#esta es la primer consulta que diseñe pero la limitante era escribir 50 veces todo, pero funciona.
#sql = "insert into Usuario(edad, nombre, profesional, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, resultadosintoma) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Edad, Nombre, profesionalAcargo, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, resultadoS)

#esta es la consulta bien hecha, que resiste la extrapolación y aumento de datos tanto de la db como de respuesta (de acá nació la idea de crear la array para la tabla y diccionario para las respuestas)

sql = (f"insert into Usuario({camposDeDB}) values ({dictionary_to_string(respuesta)})")
cursor.execute(sql)
midb.commit()





