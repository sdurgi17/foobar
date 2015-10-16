function render_data(projects_data) {
	// var projects_data = '{{projects_data}}';
	// projects_data = JSON.parse(projects_data);
	// console.log(projects_data);


	// var projects_data = '{ "projects" : [' +
	// '{ "project_name":"John" , "last_updated":"Doe" },' +
	// '{ "project_name":"Anna" , "last_updated":"Smith" },' +
	// '{ "project_name":"John" , "last_updated":"Doe" },' +
	// '{ "project_name":"Anna" , "last_updated":"Smith" },' +
	// '{ "project_name":"John" , "last_updated":"Doe" },' +
	// '{ "project_name":"Anna" , "last_updated":"Smith" },' +	
	// '{ "project_name":"Peter" , "last_updated":"Jones" } ]}';

	// projects_data = JSON.parse(projects_data);
	// // console.log(projects_data);

	var tbody = document.getElementById("project_body");
	console.log();
	for (var project_id in projects_data['user_feed']) {
		for (var project in projects_data['user_feed'][project_id]) {
			var tr = document.createElement('tr');
			var td1 = document.createElement('td');
			var td2 = document.createElement('td'); 

			td1.innerHTML = "<button type='button' class='btn btn-link'>" + projects_data['user_feed'][project_id]['name'] + "</button>";
			td2.innerHTML = projects_data['user_feed'][project_id]['updated_at'];

			td1.style.width = "70%";

			tr.appendChild(td1);
			tr.appendChild(td2);

			tbody.appendChild(tr);
		}
	}

	var tbody = document.getElementById("projects_contribution_body");
	for (var project_id in projects_data['project_contribution']) {
		for (var project in projects_data['project_contribution'][project_id]) {
			var tr = document.createElement('tr');
			var td1 = document.createElement('td');
			var td2 = document.createElement('td'); 

			td1.innerHTML = projects_data['project_contribution'][project_id]['project_name'];
			td2.innerHTML = projects_data['project_contribution'][project_id]['count'];

			td1.style.width = "70%";

			tr.appendChild(td1);
			tr.appendChild(td2);

			tbody.appendChild(tr);
		}
	}

	var tbody = document.getElementById("projects_tags_body");
	for (var project_id in projects_data['user_tags']) {
		for (var project in projects_data['user_tags'][project_id]) {
			var tr = document.createElement('tr');
			var td1 = document.createElement('td');
			var td2 = document.createElement('td'); 

			td1.innerHTML = projects_data['user_tags'][project_id]['tag_name'];
			td2.innerHTML = projects_data['user_tags'][project_id]['tag_count'];

			td1.style.width = "70%";

			tr.appendChild(td1);
			tr.appendChild(td2);

			tbody.appendChild(tr);
		}
	}
}