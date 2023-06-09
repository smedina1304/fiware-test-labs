curl --location 'http://localhost:4041/iot/devices' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "devices": [
        {
            "device_id": "server001",
            "entity_name": "urn:ngsi-ld:Server:001",
            "entity_type": "Computer",
            "attributes": [
                {
                    "object_id": "cpu",
                    "name": "cpu",
                    "type": "Decimal"
                },
                {
                    "object_id": "mem",
                    "name": "memory",
                    "type": "Decimal"
                }
            ],
            "static_attributes": [
                {
                    "name": "relationship",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:Rack:SP:001"
                }
            ]
        },
        {
            "device_id": "station001",
            "entity_name": "urn:ngsi-ld:Station:001",
            "entity_type": "Weather",
            "attributes": [
                {
                    "object_id": "temp",
                    "name": "temp",
                    "type": "Decimal"
                },
                {
                    "object_id": "windspeed",
                    "name": "windspeed",
                    "type": "Decimal"
                },
                {
                    "object_id": "winddirection",
                    "name": "winddirection",
                    "type": "Decimal"
                },
                {
                    "object_id": "humidity",
                    "name": "humidity",
                    "type": "Decimal"
                },
                {
                    "object_id": "clouds",
                    "name": "clouds",
                    "type": "Decimal"
                },
                {
                    "object_id": "description",
                    "name": "description",
                    "type": "String"
                }
            ],
            "static_attributes": [
                {
                    "name": "relationship",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:Poyry:br:sp"
                }
            ]
        }
    ]
}'
