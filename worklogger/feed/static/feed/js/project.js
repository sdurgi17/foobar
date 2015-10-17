function render_data(projects_data) {

	var user_id = 1;// projects_data['user_id']
	console.log(user_id);
	var tbody = document.getElementById("project_display_div");
	for (var project_id in projects_data['user_feed']) {
		for (var project in projects_data['user_feed'][project_id]) {
			var divs =  document.createElement('div');
			divs.className = 'card';

			var div1 =  document.createElement('div');
			var div2 =  document.createElement('div');
			var div3 =  document.createElement('div');
			div1.className = 'text';
			div2.className = 'text';
			div3.className = 'text';

			div1.innerHTML = "<button type='button' class='btn btn-link'>" + 
						"<a href=../../feed/project_tasks?user_id=" + user_id + "&project_id=" + project_id + 
						"&project_name=" + projects_data['user_feed'][project_id]['name']
						+ ">" + 
						projects_data['user_feed'][project_id]['name'] + "</a>"
						"</button>";
			div2.innerHTML = projects_data['user_feed'][project_id]['details'];
			div3.innerHTML = projects_data['user_feed'][project_id]['updated_at'];

			divs.appendChild(div1);
			divs.appendChild(div2);
			divs.appendChild(div3);

			// var tr = document.createElement('tr');
			// var td1 = document.createElement('td');
			// var td2 = document.createElement('td'); 

			// td1.innerHTML = "<button type='button' class='btn btn-link'>" + 
			// 			"<a href=project_tasks?user_id=" + user_id + "&project_id=" + project_id + 
			// 			"&project_name=" + projects_data['user_feed'][project_id]['name']
			// 			+ ">" + 
			// 			projects_data['user_feed'][project_id]['name'] + "</a>"
			// 			"</button>";
			// td2.innerHTML = projects_data['user_feed'][project_id]['updated_at'];

			// td1.style.width = "70%";

			// tr.appendChild(td1);
			// tr.appendChild(td2);

			// tbody.appendChild(tr);
			tbody.appendChild(divs);
		}
	}

	var tbody = document.getElementById("projects_contribution_body");
	for (var project_id in projects_data['project_contribution']) {
		
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

	var tbody = document.getElementById("projects_tags_body");
	for (var project_id in projects_data['user_tags']) {
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

function create_new_project(user_id) {
	window.location = '../create_post/create_project?user_id=' + user_id;
}