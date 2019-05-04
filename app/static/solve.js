function import_code(variant) {
	var form = document.getElementById("sudoku_form");
	var code_input = form.elements['code'];
	var code = code_input.value;
	code_input.value = '';

	code = code.replace(/\s/g,'').replace(/\n/g,'').replace(/\t/g,'');

	for (i = 0; i < code.length; i++) {
		var ch = code.charAt(i);
		var x = i%9;
		var y = Math.floor(i/9);
		if (ch != '' && '123456789'.indexOf(ch) !== -1) {
			form.elements[`tile_${y}${x}`].value = ch;
		} else {
			form.elements[`tile_${y}${x}`].value = '';
		}
	}
}

function switch_form(variant) {
	window.location.href = variant;
}