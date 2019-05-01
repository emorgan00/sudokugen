var pencil = false;
var pencil_marks = document.getElementsByClassName("pencil_mark");
var full_marks = document.getElementsByClassName("full_mark");

function toggle_mode() {
	window.pencil = !window.pencil;
}

function click_number(id) {
	var m = document.getElementById(id);
	var f = document.getElementById(id.substring(0, id.length-2));

	if (pencil) {
		if (m.className == "pencil_mark inactive") {
			m.className = "pencil_mark active";
			m.style.color = "#666666";
		} else {
			m.className = "pencil_mark inactive";
			m.style.color = "#AAAAAA";
		}
	} else {
		if (f.className == "full_mark inactive") {
			f.className = "full_mark active";
			f.style.color = "#666666";
		} else {
			f.className = "full_mark inactive";
			f.style.color = "#AAAAAA";
		}
	}
}

document.addEventListener("mousemove", function update_marks() {
	var outside = !pencil;
	for (var i = pencil_marks.length - 1; i >= 0; i--) {
		var m = pencil_marks[i];
		if (m.className == "pencil_mark inactive" && pencil) {
			if (m.matches(":hover")) {
				m.style.color = "#AAAAAA";
			} else {
				m.style.color = "rgba(0, 0, 0, 0)";
			}
		} else if (!pencil) {
			var f = document.getElementById(m.id.substring(0, m.id.length-2));
			if (m.matches(":hover")) {
				outside = false;
				if (f.className == "full_mark inactive") {
					f.innerHTML = m.id.substring(m.id.length-1, m.id.length);
					f.style.color = "#AAAAAA";
				}
				for (var i = full_marks.length - 1; i >= 0; i--) {
					var other = full_marks[i];
					if (other != f && other.className == "full_mark inactive") other.style.color = "rgba(0, 0, 0, 0)";
				}
			}
		}
	}
	if (outside) {
		for (var i = full_marks.length - 1; i >= 0; i--) {
			var other = full_marks[i];
			if (other.className == "full_mark inactive") other.style.color = "rgba(0, 0, 0, 0)";
		}
	}
});