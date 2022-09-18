<!DOCTYPE html>
<html>
    <head>
        <title>web控制開關</title>
        <link href="../style.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
	

		 <div class="flex">
			<h1>機器人遙控器</h1>	
			<button type="button" class="home" onclick="window.location.href='../index.php'">Homepage</button>
		</div>
		<a data-href="https://ithelp.ithome.com.tw/questions/10206698" data-limit="10">等待 10 秒</a>

		<script
		  src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
		  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs="
		  crossorigin="anonymous">
		</script>
		<script>
			function setDisabled() {
				document.getElementById('send').disabled = false;
			}
			function setstr(s) {
				document.getElementById("str").innerHTML=s;
				s -= 1;
				if(s>=0){
					setTimeout(setstr,1000,s);
				}else{
					document.getElementById("str").innerHTML='';}
			}
		</script>


		

			<!--<legend>掃地機器人控制</legend>-->
			<form method="post" action="Control.php">
			 
			<span id="str"></span>
			<div class="slider">
			  <input type="range" id="counttime" min="10" max="120" value="60" step="10" name='btn'  oninput="rangeValue.innerText = this.value">
			  <p id="rangeValue">60</p>
			  <div><button type="submit" id="send" class="green" style="width:100%" onclick="$(this).attr('disabled', true);window.setTimeout(setDisabled, (this.value)*1000);setstr(counttime.value);" >開啟</button></div>
			</div>
			 
			
			</form>

		
		
    </body>
</html>