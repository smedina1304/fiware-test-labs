curl --location 'http://localhost:4041/iot/services' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--header 'Content-Type: application/json' \
--data '{
    "services": [
        {
            "apikey": "PoyryLab",
            "cbroker": "http://orion:1026",
            "entity_type": "Equip",
            "resource": ""
        }      
    ]
}'
