select recvTime, attrName, attrType, attrValue
from `urn_ngsi-ld_Server_001_Computer`;


SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "valor"
FROM `urn_ngsi-ld_Server_001_Computer`
ORDER BY "time"


SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "valor"
FROM `urn_ngsi-ld_Server_001_Computer`
WHERE attrName = "cpu"
ORDER BY "time" 

SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "valor"
FROM `urn_ngsi-ld_Server_001_Computer`
WHERE attrName = "memory"
ORDER BY "time" 


------

'temp'
SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "temp"
FROM `urn_ngsi-ld_Station_001_Weather`
WHERE attrName = "temp"
ORDER BY "time"

'humidity'
SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "humidity"
FROM `urn_ngsi-ld_Station_001_Weather`
WHERE attrName = "humidity"
ORDER BY "time"

'windspeed'
SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "windspeed"
FROM `urn_ngsi-ld_Station_001_Weather`
WHERE attrName = "windspeed"
ORDER BY "time"

'winddirection'
SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "winddirection"
FROM `urn_ngsi-ld_Station_001_Weather`
WHERE attrName = "winddirection"
ORDER BY "time"

'description'
SELECT
    UNIX_TIMESTAMP(recvTime) as "time",
    attrName as "name",
    CAST(attrValue as decimal) as "description"
FROM `urn_ngsi-ld_Station_001_Weather`
WHERE attrName = "description"
ORDER BY "time"