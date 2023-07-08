#!C:/Users/Naveen kumar/AppData/Local/programs/python/python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql

form=cgi.FieldStorage()
id=form.getvalue("id")
conn=pymysql.connect(host="localhost",user="root",password="",database="nexus")
cur=conn.cursor()

q1="""select * from workers where id=%s""" % (id)
cur.execute(q1)
r=cur.fetchone()
fn='files/'+r[9]
print("""
<!doctype html>
<html>
<head>
    <title>Nexus</title>
   
     <link rel="shortcut icon" href="images/n.png">

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/normalize.css@8.0.0/normalize.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lykmapipo/themify-icons@0.1.2/css/themify-icons.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pixeden-stroke-7-icon@1.2.3/pe-icon-7-stroke/dist/pe-icon-7-stroke.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.2.0/css/flag-icon.min.css">
    <link rel="stylesheet" href="assets/css/cs-skin-elastic.css">
    <link rel="stylesheet" href="assets/css/style.css">

    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800' rel='stylesheet' type='text/css'>

    <script src="https://cdn.jsdelivr.net/npm/jquery@2.2.4/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.4/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery-match-height@0.7.2/dist/jquery.matchHeight.min.js"></script>
    <script src="assets/js/main.js"></script>
<style>
a,i{
color:#000;}
</style>
</head>

<body>
    <aside id="left-panel" class="left-panel" style="margin-top:50px;">
        <nav class="navbar navbar-expand-sm navbar-default">
            <div id="main-menu" class="main-menu collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="workersmain.py?id=%s">Worker Dashboard</a>
                    </li>
					<li class="active">
                        <a href="wviewprofile.py?id=%s">View Profile</a>
                    </li>
					<li class="menu-item-has-children dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Worker Orders</a>
                        <ul class="sub-menu children dropdown-menu">
                            <li><a href="w_wo_new.py?id=%s">New</a></li>
                            <li><a href="w_wo_exis.py?id=%s">Existing</a></li>
                        </ul>
                    </li>
					<li>
                        <a href="workers_feedback.py?id=%s">Feedback</a>
                    </li>
					
					<li>
                        <a href="index.html">Logout</a>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>
    </aside>
<!-- Right Panel -->
    <div id="right-panel" class="right-panel">
        <!-- Header-->
        <header id="header" class="header" style="height:100px;padding:25px;"/>
            <div class="top-left">
                <div class="navbar-header" style="width:300px;">
                    <a class="navbar" href="./"><img src="images/nlogo.png" width="400" height="100" style="margin-top:-27px;"alt="Logo"></a>
                </div>
				<!-- <a ><i style="font-size:25pt;">Nexus</i></a> -->
            </div>
"""%(id,id,id,id,id))
print("""         
            <div class="top-right">
                <div class="header-menu">
                    <div class="header-left">

						<div class="user-area dropdown float-right">
							<a href="#" class="dropdown-toggle active" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							<img class="user-avatar rounded-circle" src="%s" alt="User Avatar">
							</a>

							<div class="user-menu dropdown-menu">
								<a class="nav-link" href="#"><i class="fa fa- user"></i>%s</a>
							</div>
						</div>
                    </div>
                </div>
            </div>
        </header>
        <!-- /#header -->"""%(fn,r[2]))
print("""		 <div class="content" style="margin-top:60px;">
             <div class="animated fadeIn">
				<div class="row">
						<div class="col-lg-3"></div>
							<div class="col-lg-4">
								<div class="card">
									<div class="card-header">
										<strong class="card-title mb-3">Profile</strong>
									</div>
									<div class="card-body">
										<div class="mx-auto d-block">
											<img class="rounded-circle mx-auto d-block" src="%s" width="90" height="80" alt="Card image cap">
											<h5 class="text-sm-center mt-2 mb-1">%s</h5>
											<div class="location text-sm-center"><i class="fa  fa-tablet"></i>%s</div>
											<div class="location text-sm-center"><i class="fa  fa-envelope"></i>%s</div>
											<div class="location text-sm-center"><i class="fa fa-map-marker"></i>%s</div>
										</div>
										<hr>
										<div class="card-text text-sm-center">
											<a href="wchangeprofile.py?id=%s">Change...</a>
											
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
        </div><!-- .animated -->
    </div><!-- .content -->

</body>
</html>
"""%(fn,r[2],r[3],r[4],r[5],id))