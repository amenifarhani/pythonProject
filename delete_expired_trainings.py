from flask import Blueprint, jsonify

delete_expired_trainings_endpoint = Blueprint('delete_expired_trainings', __name__)

@delete_expired_trainings_endpoint.route('/deleteExpiredTrainings', methods=['POST'])
def delete_expired_trainings():
    # Ajoutez ici la logique pour supprimer les formations expirées et les sauvegarder vers Excel
    return jsonify({"message": "Deleted expired trainings and saved them to 'expired_trainings.xlsx'"}), 200
