<?php 
	session_start();
	header("Content-Type: text/html; charset=utf-8");
	include("connMysql.php");
	$seldb = @mysqli_select_db($db_link, "rbt");
	if (!$seldb) die("資料庫選擇失敗！");
	$sql = "SELECT * FROM `record`";
	$selectsql = mysqli_query($db_link, $sql);
?>
<html>
<head>
	<meta charset="utf-8">
	<meta content="width=device-width, initial-scale=1.0" name="viewport">
	<title>清掃紀錄</title>
	<link href="../style.css" rel="stylesheet" type="text/css" />
</head>
	<body>
		<div style="text-align:center;">
			<div class="flex">
				<h1>清掃紀錄</h1>	
				<button type="button" class="home" onclick="window.location.href='../index.php'">Homepage</button>
			</div>
			<div class='main'>
			<!--
			<div class='warnning'>
				<b><font color='#daa520' size="3">當數值呈現黃色標示:溫度高於30度；濕度低於50%</font></b>
			</div>
			-->
				<table align="center">
				<!-- 表格表頭 -->
				<thead>

					<th>開始時間</th>
					<th>結束時間</th>
				</thead>
				<!-- 資料內容 -->
				<tbody>
				<?php
					$i=1;
					if ($i=1)
					{
						while($row_result=mysqli_fetch_assoc($selectsql)){
							echo "<tr>";
							echo "<td>".$row_result["s_time"]."</td>";
							echo "<td>".$row_result["e_time"]."</td>";
							echo "</tr>";
						}
					}
					else
					{
						echo '<meta http-equiv=REFRESH CONTENT=2;url=index.php>';
					}
				?>
				</tbody>
				</table>
			</div>
		</div>	
	</body>
</html>