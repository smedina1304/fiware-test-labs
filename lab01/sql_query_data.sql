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