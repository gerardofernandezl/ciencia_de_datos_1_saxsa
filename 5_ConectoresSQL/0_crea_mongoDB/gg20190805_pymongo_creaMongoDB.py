import pymongo

mi_cliente_mongoDB = pymongo.MongoClient("mongodb://localhost:27017/")

#### 

mi_db = mi_cliente_mongoDB["mi_base_mongoDB"]


print(mi_cliente_mongoDB.list_database_names())


dblist = mi_cliente_mongoDB.list_database_names()
if "mi_base_mongoDB" in dblist:
  print("La base existe.")

### A collection in MongoDB is the same as a table in SQL databases.


mi_coleccion_clientes = mi_db["clientes"]


### A document in MongoDB is the same as a record in SQL databases.

mi_lista_clientes = [
  { "nombre": "Amy", "domicilio": "Apple st 652"},
  { "nombre": "Hannah", "domicilio": "Mountain 21"},
  { "nombre": "Michael", "domicilio": "Valley 345"},
  { "nombre": "Sandy", "domicilio": "Ocean blvd 2"},
  { "nombre": "Betty", "domicilio": "Green Grass 1"},
  { "nombre": "Richard", "domicilio": "Sky st 331"},
  { "nombre": "Susan", "domicilio": "One way 98"},
  { "nombre": "Vicky", "domicilio": "Yellow Garden 2"},
  { "nombre": "Ben", "domicilio": "Park Lane 38"},
  { "nombre": "William", "domicilio": "Central st 954"},
  { "nombre": "Chuck", "domicilio": "Main Road 989"},
  { "nombre": "Viola", "domicilio": "Sideway 1633"}
]

x = mi_coleccion_clientes.insert_many(mi_lista_clientes)

#print list of the _id values of the inserted documents:
print(x.inserted_ids) 




### In MongoDB we use the find and findOne methods to find data in a collection.

### Just like the SELECT statement is used to find data in a table in a MySQL database


for midata in mi_coleccion_clientes.find():
  print(midata) 



