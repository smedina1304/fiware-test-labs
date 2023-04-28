curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus of Station Weather changes",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:Station:*",
                "type": "Weather"
            }
        ],
        "condition": {
            "attrs": [
                "temp"
            ]
        }
    },
    "notification": {
        "http": {
            "url": "http://cygnus:5050/notify"
        },
        "attrs": [
            "temp",
            "feels_like",
            "pressure",
            "humidity",
            "description"
        ]
    },
    "throttling": 5
}'
