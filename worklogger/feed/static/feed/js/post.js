function render_data(posts_data, user_id) {

	var tbody = document.getElementById("project_feed_body");
	for (var index = 0; index < posts_data.project_feed.length; index+=1) {
		var tr = document.createElement('tr');
		var td1 = document.createElement('td');
		var td2 = document.createElement('td'); 
		var td3 = document.createElement('td'); 

		td1.innerHTML = posts_data.project_feed[index]['title'];
		td2.innerHTML = posts_data.project_feed[index]['details'];
		td3.innerHTML = posts_data.project_feed[index]['created at'];

		td1.style.width = "25%";
		td2.style.width = "60%";
		td3.style.width = "15%";

		tr.appendChild(td1);
		tr.appendChild(td2);
		tr.appendChild(td3);

		tbody.appendChild(tr);
	}

	var tbody = document.getElementById("hard_task_body");

	for (var post_id in posts_data['hard_task']) {
			var divs =  document.createElement('div');
			divs.className = 'card';
			divs.innerHTML = posts_data['hard_task'][post_id]['project_name'];

			// var tr = document.createElement('tr');
			// var td1 = document.createElement('td');
			// var td2 = document.createElement('td'); 

			// td1.innerHTML = posts_data['hard_task'][post_id]['project_name'];
			// td2.innerHTML = posts_data['hard_task'][post_id]['count'];

			// td1.style.width = "70%";

			// tr.appendChild(td1);
			// tr.appendChild(td2);

			// tbody.appendChild(tr);
			tbody.appendChild(divs);
	}

	var tbody = document.getElementById("user_tags_body");
	console.log(tbody);
	for (var post_id in posts_data['user_tags']) {
			var tr = document.createElement('tr');
			var td1 = document.createElement('td');
			var td2 = document.createElement('td'); 

			console.log(posts_data['user_tags'][post_id]['tag_name']);
			td1.innerHTML = posts_data['user_tags'][post_id]['tag_name'];
			td2.innerHTML = posts_data['user_tags'][post_id]['tag_count'];

			td1.style.width = "70%";

			tr.appendChild(td1);
			tr.appendChild(td2);

			tbody.appendChild(tr);
	}
}

function create_new_project(user_id) {
	window.location = '../create_post/create_project?user_id=' + user_id;
}