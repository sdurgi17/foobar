function render_data(posts_data, user_id) {

	var tbody = document.getElementById("post_feed_div");
	tbody.className = "container";
	var ul = document.createElement("ul");
	ul.className = "timeline";
	for (var index = 0; index < posts_data.project_feed.length; index+=1) {
		if (index%2 == 0) {
			var divs =  document.createElement('div');
			divs.className = 'card';

			var li1 = document.createElement("li");
			var div1 = document.createElement("div");
			div1.className = "timeline-panel";

			var div2 = document.createElement("div");
			div2.className = "timeline-heading";
			div2.innerHTML = "<h4 class='text-muted'>" + posts_data.project_feed[index]['title'] + "</h4>";

			div4 = document.createElement("div");
			div4.className = "timeline-title";
			div4.innerHTML = posts_data.project_feed[index]['created at'];

			var div3 = document.createElement("div");
			div3.className = "timeline-body";
			div3.innerHTML = posts_data.project_feed[index]['details'];


			div1.appendChild(div2);
			div1.appendChild(div4);

			div1.appendChild(div3);
			li1.appendChild(div1);

			ul.appendChild(li1);
		} else {
			var divs =  document.createElement('div');
			divs.className = 'card';

			var li1 = document.createElement("li");
			li1.className = "timeline-inverted";

			var div1 = document.createElement("div");
			div1.className = "timeline-panel";

			var div2 = document.createElement("div");
			div2.className = "timeline-heading";
			div2.innerHTML = "<h4 class='text-muted'>" + posts_data.project_feed[index]['title'] + "</h4>";

			div4 = document.createElement("div");
			div4.className = "timeline-title";
			div4.innerHTML = posts_data.project_feed[index]['created at'];

			var div3 = document.createElement("div");
			div3.className = "timeline-body";
			div3.innerHTML = posts_data.project_feed[index]['details'];


			div1.appendChild(div2);
			div1.appendChild(div4);

			div1.appendChild(div3);
			li1.appendChild(div1);

			ul.appendChild(li1);
		}
		// var div1 =  document.createElement('div');
		// var div2 =  document.createElement('div');
		// var div3 =  document.createElement('div');
		// div1.className = 'text';
		// div2.className = 'text';
		// div3.className = 'text';

		// div1.innerHTML = posts_data.project_feed[index]['title'];
		// div2.innerHTML = posts_data.project_feed[index]['details'];
		// div3.innerHTML = posts_data.project_feed[index]['created at'];

		// divs.appendChild(div1);
		// divs.appendChild(div2);
		// divs.appendChild(div3);





		// var tr = document.createElement('tr');
		// var td1 = document.createElement('td');
		// var td2 = document.createElement('td'); 
		// var td3 = document.createElement('td'); 

		// td1.innerHTML = posts_data.project_feed[index]['title'];
		// td2.innerHTML = posts_data.project_feed[index]['details'];
		// td3.innerHTML = posts_data.project_feed[index]['created at'];

		// td1.style.width = "25%";
		// td2.style.width = "60%";
		// td3.style.width = "15%";

		// tr.appendChild(td1);
		// tr.appendChild(td2);
		// tr.appendChild(td3);

		// tbody.appendChild(tr);

	}
	tbody.appendChild(ul);


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

function create_new_post(user_id, project_id) {
	window.location = '../create_post/create_post?user_id=' + 16 + '&project_id=' + 60;
}

function create_new_project(user_id) {
	window.location = '../create_post/create_project?user_id=' + 16;
}