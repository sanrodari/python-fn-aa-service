from flask import Flask, request, jsonify
app = Flask(__name__)
app.debug = True

@app.route('/python-fn', methods = ['POST'])
def hello():
    json = request.json
    result_array = im_the_fn(float(json['param']))
    return jsonify(result = result_array)

def im_the_fn(param):
    return [[param, param, param], [param * 2, param * 2, param * 2]]

if __name__ == '__main__':
    app.run()
