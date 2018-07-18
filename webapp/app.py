from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

clf = joblib.load("./clf.pkl")

@app.route("/profile", methods=['POST'])
def predict():

    if request.method == 'POST':

        data = request.get_json()
        if type(data) is not list:
            data = [data]

        bios = map(lambda profile: profile['bio'], data)

        predicted_probabilities = pd.DataFrame(
            clf.predict_proba(bios),
            columns=clf.classes_
        )

        predicted_probabilities['prediction'] = predicted_probabilities.idxmax(axis=1)

        def format_prediction_response(predicted_probability):
            return {
                'prediction': predicted_probability['prediction'],
                'confidence': predicted_probability[predicted_probability['prediction']]
            }

        formatted_prediction_responses = predicted_probabilities.apply(format_prediction_response, axis=1)

        return jsonify(formatted_prediction_responses.values.flatten().tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
