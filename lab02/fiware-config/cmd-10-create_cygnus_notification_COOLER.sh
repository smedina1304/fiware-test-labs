curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus of Coolers changes",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:COOLER*",
                "type": "Equip"
            }
        ]
    },
    "notification": {
        "http": {
            "url": "http://cygnus:5050/notify"
        },
        "attrs": [
            "STATUS_ID",
            "STATUS_DESC",
            "TEMPERATURE"
        ]
    },
    "throttling": 5
}'