curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - COUNTER",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:COUNTER",
                "type": "Equip"
            }
        ]
    },
    "notification": {
        "http": {
            "url": "http://cygnus:5050/notify"
        },
        "attrs": [
            "BATCH_COUNT",
            "BATCH_LITERS"
        ]
    },
    "throttling": 5
}'

