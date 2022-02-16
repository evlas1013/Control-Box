var startIndex = 0;
var endIndex = 0;
var output = "";
var keyCodes = 
{
0: "ZERO",
1: "ONE",
2: "TWO",
3: "THREE",
4: "FOUR",
5: "FIVE",
6: "SIX",
7: "SEVEN",
8: "EIGHT",
9: "NINE",
10: "ZERO",
11: "ONE",
12: "TWO",
13: "THREE",
14: "FOUR",
15: "FIVE",
16: "SIX",
17: "SEVEN",
18: "EIGHT",
19: "NINE"
}
function generate(){
	output = "";
	endIndex = parseInt(document.getElementById("numberOfButtons").value) - 1;
	output += "import board\n";
	output += "import usb_hid\n";
	output += "import digitalio\n";
	output += "import time\n";
	output += "from adafruit_hid.Keyboard import Keyboard\n";
	output += "from adafruit_hid.keycode import Keycode\n";
	output += 'print("running")\n';
	output += "k = Keyboard(usb_hid.devices)\n\n";
	output += "#INIT GPIO\n";
	for(var i = startIndex; i<=endIndex; i++)
	{
		output += "b" + i +" = digitalio.DigitalInOut(board.GP"+i+")\n";
		output += "b" + i +".switch_to_input(pull=digitalio.Pull.DOWN)\n\n";
	}
	output += "#LISTENERS\n"
	output += "buttonDelay = 50\n";
	output += "currentDelay = 0\n";
	output += "lastPressed = -1\n";
	output += "while True:\n";
	output += "    time.sleep(0.01)\n";
	output += "    currentDelay += 1\n";
	output += "    #print(lastPressed)\n";
	for(var i = startIndex; i<=endIndex; i++)
	{
		output += "    if b"+i+".value and (lastPressed != "+i+" or currentDelay > buttonDelay):\n";
		output += "        (k.send(Keycode.LEFT_CONTROL, ";
		if(i<10)
			output += "Keycode.LEFT_ALT, ";
		else
			output += "Keycode.LEFT_SHIFT, ";
		output += "Keycode."+keyCodes[i]+")\n";
		output += "        lastPressed = "+i+"\n";
		output += "        currentDelay = 0\n";
		output += "        continue\n\n";
	}
	document.getElementById("myOutput").value = output;
}