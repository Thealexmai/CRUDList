$(document).ready(function() {
	$(".loginBox").hide();
    $(".signBox").hide();
    $(".form-group").hide();
    $(".matchesTabs").hide();
	$("#loggedin").hide();
	$("#settings").hide();
	$("#loginerror").hide();
	$("#logout").hide();
	$(".intro-message").hide();
	$(".intro-header").hide();
	

	// $("#testCheck").click(function() {
	// 	alert($('input[name="buysell"]:checked').val());
	// });

	//Check to see if there is a cookie
	$.ajax({
		url: "/cgi-bin/validateCookie.py",
		type: "GET",
		dataType: "json",
		success: function(data) {
			console.log(data);
			if(data['hasCookie']==true && data['match']==true) {
				$("#loggedin").show();
				$("#logout").show();
				$(".matchesTabs").show();
				$(".intro-message").hide();
				$(".intro-header").hide();

                $(".navbarphoto").attr("src",data['picture']);
				//Calls ajax function to display the people of interest
				displayInterested();
				loadAll();

				$("#welcomename").append(data['firstname'] + " " + data['lastname'] + "<br>You are a : " + data['buyer']);
			}
			else {
				$(".form-group").show();
				$(".intro-message").show();
				$(".intro-header").show();

    			loadHome();
			}
		},
		error: function() {
			console.log("oops");
		},
	});

	

	// Log in button
	$("#loginsubmit").click(function() {
		var emailToLookup = $("#loginemail").val();
		var passwordToLookup = $("#loginpassword").val();
		// console.log(emailToLookup);
		$.ajax({
			url : "/cgi-bin/login.py",
			data : {
				loginemail : emailToLookup,
				loginpassword : passwordToLookup
			},
			type : "POST",
			dataType : "json",
			success : function(data) {
				console.log(data);
				//Hide the registration material
				$(".form-group").hide();
				$("#loginerror").hide();
				$(".matchesTabs").show();
				$(".navbarphoto").attr("src",data['picture']);

				// Create a cookie if successfully logged in - expires in 7 days
				setCookie(data.email, 7);
				$("#loggedin").show();
				$("#logout").show();

				$("#welcomename").append(data['firstname'] + " " + data['lastname'] + "<br>You are a : " + data['buyer']);

				//Calls function that displays people of interest
				displayInterested();
				$(".landingPageBod").hide();
				loadAll()
				
			},
			// Code to run if the request fails
			error : function() {
				$("#loginerror").fadeIn('slow');
			},
		});
	});

	//Logout
	$("#logoutbutton").click(function() {
		deleteCookie();
		window.location.replace("index.html");
	});
	// function stripHTML(html) {
	// 	return $($.parseHTML(html)).text();
	// }

	function loadHome(){
        $("#logButt").click(function() {
        	$(".intro-message").hide();
            $(".loginBox").show();
        });
        $("#signButt").click(function() {
            $(".intro-message").hide();
            $(".signBox").show();
        });
	}

	function displayInterested() {
		//Nested ajax calls the displayinterested
		$.ajax({
			url: "/cgi-bin/displayinterested.py",
			type: "POST",
			dataType: "json",
			success: function(data) {
				forPopulate(data, "#matches");
				// console.log(data[0]); //Returns ["Water", "Bottle", "waterbottle100@gmail.com"]
				// console.log(data[0][0]); //Returns "Water"
				// console.log("List is this long: " + data.length);
				// for(i=0; i<data.length; i++) {
				// 	// $("#matches").append(data[i][0] + " " + data[i][1] + "<br>");
				// 	$("#matches").append('<div class="col-md-4"><div class="col-xs-6"><img src="/attachments/profile.jpg" alt="profile img here" class="img-circle" style="height:150px;width:150px;"></div><div class="col-xs-6"><h3>'+data[i][0] + ' ' + data[i][1] +'</h3><h4>' + data[i][3]+ '</h4><form method="get" action="/cgi-bin/readprofiles.py"><button type="submit" class="btn btn-primary btn-xs" name="viewuser" id="' + i + '" value="' + data[i][2] + '">View Profile</button></form></div></div>');
				// 	//Assign click handlers for each of the button, (id needs to be unique [maybe just use the counter] and have it ajax)
				// }
			},
			error: function(){
				console.log("oops can't display");
			},
		});
	} //end of displayInterested

	function loadAll() {
		$.ajax({
			url: "cgi-bin/list.py",
			type: "GET",
			dataType: "json",
			data: {
				servicetoview: 0
			},
			success: function(data) {
				console.log(data);
				forPopulate(data, "#haircutpopulate");
			},
			error: function(data) {
				console.log("Can't display list of people " + data);
			}
		}); //End of display haircut

		$.ajax({
			url: "cgi-bin/list.py",
			type: "GET",
			dataType: "json",
			data: {
				servicetoview: 1
			},
			success: function(data) {
				console.log(data);
				forPopulate(data, "#taxipopulate");
			},
			error: function(data) {
				console.log("Can't display list of people " + data);
			}
		}); //End of display taxi

		$.ajax({
			url: "cgi-bin/list.py",
			type: "GET",
			dataType: "json",
			data: {
				servicetoview: 2
			},
			success: function(data) {
				console.log(data);
				forPopulate(data, "#foodpopulate");
			},
			error: function(data) {
				console.log("Can't display list of people " + data);
			}
		}); //End of display Food

		$.ajax({
			url: "cgi-bin/list.py",
			type: "GET",
			dataType: "json",
			data: {
				servicetoview: 3
			},
			success: function(data) {
				console.log(data);
				forPopulate(data, "#bikepopulate");
			},
			error: function(data) {
				console.log("Can't display list of people " + data);
			}
		}); //End of display Fix bike

		$.ajax({
			url: "cgi-bin/list.py",
			type: "GET",
			dataType: "json",
			data: {
				servicetoview: 4
			},
			success: function(data) {
				console.log(data);
				forPopulate(data, "#websitepopulate");
			},
			error: function(data) {
				console.log("Can't display list of people " + data);
			}
		}); //End of display website

	} //End of loadAll method

	function forPopulate(data, divID) {
		for(i=0; i<data.length; i++) {
			$(divID).append('<div class="col-md-4"><div class="col-xs-6"><img src="'+data[i][4]+'" alt="profile img here" class="img-circle" style="height:150px;width:150px;"></div><div class="col-xs-6"><h3>'+data[i][0] + ' ' + data[i][1] +'</h3><h4>' + data[i][3]+ '</h4><form method="get" action="/cgi-bin/readprofiles.py"><button type="submit" class="btn btn-primary btn-xs" name="viewuser" id="' + i + '" value="' + data[i][2] + '">View Profile</button></form></div></div>');
		}
	}

	// Function that sets the cookie
	function setCookie(value, expdays) {
		var d = new Date();
		d.setTime(d.getTime() + (expdays*24*60*60*1000));
		var expires = "expires="+d.toUTCString();
		document.cookie = "email=" + value + ";" + "path=/;" + expires + ";";
	}

	function deleteCookie() {
		document.cookie = "email=" + null + ";" + "path=/;";
	}

}); //End of document ready