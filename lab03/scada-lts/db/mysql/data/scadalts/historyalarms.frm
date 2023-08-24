TYPE=VIEW
query=select `func_fromats_date`(`scadalts`.`plcalarms`.`activeTime`) AS `activeTime`,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) AS `inactiveTime`,`func_fromats_date`(`scadalts`.`plcalarms`.`acknowledgeTime`) AS `acknowledgeTime`,`scadalts`.`plcalarms`.`level` AS `level`,`scadalts`.`plcalarms`.`dataPointName` AS `name` from `scadalts`.`plcalarms` order by (`scadalts`.`plcalarms`.`inactiveTime` = 0) desc,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) desc,`scadalts`.`plcalarms`.`id` desc
md5=43d2450dbcf9c31d0ff5c79f0176047f
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=2023-06-15 14:27:33
create-version=1
source=SELECT func_fromats_date(activeTime) AS \'activeTime\',\nfunc_fromats_date(inactiveTime) AS \'inactiveTime\',\nfunc_fromats_date(acknowledgeTime) AS \'acknowledgeTime\',\nlevel,\ndataPointName AS \'name\' \nFROM plcAlarms ORDER BY inactiveTime = 0 DESC, inactiveTime DESC, id DESC
client_cs_name=latin1
connection_cl_name=latin1_swedish_ci
view_body_utf8=select `func_fromats_date`(`scadalts`.`plcalarms`.`activeTime`) AS `activeTime`,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) AS `inactiveTime`,`func_fromats_date`(`scadalts`.`plcalarms`.`acknowledgeTime`) AS `acknowledgeTime`,`scadalts`.`plcalarms`.`level` AS `level`,`scadalts`.`plcalarms`.`dataPointName` AS `name` from `scadalts`.`plcalarms` order by (`scadalts`.`plcalarms`.`inactiveTime` = 0) desc,`func_fromats_date`(`scadalts`.`plcalarms`.`inactiveTime`) desc,`scadalts`.`plcalarms`.`id` desc
