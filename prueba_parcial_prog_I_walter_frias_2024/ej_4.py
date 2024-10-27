#a. Permita al usuario ingresar un nuevo País para ser incorporado a la lista (‘Argentina’).Luego mostrar la lista completa y la cantidad de países incluidos. 
#b. Crear una función Buscar_pais() que reciba como parámetros la lista y un String, deberá retornar un valor entero con la posición que se encuentra en la lista.
#c. Listar todos los países de la lista que empiecen con la letra ‘M’.
 

paises = ["Afghanistan","Albania","Algeria",
"Andorra","Angola","Anguilla",
"Antigua and Barbuda","Armenia",
"Aruba","Australia","Austria",
"Azerbaijan","Bahamas","Bahrain",
"Bangladesh","Barbados","Belarus",
"Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia & Herzegovina",
"Botswana","Brazil","British Virgin Islands",
"Brunei","Bulgaria","Burkina Faso","Burundi",
"Cambodia","Cameroon","Cape Verde",
"Cayman Islands","Chad","Chile","China",
"Colombia","Congo","Cook Islands",
"Costa Rica","Cote D Ivoire","Croatia",
"Cruise Ship","Cuba","Cyprus","Czech Republic",
"Denmark","Djibouti","Dominica",
"Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea",

"Estonia","Ethiopia","Falkland Islands",
"Faroe Islands","Fiji","Finland","France",
"French Polynesia","French West Indies","Gabon",
"Gambia","Georgia","Germany","Ghana","Gibraltar",
"Greece","Greenland","Grenada","Guam","Guatemala",
"Guernsey","Guinea","Guinea Bissau","Guyana",
"Haiti","Honduras","Hong Kong","Hungary","Iceland",
"India","Indonesia","Iran","Iraq","Ireland",
"Isle of Man","Israel","Italy","Jamaica","Japan",
"Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
"Kyrgyz Republic","Laos","Latvia","Lebanon",
"Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania","Luxembourg","Macau","Macedonia",
"Madagascar","Malawi","Malaysia","Maldives",
"Mali","Malta","Mauritania","Mauritius","Mexico",
"Moldova","Monaco","Mongolia","Montenegro",
"Montserrat","Morocco","Mozambique","Namibia",
"Nepal","Netherlands","Netherlands Antilles",
"New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Norway","Oman","Pakistan","Palestine",
"Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Poland","Portugal","Puerto Rico",
"Qatar","Reunion","Romania","Russia","Rwanda",
"Saint Pierre & Miquelon","Samoa","San Marino",
"Satellite","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone","Singapore","Slovakia",
"Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","St Kitts & Nevis","St Lucia",
"St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
"Sweden","Switzerland","Syria","Taiwan","Tajikistan",
"Tanzania","Thailand","Timor L'Este","Togo","Tonga",
"Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine",
"United Arab Emirates","United Kingdom","Uruguay",
"Uzbekistan","Venezuela","Vietnam",
"Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

#print(len(paises))
#print(paises)

print("")
print("")

def ingresar_pais():
    nuevo_pais = input("a. Introduce el el pais Argentina  a la lista: ")
    paises.append(nuevo_pais)
    print(f"La cantidad de paises es: {len(paises)}")
    print("")
    print(f" Esta es la cantidad de paises: {paises}")
ingresar_pais()

print("")
def buscar_pais(paises, paises_a_buscar):
    if paises_a_buscar in paises:
        posicion = paises.index(paises_a_buscar)
        print(f"b .El pais {paises_a_buscar} se encuentra en la lista esta en la posicion {posicion}")
    else:
        print("El pais no se encuentra en la lista")
print("")
buscar_pais(paises=paises, paises_a_buscar="Argentina")

print("")
print("")

#. Listar todos los países de la lista que empiecen con la letra ‘M’. 
def listar_paises(paises):
    print("c . Esta es la lista de paises que empiezan con M :")
    for paises_M in paises:
        if paises_M.startswith("M"):
            print(f"{paises_M}")           
listar_paises(paises=paises)

print("")
print("")
