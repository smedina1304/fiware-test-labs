TYPE=VIEW
query=select `scadalts`.`plcalarms`.`id` AS `id`,`func_fromats_date`(`scadalts`.`plcalarms`.`activeTime`) AS `activation-time`,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) AS `inactivation-time`,`scadalts`.`plcalarms`.`dataPointType` AS `level`,`scadalts`.`plcalarms`.`dataPointName` AS `name`,`scadalts`.`plcalarms`.`dataPointId` AS `dataPointId` from `scadalts`.`plcalarms` where ((`scadalts`.`plcalarms`.`acknowledgeTime` = 0) and ((`scadalts`.`plcalarms`.`inactiveTime` = 0) or (`scadalts`.`plcalarms`.`inactiveTime` > (unix_timestamp((now() - interval 24 hour)) * 1000)))) order by (`scadalts`.`plcalarms`.`inactiveTime` = 0) desc,`scadalts`.`plcalarms`.`activeTime` desc,`scadalts`.`plcalarms`.`inactiveTime` desc,`scadalts`.`plcalarms`.`id` desc
md5=0bfdebbb29957ffec84e6e7c84ca75a2
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=2023-06-15 14:27:36
create-version=1
source=SELECT  id,  func_fromats_date(activeTime) AS \'activation-time\',  func_fromats_date(inactiveTime) AS \'inactivation-time\',  dataPointType AS \'level\',  dataPointName AS \'name\',  dataPointId AS dataPointId FROM plcAlarms WHERE acknowledgeTime = 0   AND (inactiveTime = 0 OR (inactiveTime > UNIX_TIMESTAMP(NOW() - INTERVAL 24 HOUR) * 1000)) ORDER BY inactiveTime = 0 DESC, activeTime DESC, inactiveTime DESC, id DESC
client_cs_name=latin1
connection_cl_name=latin1_swedish_ci
view_body_utf8=select `scadalts`.`plcalarms`.`id` AS `id`,`func_fromats_date`(`scadalts`.`plcalarms`.`activeTime`) AS `activation-time`,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) AS `inactivation-time`,`scadalts`.`plcalarms`.`dataPointType` AS `level`,`scadalts`.`plcalarms`.`dataPointName` AS `name`,`scadalts`.`plcalarms`.`dataPointId` AS `dataPointId` from `scadalts`.`plcalarms` where ((`scadalts`.`plcalarms`.`acknowledgeTime` = 0) and ((`scadalts`.`plcalarms`.`inactiveTime` = 0) or (`scadalts`.`plcalarms`.`inactiveTime` > (unix_timestamp((now() - interval 24 hour)) * 1000)))) order by (`scadalts`.`plcalarms`.`inactiveTime` = 0) desc,`scadalts`.`plcalarms`.`activeTime` desc,`scadalts`.`plcalarms`.`inactiveTime` desc,`scadalts`.`plcalarms`.`id` desc
