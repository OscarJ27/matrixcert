import pymongo

client = pymongo.MongoClient("mongodb+srv://CMatrixcert:dMLVmK7kzPAJqYaD@clustermatrixcert.pj8z0.mongodb.net/ClusterMatrixcertryWrites=true&w=majority")

db = client.Contacto

coll = db.Mensaje

coll.insert_many([
    {'nombre':'Jesus Peralta',
     'correo' :'JPeralta@gmail.com',
     'telefono':'985624415',
     'mensaje':'Hola buenas tardes, quisiera saber cuanto me saldria para poder hacer un molde de acero y les estoy adjuntando el diseño y medida'
    },
    {'nombre':'Ayrtton Florian',
     'correo' :'sirmaster@gmail.com',
     'telefono':'986754622',
     'mensaje':'Buenas noches, quisiera preguntar ¿Hasta cuantos diseños y moldes pueden realizar en un mes?'
    },
    {'nombre':'Pedro Fernandez',
     'correo' :'psg_pedro@gmail.com',
     'telefono':'965334882',
     'mensaje':'Tengo una consulta, de acuerdo con lo que e visto en la pagina web, ¿Cuanto se demorarian en el planeamiento del producto? y ¿Cuanto seria el costo por 50 unidades?'
    },
    {'nombre':'Rosa Hernandez',
     'correo' :'rosahernandez@hotmail.com',
     'telefono':'986855785',
     'mensaje':'¿Cual es el material mas comodo para hacer los moldes?'
    },
    {'nombre':'Helena Suarez',
     'correo' :'hs_87@hotmail.com',
     'telefono':'968655628',
     'mensaje':'Hola buenas noches, ¿Cuantas cavidades pueden entrar en el molde?'
    }

])

print(client.list_database_names())
