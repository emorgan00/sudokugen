var pencil = false;
var pencil_marks = document.getElementsByClassName("pencil_mark");
var full_marks = document.getElementsByClassName("full_mark");

var circle = document.createElement('div');
circle.innerHTML = "<img src='/static/circle.png' style='width: 100%; position: absolute; left: 0; top: 0; z-index: 0;'>"
circle = circle.firstChild;

window.oncontextmenu = function () {
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		if (m.matches(":hover")) {
			toggle_pencil();
			clean_marks();
			document.dispatchEvent(new Event("mousemove"));
			return false;
		}
	}
	return true;
}

function toggle_pencil() {
	window.pencil = !window.pencil;

	var pencil_button = document.getElementById("pencil_toggle");
	if (pencil) pencil_button.value = "Pencil Marks";
	else pencil_button.value = "Numbers";
}

function clear_highlights() {
	for (var i = full_marks.length - 1; i >= 0; i--) {
		var f = full_marks[i];
		if (f.lastChild.nodeName == "IMG") f.removeChild(f.lastChild);

	}
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		if (m.lastChild.nodeName == "IMG") m.removeChild(m.lastChild);
	}
}

function click_number(id, shift, editable) {
	var m = document.getElementById(id);
	var f = document.getElementById(id.substring(0, id.length-2));

	if (pencil && editable && f.className == "full_mark inactive") {
		if (shift) {
			if (m.lastChild.nodeName == "IMG") m.removeChild(m.lastChild);
			else m.appendChild(circle.cloneNode(true));
		} else {
			if (m.className == "pencil_mark inactive") {
				m.className = "pencil_mark active";
				m.style.color = "#666666";
			} else {
				m.className = "pencil_mark inactive";
				m.style.color = "#AAAAAA";
			}
		}
	} else if (!pencil) {
		if (shift) {
			if (f.lastChild.nodeName == "IMG") f.removeChild(f.lastChild);
			else f.appendChild(circle.cloneNode(true));
		} else if (editable) {
			if (f.className == "full_mark inactive") {
				f.className = "full_mark active";
				f.style.color = "#666666";
			} else {
				f.className = "full_mark inactive";
				f.style.color = "#AAAAAA";
			}
		}
	}
}

function clean_marks() {
	for (var i = full_marks.length - 1; i >= 0; i--) {
		var f = full_marks[i];
		if (f.className == "full_mark inactive")
			f.style.color = "rgba(0, 0, 0, 0)";
	}
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		f = document.getElementById(m.id.substring(0, m.id.length-2));
		if (f.className == "full_mark inactive") {
			if (m.className == "pencil_mark active") m.style.color = "#666666";
			else m.style.color = "rgba(0, 0, 0, 0)";
			if (m.lastChild.nodeName == "IMG") m.lastChild.style.display = "block";
		}
	}
}

document.addEventListener("mousemove", function update_marks() {
	var outside = !pencil;
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		var f_id = m.id.substring(0, m.id.length-2);
		var f = document.getElementById(f_id);
		if (m.className == "pencil_mark inactive" && f.className == "full_mark inactive" && pencil) {
			if (m.matches(":hover")) {
				m.style.color = "#AAAAAA";
			} else {
				m.style.color = "rgba(0, 0, 0, 0)";
			}
		} else if (!pencil) {
			if (m.matches(":hover")) {
				outside = false;
				if (f.className == "full_mark inactive") {
					f.firstChild.textContent = m.id.substring(m.id.length-1, m.id.length);
					f.style.color = "#AAAAAA";
				}
				for (var i = full_marks.length - 1; i >= 0; i--) {
					var f_other = full_marks[i];
					if (f_other != f && f_other.className == "full_mark inactive") {
						f_other.style.color = "rgba(0, 0, 0, 0)";
					}
				}
				for (var i = pencil_marks.length - 1; i >= 0; i--) {
					var m_other = pencil_marks[i];
					f_other_id = m_other.id.substring(0, m_other.id.length-2);
					if (f_other_id == f_id) {
						if (m_other.className == "pencil_mark active") m_other.style.color = "rgba(0, 0, 0, 0)";
						if (m_other.lastChild.nodeName == "IMG") m_other.lastChild.style.display = "none";
					} else {
						f_other = document.getElementById(f_other_id);
						if (f_other.className == "full_mark inactive") {
							if (m_other.className == "pencil_mark active") m_other.style.color = "#666666";
							if (m_other.lastChild.nodeName == "IMG") m_other.lastChild.style.display = "block";
						}
					}
				}
			}
		}
	}
	if (outside) clean_marks();
});