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
            "id": "urn:ngsi-ld:Poyry:br:sp",
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
            "id": "urn:ngsi-ld:Poyry:br:bh",
            "type": "Site",
            "address": {
                "type": "PostalAddress",
                "value": {
                    "streetAddress": "Rua Maria Luiza Santiago, 200 - 6º andar - Bairro Santa Lúcia",
                    "addressRegion": "Minas Gerais",
                    "addressLocality": "Belo Horizonte",
                    "postalCode": "30360-740"
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
                        -19.974966679687764, 
                        -43.94785050238647
                    ]
                }
            },
            "name": {
                "type": "Text",
                "value": "Poyry MG"
            },
            "relationship": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Poyry:br"
            }
        },
        {
            "id": "urn:ngsi-ld:Rack:SP:001",
            "type": "Rack",
            "name": {
                "type": "Text",
                "value": "Rack 001 SP"
            },
            "relationship": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Poyry:br:sp"
            }
        },
        {
            "id": "urn:ngsi-ld:Rack:BH:002",
            "type": "Rack",
            "name": {
                "type": "Text",
                "value": "Rack 002 BH"
            },
            "relationship": {
                "type": "Relationship",
                "value": "urn:ngsi-ld:Poyry:br:bh"
            }
        }
    ]
}'
