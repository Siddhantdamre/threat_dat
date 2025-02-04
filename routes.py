from flask import Blueprint, jsonify
from .threat_detection import detect_threats
from .elasticsearch_client import index_log, search_logs

@api_bp.route('/logs', methods=['POST'])
def ingest_log():
    log_data = {"message": "Failed login attempt", "timestamp": "2025-01-08"}
    index_log("logs", log_data)
    return jsonify({"message": "Log indexed successfully"})

@api_bp.route('/search', methods=['GET'])
def search_log():
    query = {"match": {"message": "Failed login"}}
    results = search_logs("logs", query)
    return jsonify(results)

api_bp = Blueprint('api', __name__)

@api_bp.route('/detect', methods=['GET'])
def detect():
    # This is a placeholder endpoint for threat detection
    threats = detect_threats()
    return jsonify({'threats': threats})

