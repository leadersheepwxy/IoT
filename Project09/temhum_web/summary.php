<?php 
	session_start();
	header("Content-Type: text/html; charset=utf-8");
	include("connMysql.php");
	$seldb = @mysqli_select_db($db_link, "temhum");
	if (!$seldb) die("資料庫選擇失敗！");
	$csql = "select (count( * )/60) as 'count' from th";
	$count_sql = mysqli_query($db_link, $csql);
?>
<html>
<head>
	<meta charset="utf-8">
	<meta content="width=device-width, initial-scale=1.0" name="viewport">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
	<title>溫溼度彙整數據</title>
	<link href="style.css" rel="stylesheet" type="text/css" />
</head>
	<body>
		<div style="text-align:center;"> 
			<div class="flex">
				<h1>溫溼度彙整數據  </h1>	
				<button type="button" class="home" onclick="window.location.href='index.php'">Homepage</button>
			</div>
			
			<div class='main'>
			<div class='warnning'>
				<b><font color='#daa520' size="3">當數值呈現黃色標示:溫度高於30度；濕度低於50%</font></b>
			</div>
				<table align="center">
				<!-- 表格表頭 -->
				<thead>
					<th>平均溫度</th>
					<th>平均濕度</th>
					<th>時間</th>

				</thead>
				<!-- 資料內容 -->
				<tbody>
				<?php
					$i=1;
					if ($i=1){
						while($count_result = mysqli_fetch_assoc($count_sql)){
							$count = intval($count_result["count"]); //幾個一分鐘
							//echo $count;
							for ( $k=0; $k<$count ; $k++ ) {
								$j = $k*60;
								
								//echo $j;
								$asql_t = "SELECT AVG(minute.tem) as 'avg_t' from (SELECT tem  From th Limit {$j}, 60) as minute;";
								$asql_h = "SELECT AVG(minute.hum) as 'avg_h' from (SELECT hum  From th Limit {$j}, 60) as minute;";
								$asql_time = "Select * From th Limit {$j}, 1;";
								//echo $asql_t;
								$avg_sql_t = mysqli_query($db_link, $asql_t);
								$avg_sql_h = mysqli_query($db_link, $asql_h);
								$avg_sql_time = mysqli_query($db_link, $asql_time);

								while($svg_result_t=mysqli_fetch_assoc($avg_sql_t) and $svg_result_h=mysqli_fetch_assoc($avg_sql_h) and $svg_result_time=mysqli_fetch_assoc($avg_sql_time)){
									echo "<tr>";
									if ($svg_result_t["avg_t"]>30){
										echo "<td><font color='#daa520'>".$svg_result_t["avg_t"]."</font></td>";
									}else{
										echo "<td>".$svg_result_t["avg_t"]."</td>";
									}
									if ($svg_result_h["avg_h"]<50){
										echo "<td><font color='#daa520'>".$svg_result_h["avg_h"]."</font></td>";
									}else{
										echo "<td>".$svg_result_h["avg_h"]."</td>";
									}
									echo "<td>".$svg_result_time["time"]."</td>";
									echo "</tr>";
								}
							}
						}
					}
					else{
							echo '<meta http-equiv=REFRESH CONTENT=2;url=index.php>';
						}
				?>
				</tbody>
				</table>
			</div>
		</div>	
	</body>
</html>