curl --location 'http://localhost:4041/iot/devices' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "devices": [
        {
            "device_id": "TQ1",
            "entity_name": "urn:ngsi-ld:SiteSP:Envase01:TQ1",
            "entity_type": "Equip",
            "attributes": [
                {
                    "object_id": "STATUS.ID",
                    "name": "STATUS.ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS.DESC",
                    "name": "STATUS.DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL.HIGH",
                    "name": "LEVEL.HIGH",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.HIGH.ALARM",
                    "name": "LEVEL.HIGH.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW",
                    "name": "LEVEL.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW.ALARM",
                    "name": "LEVEL.LOW.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "VOLUME",
                    "name": "VOLUME",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY",
                    "name": "CAPACITY",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY.UNIT",
                    "name": "CAPACITY.UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP.ALARM",
                    "name": "TEMP.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.LOW",
                    "name": "TEMP.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.HIGH",
                    "name": "TEMP.HIGH",
                    "type": "Boolean"
                }
            ],
            "static_attributes": [
                {
                    "name": "refStore",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:SiteSP:Envase01"
                }
            ]
        },
        {
            "device_id": "TQ2",
            "entity_name": "urn:ngsi-ld:SiteSP:Envase01:TQ2",
            "entity_type": "Equip",
            "attributes": [
                {
                    "object_id": "STATUS.ID",
                    "name": "STATUS.ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS.DESC",
                    "name": "STATUS.DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL.HIGH",
                    "name": "LEVEL.HIGH",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.HIGH.ALARM",
                    "name": "LEVEL.HIGH.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW",
                    "name": "LEVEL.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW.ALARM",
                    "name": "LEVEL.LOW.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "VOLUME",
                    "name": "VOLUME",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY",
                    "name": "CAPACITY",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY.UNIT",
                    "name": "CAPACITY.UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP.ALARM",
                    "name": "TEMP.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.LOW",
                    "name": "TEMP.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.HIGH",
                    "name": "TEMP.HIGH",
                    "type": "Boolean"
                }
            ],
            "static_attributes": [
                {
                    "name": "refStore",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:SiteSP:Envase01"
                }
            ]
        },
        {
            "device_id": "TQ3",
            "entity_name": "urn:ngsi-ld:SiteSP:Envase01:TQ3",
            "entity_type": "Equip",
            "attributes": [
                {
                    "object_id": "STATUS.ID",
                    "name": "STATUS.ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS.DESC",
                    "name": "STATUS.DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL.HIGH",
                    "name": "LEVEL.HIGH",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.HIGH.ALARM",
                    "name": "LEVEL.HIGH.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW",
                    "name": "LEVEL.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL.LOW.ALARM",
                    "name": "LEVEL.LOW.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "VOLUME",
                    "name": "VOLUME",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY",
                    "name": "CAPACITY",
                    "type": "Number"
                },
                {
                    "object_id": "CAPACITY.UNIT",
                    "name": "CAPACITY.UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP.ALARM",
                    "name": "TEMP.ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.LOW",
                    "name": "TEMP.LOW",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP.HIGH",
                    "name": "TEMP.HIGH",
                    "type": "Boolean"
                }
            ],
            "static_attributes": [
                {
                    "name": "refStore",
                    "type": "Relationship",
                    "value": "urn:ngsi-ld:SiteSP:Envase01"
                }
            ]
        }
    ]
}'
