var mode;

function toggle_mode() {
	window.mode = !window.mode;
}

function click_number(id) {
	var elem = document.getElementById(id);
	if (elem.className == "pencil_mark") elem.className = "pencil_mark_active";
	else elem.className = "pencil_mark";
}