curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - PUMP1",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:PUMP1",
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
            "OPERATION"
        ]
    },
    "throttling": 5
}'

curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - PUMP2",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:PUMP2",
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
            "OPERATION"
        ]
    },
    "throttling": 5
}'

curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - PUMP3",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:PUMP3",
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
            "OPERATION"
        ]
    },
    "throttling": 5
}'