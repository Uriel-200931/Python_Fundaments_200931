d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)

print("")
alumno ={
    "matricula":200931,
    "nombre":"Juan",
    "apellidos":"Romero Lazcano",
    "cuatrimestre": 9,
    "promedio":9.6,
    "direccion":{
        "calle": "5 de mayo",
        "numero":55,
        "colonias":"El tabacal"
    }
    }
    
print(alumno)
print(alumno['nombre'])

for k in alumno: 
    print(k)

print("")

for k in alumno: 
    print(alumno[k])

print("")
print(alumno["direccion"]["calle"])

print("")
print(alumno.keys())
print(alumno.values())
print(alumno.items())