TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`%` TRIGGER tri_notify_faults_or_alarms AFTER INSERT ON pointValues \nFOR EACH ROW CALL prc_alarms_notify(new.dataPointId, new.ts, new.pointValue)'
sql_modes=1436549152
definers='root@%'
client_cs_names='latin1'
connection_cl_names='latin1_swedish_ci'
db_cl_names='utf8_general_ci'
created=168683925377
