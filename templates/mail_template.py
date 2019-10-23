template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Dónde Estás Mail</title>
    <style>
        {style}
    </style>

</head>
<body>
    <div class="container">
        {body}
    </div>
</body>
</html>
""".replace("\n", " ").replace("  ", " ")
