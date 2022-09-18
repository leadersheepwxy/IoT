<?php 
	//資料庫主機設定
	$db_host = "192.168.0.129";
	$db_username = "web";
	$db_password = "108029041";
	//連線伺服器
	$db_link = @mysqli_connect($db_host, $db_username, $db_password);
	if (!$db_link) die("資料連結失敗！");
	//設定字元集與連線校對
	mysqli_set_charset($db_link, 'utf8');
?>