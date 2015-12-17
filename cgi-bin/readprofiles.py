#!/usr/bin/env python
import cgitb, cgi, sqlite3
cgitb.enable()
form = cgi.FieldStorage()

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

#get the email from the form
user_email = form['viewuser'].value


print "Content-Type: text/html"
print

data = {}

#Transforming service numbers to words
def convertService(theint):
	if theint == 0:
		theint = "Haircut"
	elif theint == 1:
		theint = "Taxi"
	elif theint == 2:
		theint = "Food"
	elif theint == 3:
		theint = "Fix bicycle/car"
	elif theint == 4:
		theint = "Make website"
	return theint

the_buyer = c.execute('SELECT firstname, lastname, service, description, picture, location FROM users where email = ?;', (user_email,)).fetchone()
data['firstname'] = the_buyer[0]
data['lastname'] = the_buyer[1]
data['service'] = convertService(the_buyer[2])
data['description'] = the_buyer[3]
data['picture'] = the_buyer[4]
data['location'] = the_buyer[5]


print '''<!doctype html>
	<html>
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<!-- Defensive coding in case bootstrap server is down -->
			<script
				src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
			<script src="../js/jquery-1.11.3.min.js"></script>
			<link rel="stylesheet" href="../css/bootstrap.css">
			<link rel="stylesheet" href="../css/bootstrap.min.css">
			<link rel="stylesheet" href="../css/bootstrap-theme.css">
			<link rel="stylesheet" href="../css/bootstrap-theme.min.css">
			
			
			<script src="../js/bootstrap.js"></script>
			<script src="../js/bootstrap.min.js"></script>
			<!-- Get from online -->


			<link href="../css/landing-page.css" rel="stylesheet">
			<link href="../font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
			<link href="http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
			
			<script
				src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
			<link rel="stylesheet"
				href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
				
			<title>''' + data['firstname'] + ' ' + data['lastname'] +'''</title>

			<script type="text/javascript">
				$(document).ready(function() {
					$("#logout").hide();
					$.ajax({
						url: "/cgi-bin/validateCookie.py",
						type: "GET",
						dataType: "json",
						success: function(data) {
							console.log(data);
							if(data.hasCookie==true && data.match==true) {
								$("#logout").show();
								
								$(".navbarphoto").attr("src", "../"+data['picture']);
							}
						},
						error: function() {
							console.log("Error, something happened with cookie validation");
						},
					}); //End of ajax call

					$("#logoutbutton").click(function() {
						document.cookie = "email=" + null + ";" + "path=/;";
						window.location.replace("../index.html");
					});

					function deleteCookie() {
						document.cookie = "email=" + null + ";" + "path=/;";
					}
				}); //End of document ready
			</script>

				<!-- MAP STUFF -->
	<script src="http://maps.googleapis.com/maps/api/js"></script>
	<script>
	$.ajax({
		url: "/cgi-bin/validateCookie.py",
		type: "GET",
		dataType: "json",
		success: function () {
			var latitude = 0
			var longtitude = 0

			if ("'''+data['location'] + '''" == "Southside") {
				latitude = 43.117876
				longtitude = -77.631271
			}
			else if ("'''+data['location'] + '''" == "Fraternity Quad") {
				latitude = 43.129009
				longtitude = -77.632299
			}
			else if ("'''+data['location'] + '''" == "Residence Quad") {
				latitude = 43.130106
				longtitude = -77.631656
			}
			else if ("'''+data['location'] + '''" == "Sue B") {
				latitude = 43.129948
				longtitude = -77.626525
			}
			else if ("'''+data['location'] + '''" == "Towers") {
				latitude = 43.131756
				longtitude = -77.625508
			}
			else if ("'''+data['location'] + '''" == "Phase") {
				latitude = 43.130918
				longtitude = -77.622949
			}
			else if ("'''+data['location'] + '''" == "Riverview") {
				latitude = 43.133449
				longtitude = -77.630103
			}
			else {
				latitude = 43.131920
				longtitude = -77.633961
			}
			
			var mycenter = new google.maps.LatLng(latitude, longtitude)
			var mapProp = {
				center:mycenter,
				zoom:16,
				mapTypeId:google.maps.MapTypeId.ROADMAP
			};
			var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
			var marker=new google.maps.Marker({
				position: mycenter,
				animation:google.maps.Animation.BOUNCE
			});
			marker.setMap(map);
			google.maps.event.addDomListener(window, 'load')
		},
		error: function() {
			console.log("Error, something happened with cookie validation");
		},
	}); //End of ajax call
	</script>
		</head>

		<body>
			<div id="fb-root"></div>
			<script>
			$(document).ready(function() {
				(function(d, s, id) {
				  var js, fjs = d.getElementsByTagName(s)[0];
				  if (d.getElementById(id)) return;
				  js = d.createElement(s); js.id = id;
				  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5";
				  fjs.parentNode.insertBefore(js, fjs);
				}
				(document, 'script', 'facebook-jssdk'));
			});
			</script>
			<!-- Nav bar -->
			<nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">
			<div class="container topnav">
			
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand topnav" href="/index.html"><img src="/attachments/logo.jpg" style="max-height: 65px; max-width: 100px;"></a>
			</div>
			<!-- Collect the nav links, forms, and other content for toggling -->
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<div id="logout">
					<ul class="nav navbar-nav navbar-right">
						<li><a href="/myprofile.html"><img class="navbarphoto" style="height:20px;width:20px"> My Profile</a></li>
						<li><a id="settingsbutton" href="/settings.html"><span class="glyphicon glyphicon-lock"></span> Settings</a></li>
						<li><a id="logoutbutton" href="/index.html"><span class="glyphicon glyphicon-off"></span> Logout</a></li>
						
					</ul>
				 </div>
			</div>
			<!-- /.navbar-collapse -->
		</div>
		<!-- /.container -->
	</nav>
			
			<!-- Container for photo -->
			<div id="profile">

				<div class="container-fluid">
					<div class="row" style="padding-top:75px;text-align:center;">
						<!-- Empty div for name -->
						<h1 id="nameHeader">''' + data['firstname'] + ' ' + data['lastname'] + '''</h1>
					</div>

					<div class="row" style="padding:25px;text-align:center;">
						<div class="col-md-10" style="padding:25px;display:inline-block;float:none;text-align:left;border-style: inset;">
							<div class="col-md-6" style="text-align:center;">
								<img src="../'''+data['picture']+'''" class="img-circle" style="height: 300px; width: 100%; max-width: 300px;" alt="profile img">
							</div>
							<div class="col-md-6">
								<!-- Empty header for service listing -->
								<h3 id="service">Service: ''' + data['service'] + ''' </h3>
								<!-- Empty paragraph for description -->
								<h3 id="about">About: ''' + data['description'] + '''</h3>
								<!-- Empty paragraph for location -->
								<h3 id="locatioin">Located in: ''' + data['location'] + '''</h3>
							</div>
						</div>
					</div>

					<div class="row" style="padding:25px;text-align:center;">
						<a class="btn btn-success btn-lg" href="mailto:''' + user_email + '''?subject=CRUDLIST Interest in You">Email User</a>
						<a class="btn btn-danger btn-lg" href="../">Back to List</a>
					</div>

					<div id="googleMap" style="width:500px;height:380px; margin-left:auto; margin-right:auto"></div>
					<!-- Facebook comment -->
					<div class="fb-comments" data-href="localhost/www/cgi-bin/readprofiles.py?viewuser=''' + user_email + '''" data-width="100%" data-numposts="5"></div>
				</div> <!-- End of container fluid -->
			</div>



	<a  name="contact"></a>
	<div class="banner">
		<div class="container">
			<div class="row">
				<div class="col-lg-4" style="padding-top:75px;">
					<div class="bod1">
						
						<div class='hexagon'>
						  <ul class="menuMod">
							<li class='polygon_top'>
							  <a href="../index.html">Home</a>
							</li>
							<li class='polygon_top'></li>
							<li class='polygon_top'>
							  <a href="../myprofile.html">Profile</a>
							</li>
							<li class='polygon_bottom'>
							  <a href="../settings.html">Settings</a>
							</li>
							<li class='polygon_bottom'></li>
							<li class='polygon_bottom'>
							  <a href="../about.html">About</a>
							</li>
						  </ul>

							<p>
								<div class="menuText">
								<br><br>Menu
								</div>
							</p>

						</div>
					</div>

				</div>
				
				<div class="col-lg-6">
					<ul class="list-inline banner-social-buttons">
						<li>
							<a href="http://courses.pgbovine.net/csc210/project.htm" class="btn btn-default btn-lg"><i class="fa fa-external-link-square"></i> <span class="network-name">Project</span></a>
						</li>
						<li>
							<a href="https://github.com/zchen364/CRUDList" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>
						</li>
						<li>
							<a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>
						</li>
					</ul>
				</div>

			</div>



		</div>
		<!-- /.container -->

	</div>
	<!-- /.banner -->

	<!-- Footer -->
	<footer>
		<div class="container">
			<div class="row">
				<div class="col-lg-12">
				   
					<p class="copyright text-muted small">Copyright &copy; Alex Mai, Adam Livingston, Zhiming Chen. All Rights Reserved</p>
				</div>
			</div>
		</div>
	</footer>




</body>
	</html>'''