# main.pyfrom flask import Flask
from flask import Flask
from flask import request,render_template

import Test

app = Flask(__name__)


@app.route('/parseImg',methods=['GET', 'POST'])
def index():
     #   return jsonify({"error": 1001, "msg": "上传失败"}

    if request.method == "POST":
        # 接收图片

        img = request.files['file']

        return Test.parseImg(img.read())
    else:
        return "格式有误"


@app.route('/',methods=['GET', 'POST'])
def uploadTest():
     #   return jsonify({"error": 1001, "msg": "上传失败"}

     return render_template('upload.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()