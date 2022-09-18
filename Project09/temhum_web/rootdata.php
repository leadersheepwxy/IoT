<?php 
	session_start();
	header("Content-Type: text/html; charset=utf-8");
	include("connMysql.php");
	$seldb = @mysqli_select_db($db_link, "temhum");
	if (!$seldb) die("資料庫選擇失敗！");
	$sql = "SELECT * FROM `th`";
	$selectsql = mysqli_query($db_link, $sql);
?>
<html>
<head>
	<meta charset="utf-8">
	<meta content="width=device-width, initial-scale=1.0" name="viewport">
	<title>溫溼度原始數據</title>
	<link href="style.css" rel="stylesheet" type="text/css" />
</head>
	<body>
		<div style="text-align:center;"> 
			<div class="flex">
				<h1>溫溼度原始數據  </h1>	
				<button type="button" class="home" onclick="window.location.href='index.php'">Homepage</button>
			</div>
			<div class='main'>
			<div class='warnning'>
				<b><font color='#daa520' size="3">當數值呈現黃色標示:溫度高於30度；濕度低於50%</font></b>
			</div>
				<table align="center">
				<!-- 表格表頭 -->
				<thead>
					<th>溫度</th>
					<th>濕度</th>
					<th>時間</th>
				</thead>
				<!-- 資料內容 -->
				<tbody>
				<?php
					$i=1;
					if ($i=1)
					{
						while($row_result=mysqli_fetch_assoc($selectsql)){
							echo "<tr>";
							if ($row_result["tem"]>30){
								echo "<td><font color='#daa520'>".$row_result["tem"]."</font></td>";
							}else{
								echo "<td>".$row_result["tem"]."</td>";
							}
							if ($row_result["hum"]<50){
								echo "<td><font color='#daa520'>".$row_result["hum"]."</font></td>";
							}else{
								echo "<td>".$row_result["hum"]."</td>";
							}
							echo "<td>".$row_result["time"]."</td>";
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