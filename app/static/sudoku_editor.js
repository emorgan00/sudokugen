var pencil = false;
var pencil_marks = document.getElementsByClassName("pencil_mark");
var full_marks = document.getElementsByClassName("full_mark");
var numbers = true;

var img_o = document.createElement('div');
img_o.innerHTML = "<img src='/static/circle.png' class='solid' style='width: 100%; position: absolute; left: 0; top: 0; z-index: 0;'>"
img_o = img_o.firstChild;
img_o_preview = img_o.cloneNode(true);
img_o_preview.style.opacity = "0.5";
img_o_preview.style.filter  = 'alpha(opacity=50)';
img_o_preview.className  = 'preview';

var img_x = document.createElement('div');
img_x.innerHTML = "<img src='/static/x.png' class='solid' style='width: 100%; position: absolute; left: 0; top: 0; z-index: 0;'>"
img_x = img_x.firstChild;
img_x_preview = img_x.cloneNode(true);
img_x_preview.style.opacity = "0.5";
img_x_preview.style.filter  = 'alpha(opacity=50)';
img_x_preview.className  = 'preview';

var active_img = img_o;
var active_preview = img_o_preview;

document.addEventListener("keyup", function check_key(e) {
	if (e.keyCode == 16) { // shift
		if (numbers) {
			numbers = false;
			active_img = img_o;
			active_preview = img_o_preview;
		} else if (active_img == img_o) {
			active_img = img_x;
			active_preview = img_x_preview;
		} else {
			numbers = true;
		}
		clean_marks();
		document.dispatchEvent(new Event("mousemove"));
	}
});

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
		if (!numbers) {
			if (m.lastChild.nodeName == "IMG" && m.lastChild.className == "solid") {
				m.removeChild(m.lastChild);
				m.appendChild(active_preview.cloneNode(true));
			} else if (m.lastChild.nodeName == "IMG") {
				m.removeChild(m.lastChild);
				m.appendChild(active_img.cloneNode(true));
			} else
				m.appendChild(active_img.cloneNode(true));
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
		if (!numbers) {
			if (f.lastChild.nodeName == "IMG" && f.lastChild.className == "solid") {
				f.removeChild(f.lastChild);
				f.appendChild(active_preview.cloneNode(true));
			} else if (f.lastChild.nodeName == "IMG") {
				f.removeChild(f.lastChild);
				f.appendChild(active_img.cloneNode(true));
			} else
				f.appendChild(active_img.cloneNode(true));
		} else if (editable && numbers) {
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
		if (f.lastChild.nodeName == "IMG" && f.lastChild.className == "preview")
			f.removeChild(f.lastChild);
	}
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		f = document.getElementById(m.id.substring(0, m.id.length-2));
		if (f.className == "full_mark inactive") {
			if (m.className == "pencil_mark active") m.style.color = "#666666";
			else m.style.color = "rgba(0, 0, 0, 0)";
			if (m.lastChild.nodeName == "IMG") {
				if (m.lastChild.className == "preview")
					m.removeChild(m.lastChild);
				else
					m.lastChild.style.display = "block";
			}
		}
	}
}

document.addEventListener("mousemove", function update_marks() {
	var outside = !pencil;
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		var f_id = m.id.substring(0, m.id.length-2);
		var f = document.getElementById(f_id);
		if (f.className == "full_mark inactive" && pencil) {
			if (m.matches(":hover")) {
				if (m.className == "pencil_mark inactive" && numbers)
					m.style.color = "#AAAAAA";
				if (m.lastChild.nodeName != "IMG" && !numbers)
					m.appendChild(active_preview.cloneNode(true));
			} else {
				if (m.className == "pencil_mark inactive" && numbers)
					m.style.color = "rgba(0, 0, 0, 0)";
				if (m.lastChild.nodeName == "IMG" && m.lastChild.className == "preview" && !numbers)
					m.removeChild(m.lastChild);
			}
		} else if (!pencil) {
			if (m.matches(":hover")) {
				outside = false;
				if (f.className == "full_mark inactive") {
					f.firstChild.textContent = m.id.substring(m.id.length-1, m.id.length);
					if (numbers) f.style.color = "#AAAAAA";
				}
				if (f.lastChild.nodeName != "IMG" && !numbers) f.appendChild(active_preview.cloneNode(true));
				for (var i = full_marks.length - 1; i >= 0; i--) {
					var f_other = full_marks[i];
					if (f_other != f) {
						if (f_other.className == "full_mark inactive")
							f_other.style.color = "rgba(0, 0, 0, 0)";
						if (f_other.lastChild.nodeName == "IMG" && f_other.lastChild.className == "preview")
							f_other.removeChild(f_other.lastChild);
					}
				}
				for (var i = pencil_marks.length - 1; i >= 0; i--) {
					var m_other = pencil_marks[i];
					f_other_id = m_other.id.substring(0, m_other.id.length-2);
					if (f_other_id == f_id) {
						if (m_other.className == "pencil_mark active" && numbers) m_other.style.color = "rgba(0, 0, 0, 0)";
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