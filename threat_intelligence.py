import requests

OTX_API_KEY = "your-api-key"
OTX_URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"

def fetch_threat_intelligence():
    headers = {"X-OTX-API-KEY": OTX_API_KEY}
    response = requests.get(OTX_URL, headers=headers)
    if response.status_code == 200:
        return response.json()["results"]
    return []

if __name__ == "__main__":
    threats = fetch_threat_intelligence()
    for threat in threats:
        print(f"Threat: {threat['name']}, Indicators: {len(threat['indicators'])}")
