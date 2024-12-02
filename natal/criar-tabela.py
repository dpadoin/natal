import csv
from django.db import models
from models import AmigoSecretoTeste2

with open('./secreto/amigos.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = AmigoSecretoTeste2.objects.get_or_create(
                chave = row[0],
    descricao = row[1],
    nome = row[2],
    autor = row[3],
    amigo = row[4],
    email = row[5],
    enviou_desc = row[6],
    enviou_amigo = row[7],
                )