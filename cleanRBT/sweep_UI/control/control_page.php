<!DOCTYPE html>
<html>
    <head>
        <title>機器人遙控器</title>
        <link href="../style.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
	

     <div class="flex">
		<h1>機器人遙控器</h1>	
		<button type="button" class="home" onclick="window.location.href='../index.php'">Homepage</button>
	</div>

		

			<!--<legend>掃地機器人控制</legend>-->
			<form method="post" action="Control.php">
			 
			 
			 <div class="slider">
			  <input type="range" min="10" max="120" value="60" step="10" name='btn'  oninput="rangeValue.innerText = this.value">
			  <p id="rangeValue">60</p>
			  <div><button type="submit" class="green" style="width:100%">開啟</button></div>
			</div>
			 
			
			</form>

		
		
    </body>
</html>