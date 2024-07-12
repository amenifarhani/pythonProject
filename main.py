from datetime import datetime
from flask import Flask, jsonify

from cleanupservice import delete_expired_trainings_and_save_to_excel

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Training Management API!'

@app.route('/deleteExpiredTrainings', methods=['POST'])
def delete_expired_trainings_endpoint():
    try:




        delete_expired_trainings_and_save_to_excel('mysql+pymysql://root:@localhost:3306/Pidev')
        return jsonify({"message": "Deleted expired trainings and saved them to 'expired_trainings.xlsx'."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
