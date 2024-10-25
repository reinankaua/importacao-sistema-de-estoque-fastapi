import csv
from .models import Cliente

def importar_clientes_csv(file, db):
    reader = csv.DictReader(file.file)
    for row in reader:
        cliente = Cliente(nome=row["nome"], endereco=row["endereco"], contato=row["contato"])
        db.add(cliente)
    db.commit()
