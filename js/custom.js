$(document).ready(function() {
	//Logout
	$("#logoutbutton").click(function() {
		deleteCookie();
		window.location.replace("index.html");
	});
});

function deleteCookie() {
	document.cookie = "email=" + null + ";" + "path=/;";
}

