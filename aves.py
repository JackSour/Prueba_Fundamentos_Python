import requests
from string import Template

html_template = Template('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="image/png" href="./img/images.png">
    <title>Aves Chile</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

$body

</body>
</html>                         
                         ''')

elem_template = Template('''<h2><u>Nombre Ave Español:</u> $nombre_espaniol</h2>
                            <h2><u>Nombre Ave Ingles:</u> $nombre_ingles</h2>
                            <img src="$url">
                         
                         ''')

def request_get(url):
    return requests.get(url).json()

def build_html(url):
    response = request_get(url)[20:30]
    texto =''
    
    for aves in response:
        nombre_esp = aves['name']['spanish']
        nombre_eng = aves['name']['english']
        imagen_url = aves['images']['main']
        texto += elem_template.substitute(nombre_espaniol=nombre_esp, nombre_ingles=nombre_eng, url=imagen_url)
    return html_template.substitute(body=texto)
    


html = build_html('https://aves.ninjas.cl/api/birds')
with open('aves_chile.html', 'w') as f:
    f.write(html)





