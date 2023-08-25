curl --location 'http://localhost:4041/iot/devices' \
--header 'Content-Type: application/json' \
--header 'fiware-service: poyry' \
--header 'fiware-servicepath: /' \
-d @config_devices-Equip-PUMP.json
