curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus of cpu and memory changes",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:Server:*",
                "type": "Computer"
            }
        ],
        "condition": {
            "attrs": [
                "cpu"
            ]
        }
    },
    "notification": {
        "http": {
            "url": "http://cygnus:5050/notify"
        },
        "attrs": [
            "cpu",
            "memory"
        ]
    },
    "throttling": 5
}'
