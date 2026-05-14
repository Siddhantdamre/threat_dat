# threat_dat

Threat-intelligence dashboard prototype with anomaly detection, Elasticsearch integration, Docker setup, and React-style dashboard components.

## What It Does

- Collects and models security-event style data.
- Trains anomaly-detection logic for suspicious patterns.
- Exposes backend routes for threat data.
- Includes dashboard components for visualizing threat signals.

## Tech

Python, JavaScript, Docker, Elasticsearch, anomaly detection, dashboard UI components.

## Repository Map

- `threat_detection.py`, `train_anomaly_model.py` - ML and detection logic.
- `elasticsearch_client.py` - search/storage integration.
- `routes.py`, `run.py` - backend entry points.
- `Dashboard.js`, `ThreatChart.js`, `App.js` - UI experiments.
- `docker-compose.yml` - local service orchestration.

## Status

Prototype. Best viewed as a cybersecurity + ML integration experiment.
