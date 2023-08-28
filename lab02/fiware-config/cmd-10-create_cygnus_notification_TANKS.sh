curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - Envase01:TQ1",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:TQ1",
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
            "LEVEL",
            "LEVEL_HIGH",
            "LEVEL_HIGH_ALARM",
            "LEVEL_LOW",
            "LEVEL_LOW_ALARM",
            "VOLUME",
            "CAPACITY",
            "CAPACITY_UNIT",
            "TEMPERATURE",
            "TEMP_ALARM",
            "TEMP_LOW",
            "TEMP_HIGH"
        ]
    },
    "throttling": 5
}'

curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - Envase01:TQ2",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:TQ2",
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
            "LEVEL",
            "LEVEL_HIGH",
            "LEVEL_HIGH_ALARM",
            "LEVEL_LOW",
            "LEVEL_LOW_ALARM",
            "VOLUME",
            "CAPACITY",
            "CAPACITY_UNIT",
            "TEMPERATURE",
            "TEMP_ALARM",
            "TEMP_LOW",
            "TEMP_HIGH"
        ]
    },
    "throttling": 5
}'

curl --location 'http://localhost:1026/v2/subscriptions/' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "description": "Notify Cygnus - Envase01:TQ3",
    "subject": {
        "entities": [
            {
                "idPattern": "urn:ngsi-ld:SiteSP:Envase01:TQ3",
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
            "LEVEL",
            "LEVEL_HIGH",
            "LEVEL_HIGH_ALARM",
            "LEVEL_LOW",
            "LEVEL_LOW_ALARM",
            "VOLUME",
            "CAPACITY",
            "CAPACITY_UNIT",
            "TEMPERATURE",
            "TEMP_ALARM",
            "TEMP_LOW",
            "TEMP_HIGH"
        ]
    },
    "throttling": 5
}'