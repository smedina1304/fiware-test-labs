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
                    "type": "Number"
                },
                {
                    "object_id": "mem",
                    "name": "memory",
                    "type": "Number"
                }
            ],
            "static_attributes": [
                {
                    "name": "relationship",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:Rack:SP:001"
                }
            ]
        }
    ]
}'
