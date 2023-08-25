curl --location 'http://localhost:1026/v2/op/update' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
--data '{
    "actionType": "append",
    "entities": [
        {
            "id": "urn:ngsi-ld:Poyry:br",
            "type": "Company",
            "address": {
                "type": "PostalAddress",
                "value": {
                    "streetAddress": "Avenida Alfredo Egídio de Souza Aranha, 100 - Bloco B - 5o Andar",
                    "addressRegion": "São Paulo",
                    "addressLocality": "São Paulo",
                    "postalCode": "04726-170"
                },
                "metadata": {
                    "verified": {
                        "value": true,
                        "type": "Boolean"
                    }
                }
            },
            "location": {
                "type": "geo:json",
                "value": {
                    "type": "Point",
                    "coordinates": [
                        -23.632733513960115, 
                        -46.71232693112042
                    ]
                }
            },
            "name": {
                "type": "Text",
                "value": "Poyry"
            }
        },
        {
            "id": "urn:ngsi-ld:SiteSP:br",
            "type": "Site",
            "address": {
                "type": "PostalAddress",
                "value": {
                    "streetAddress": "Avenida Alfredo Egídio de Souza Aranha, 100 - Bloco B - 5o Andar",
                    "addressRegion": "São Paulo",
                    "addressLocality": "São Paulo",
                    "postalCode": "04726-170"
                },
                "metadata": {
                    "verified": {
                        "value": true,
                        "type": "Boolean"
                    }
                }
            },
            "location": {
                "type": "geo:json",
                "value": {
                    "type": "Point",
                    "coordinates": [
                        -23.632733513960115, 
                        -46.71232693112042
                    ]
                }
            },
            "name": {
                "type": "Text",
                "value": "Poyry SP"
            },
            "relationship": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Poyry:br"
            }
        },
        {
            "id": "urn:ngsi-ld:SiteSP:Envase01",
            "type": "Rack",
            "name": {
                "type": "Text",
                "value": "Area de Envase 01"
            },
            "relationship": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:SiteSP:br"
            }
        }
    ]
}'
