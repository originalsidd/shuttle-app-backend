from flask import Flask, request, jsonify
import joblib

clf = joblib.load('model.joblib')

app = Flask(__name__)

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     return 'hi'
    

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	input_data = request.args.get('y')

	prediction = clf.predict(input_data)

	return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
	app.run()
