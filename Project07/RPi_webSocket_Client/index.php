<!--首頁-->
<html>
<head>
<meta  charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>WebSocket 108029041</title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<div class="flex">
<h2>WebSocket控制樹莓派開關燈</h2>	
</div>

<div class="flex">
<fieldset class="red">
<legend>紅燈控制</legend>
<button type="button" class="red" onclick="window.location.href='ron.php'">紅燈ON</button>
<button type="button" class="red" onclick="window.location.href='roff.php'">紅燈OFF</button>
</fieldset>

<fieldset class="yellow">
<legend>黃燈控制</legend>
<button type="button" class="yellow" onclick="window.location.href='yon.php'">黃燈ON</button>
<button type="button" class="yellow" onclick="window.location.href='yoff.php'">黃燈OFF</button>
</fieldset>

<fieldset class="green">
<legend>綠燈控制</legend>
<button type="button" class="green" onclick="window.location.href='gon.php'">綠燈ON</button>
<button type="button" class="green" onclick="window.location.href='goff.php'">綠燈OFF</button>
</fieldset>

<fieldset class="all">
<legend>所有燈控制</legend>
<button type="button" class="all" onclick="window.location.href='allon.php'">所有燈ON</button>
<button type="button" class="all" onclick="window.location.href='alloff.php'">所有燈OFF</button>
</fieldset>
</div>

</body>
</html>