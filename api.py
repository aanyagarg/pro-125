from flask import Flask , jsonify, request

from prediction import get_prediction

app = Flask(__name__)

@app.route("/predict", methods=["POST"] )

def predict_1():
    image = request.files.get("digit")
    predicted_data = get_prediction(image)

    return jsonify({
        "prediction" : predicted_data
    }),200


if __name__ =="__main__":
    app.run(debug=True)




