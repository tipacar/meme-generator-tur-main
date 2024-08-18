# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')

        # Görev #3. Metnin konumunu almak
        textBottom_y=request.form.get('textBottom_y')
        textTop_y=request.form.get('textTop_y')
        # Görev #3. Metnin rengini almak
        color_selector=request.form.get('color-selector')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               textTop=textTop, 
                               textBottom=textBottom,
                               # Görev #3. Rengi görüntüleme
                               color_selector=color_selector,
                               
                               # Görev #3. Metnin konumunu görüntüleme
                               textTop_y=textTop_y,
                               textBottom_y=textBottom_y,

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
