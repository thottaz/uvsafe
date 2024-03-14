from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['POST'])
def calculate():
    # 从前端获取数字
    number = request.form.get('number')
    print(number)

    if number == '3000':
        location = 'Melbourne City'
        UVLevel = 5
        cloth = "Sun glasses, wide-brimmed hat, lightweight cloth"
    elif number == '3008':
        location = 'Docklands'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    elif number == '3002':
        location = 'East Melbourne'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    elif number == '3142':
        location = 'Tookak'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    elif number == '3206':
        location = 'Albert Park'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    elif number == '3186':
        location = 'Brighton'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    elif number[0] == '3' and number[1] == '2':
        location = '---'
        UVLevel = 5
        cloth = "Hat and Full slieves"
    else:
        return "No such place, Please enter again"

    return f"Your location is %s, the UV level is %s, the recommend cloths are %s." %(location, UVLevel, cloth)



if __name__ == '__main__':
    app.run(debug=True)