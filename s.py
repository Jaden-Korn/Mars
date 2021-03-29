from flask import Flask

app = Flask(__name__)


@app.route('/promotion_image')
def im():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                      <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                       <body>
                         <h1>Жди нас, Марс!</h1>
                         <img src="MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                         <div class="alert alert-primary" role="alert"> Человечество вырастает из детства. </div>
                         <div class="alert alert-primary" role="alert"> Человечеству мала одна планета. </div>
                         <div class="alert alert-primary" role="alert"> 'Мы сделаем обитаемыми безжизненные пока планеты.'</div>
                         <div class="alert alert-primary" role="alert"> 'И начнем с Марса!' </div>
                         <div class="alert alert-primary" role="alert"> 'Присоединяйся!' </div>
                      </body>
                    </html>'''


@app.route('/')
def i():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def prom():
    n = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(n)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
