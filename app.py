import flask
from flask import Flask, render_template
import qrcode
import io


def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    #filename = f"qr\{data}.png"
    #img.save(filename)
    #return filename
    img_io = io.BytesIO()
    img.save(img_io)
    img_io.seek(0)
    return img_io


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('abdaubda.html', title='abdaubda')


@app.route("/trampacumpa")
def trampacumpa():
    return render_template('trampacumpa.html', title='trampacumpa')


@app.route("/qr/<string:key>")
def qr(key):
    qr_img = generate_qr(key)
    return flask.send_file(qr_img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

