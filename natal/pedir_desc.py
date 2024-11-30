import csv
from django.db import models
from secreto.models import AmigoSecretoTeste2

import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

## Variáveis para a API Gmail
SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)


## Busca tabela de amigo secreto
dados_tabela = AmigoSecretoTeste2.objects.all()

for l in dados_tabela:
    service = build('gmail', 'v1', credentials=creds)
    message = MIMEMultipart('alternative')
    html = """\
    <html>
      <head></head>
      <body>
      <table height="740px" border="0" cellspacing="0" cellpadding="10"><tr>
      <td style="background-image: url('http://174.129.243.200/natal/natal/secreto/res/bk.png');
      background-repeat: no-repeat; background-size: cover; color: black; font-size: 15px;">
        <br><h2>Amigo Bem Secreto</h2><br>
        <p>Olá!""" + l.autor + """,<br><br>
           Este ano a proposta da brincadeira é em duas etapas. Esta é a primeira etapa.<br><br>
           Nesta primeira etapa você <b>NÃO ESTÁ</b> recebendo seu amigo secreto. <br><br>
           Foi sorteada uma pessoa para você descrever em não muitas palavras, mas <b>SEM ENTREGAR</b> fácil demais quem é. <br><br>
           Esta pessoa será o amigo secreto de alguém, mas não o seu.<br><br>
           Na segunda etapa, vocẽ (e todo mundo) vai receber somente a descrição do seu amigo secreto (escrita por um terceiro)<br>
           e vai ser toda a informação disponível para comprar o presente.<br><br>

           Para saber quem você vai descrever e fazer o seu texto, <b>clique neste <a href="http://174.129.243.200/">link</a></b>.<br>
           Se você quiser ou precisar alterar a descrição, basta voltar aqui e clicar novamente no link.<br><br><br>

           <b>Que o Natal traga bastante inspiração! (e presentes legais!)<b>
        </p>
        </td></tr></table>
      </body>
    </html>
    """
    part2 = MIMEText(html, 'html')
    message.attach(part2)

    #message = MIMEText('This is the body of the email')
    message['to'] = l.email
    message['subject'] = 'Amigo Bem Secreto - Fase 1 - Descrição'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
    message = None

