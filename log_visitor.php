<?php
$ip = $_SERVER['REMOTE_ADDR'];
$file = 'visitor_log.txt';
$date = date('Y-m-d H:i:s');
$log_entry = "$date - $ip\n";

// Append IP address to the log file
file_put_contents($file, $log_entry, FILE_APPEND | LOCK_EX);
?>
