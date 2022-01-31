var startIndex = 8;
var endIndex = 19;
for(var i = startIndex; i<endIndex; i++)
{
	console.log("b" + i +" = digitalio.DigitalInOut(board.GP"+i+")");
	console.log("b" + i +".switch_to_input(pull=digitalio.Pull.DOWN)");

	console.log("if b"+i+".value and (lastPressed != "+i+" or currentDelay > buttonDelay):");
	console.log("k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.ZERO)");
	console.log("lastPressed = "+i);
	console.log("currentDelay = 0");
}