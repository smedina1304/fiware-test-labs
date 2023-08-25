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
                    "object_id": "STATUS_ID",
                    "name": "STATUS_ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS_DESC",
                    "name": "STATUS_DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH",
                    "name": "LEVEL_HIGH",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH_ALARM",
                    "name": "LEVEL_HIGH_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL_LOW",
                    "name": "LEVEL_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_LOW_ALARM",
                    "name": "LEVEL_LOW_ALARM",
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
                    "object_id": "CAPACITY_UNIT",
                    "name": "CAPACITY_UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_ALARM",
                    "name": "TEMP_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP_LOW",
                    "name": "TEMP_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_HIGH",
                    "name": "TEMP_HIGH",
                    "type": "Number"
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
                    "object_id": "STATUS_ID",
                    "name": "STATUS_ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS_DESC",
                    "name": "STATUS_DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH",
                    "name": "LEVEL_HIGH",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH_ALARM",
                    "name": "LEVEL_HIGH_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL_LOW",
                    "name": "LEVEL_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_LOW_ALARM",
                    "name": "LEVEL_LOW_ALARM",
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
                    "object_id": "CAPACITY_UNIT",
                    "name": "CAPACITY_UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_ALARM",
                    "name": "TEMP_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP_LOW",
                    "name": "TEMP_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_HIGH",
                    "name": "TEMP_HIGH",
                    "type": "Number"
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
                    "object_id": "STATUS_ID",
                    "name": "STATUS_ID",
                    "type": "Text"
                },
                {
                    "object_id": "STATUS_DESC",
                    "name": "STATUS_DESC",
                    "type": "Text"
                },
                {
                    "object_id": "LEVEL",
                    "name": "LEVEL",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH",
                    "name": "LEVEL_HIGH",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_HIGH_ALARM",
                    "name": "LEVEL_HIGH_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "LEVEL_LOW",
                    "name": "LEVEL_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "LEVEL_LOW_ALARM",
                    "name": "LEVEL_LOW_ALARM",
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
                    "object_id": "CAPACITY_UNIT",
                    "name": "CAPACITY_UNIT",
                    "type": "Text"
                },
                {
                    "object_id": "TEMPERATURE",
                    "name": "TEMPERATURE",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_ALARM",
                    "name": "TEMP_ALARM",
                    "type": "Boolean"
                },
                {
                    "object_id": "TEMP_LOW",
                    "name": "TEMP_LOW",
                    "type": "Number"
                },
                {
                    "object_id": "TEMP_HIGH",
                    "name": "TEMP_HIGH",
                    "type": "Number"
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
