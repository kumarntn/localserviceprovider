#!C:/Users/Naveen kumar/AppData/Local/programs/python/python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql

form=cgi.FieldStorage()
uname=form.getvalue("uname")
pwd=form.getvalue("pwd")
sub=form.getvalue("sub")

conn=pymysql.connect(host="localhost",user="root",password="",database="nexus")
cur=conn.cursor()

if sub!=None:
	q1="""select * from admin where username='%s' and password='%s'""" % (uname,pwd)
	cur.execute(q1)
	r=cur.fetchone()

	if r!=None:
		
		print("""<script>location.href="admmain.py";</script>""")
	
	else:
		print("""<script>alert("Invalid Username or password... ");location.href="admlogin.py";</script>""")
conn.close()

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
                    <li class="active">
                        <a href="index.html">Home</a>
                    </li>
					<li>
                        <a href="services.html">Services</a>
                    </li>
					<li>
                        <a href="workers.py">Workers</a>
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
            <div class="top-right">
                <div class="header-menu">
                    <div class="header-left">

                        <div class="dropdown">
                            <button class="btn btn-secondary dropdown-toggle" type="button" id="admin" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i>Admin</i>
                            </button>
                            <div class="dropdown-menu" aria-labelledby="admin">
                                <a class="dropdown-item media" href="admlogin.py">
                                    <p>Login</p>
                                </a>
                            </div>
                        </div>
						<div class="dropdown">
                            <button class="btn btn-secondary dropdown-toggle" type="button" id="klorker" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i>Workers</i>
                            </button>
                            <div class="dropdown-menu" aria-labelledby="klorker">
                                <a class="dropdown-item media" href="workersreg.py">
                                    <p>Register</p>
                                </a>
                                <a class="dropdown-item media" href="workerslog.py">
                                    <p>Login</p>
                                </a>
                            </div>
                        </div>
						<div class="dropdown">
                            <button class="btn btn-secondary dropdown-toggle" type="button" id="contract" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i>Contractors</i>
                            </button>
                            <div class="dropdown-menu" aria-labelledby="contract">
                                <a class="dropdown-item media" href="contractorsreg.py">
                                    <p>Register</p>
                                </a>
                                <a class="dropdown-item media" href="contractorslog.py">
                                    <p>Login</p>
                                </a>
                            </div>
                        </div>
						<div class="dropdown">
                            <button class="btn btn-secondary dropdown-toggle" type="button" id="users" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i>Users</i>
                            </button>
                            <div class="dropdown-menu" aria-labelledby="users">
                                <a class="dropdown-item media" href="usersreg.py">
                                    <p>Register</p>
                                </a>
                                <a class="dropdown-item media" href="userslog.py">
                                    <p>Login</p>
                                </a>
                            </div>
                        </div>
                </div>
            </div>
        </header>
        <!-- /#header -->
		 <div class="content" style="margin-top:60px;">
             <div class="animated fadeIn">
				<div class="row">
				<div class="col-lg-3"></div>
                <div class="col-lg-6">
                    <div class="card">
                        <div class="card-header">Admin Login</div>
                        <div class="card-body card-block">
                              <form action="admlogin.py" method="post" autocomplete="off">
                                <div class="form-group">
                                    <div class="input-group">
                                        <div class="input-group-addon"><i class="fa fa-user"></i></div>
                                        <input type="text" id="username" name="uname" placeholder="Username" class="form-control" required>
                                    </div>
                                </div>
                                
                                <div class="form-group">
                                    <div class="input-group">
                                        <div class="input-group-addon"><i class="fa fa-asterisk"></i></div>
                                        <input type="password" id="password" name="pwd" placeholder="Password" class="form-control" required>
                                    </div>
                                </div>
                               <div class="form-actions form-group" style="padding:10px;">
								
									<input type="reset" class="btn btn-danger btn-sm" value="Clear" style="float:right;">
									<input type="submit" class="btn btn-success btn-sm" value="Login" name="sub" style="float:right;margin-right:10px;">
									
                                 </div>
                            </form>
							</div>
                    </div>
                </div>

            </div>
        </div><!-- .animated -->
    </div><!-- .content -->

</body>
</html>
""")