#!C:/Users/Naveen kumar/AppData/Local/programs/python/python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql,os,cgitb;cgitb.enable()

conn=pymysql.connect(host="localhost",user="root",password="",database="nexus")
cur=conn.cursor()

form=cgi.FieldStorage()
id=form.getvalue("id")
sub=form.getvalue("sub")

if sub!=None:
	pwd=form.getvalue("pwd")
	profile=form['profile']
	if profile.filename:
		fn1=os.path.basename(profile.filename)
		open("files/"+fn1,"wb").write(profile.file.read())
		q="""update workers set profile='%s',password='%s' where id=%s"""%(fn1,pwd,id)
		cur.execute(q)
		conn.commit()
	else:
		q="""update workers set password='%s' where id=%s"""%(pwd,id)
		cur.execute(q)
		conn.commit()
	print("""
		<script>
			alert("Profile Changed successfully!!");
			location.href="wviewprofile.py?id=%s";
		</script>
		"""%(id))

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
							 <div class="col-lg-6">
                    <div class="card">
                        <div class="card-header">Change profile</div>
                        <div class="card-body card-block">
                            <form action="wchangeprofile.py" method="post" enctype="multipart/form-data">
                                <input type="hidden" name="id" value="%s">
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="text-input" class=" form-control-label">Name</label></div>
                                        <div class="col-12 col-md-9"><input type="text" name="name" value="%s" class="form-control" readonly></div>
                                </div>
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="file-input" class=" form-control-label">Profile Pic</label></div>
                                        <div class="col-12 col-md-9"><input type="file" id="file-input" name="profile" class="form-control-file"></div>
                                </div>
								
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="text-input" class=" form-control-label">User Name</label></div>
										<div class="col-12 col-md-9"><input type="text" name="uname" class="form-control" value="%s" readonly></div>
                                </div>

								<div class="row form-group">
                                        <div class="col col-md-3"><label for="text-input" class=" form-control-label">Password</label></div>
                                        <div class="col-12 col-md-9"><input type="password" name="pwd" value="%s" class="form-control"></div>
                                </div>
								<div class="form-actions form-group" style="padding:10px;">
									
									<input type="reset" class="btn btn-danger btn-sm" value="Clear" style="float:right;">
									<input type="submit" class="btn btn-success btn-sm" value="Update" name="sub" style="float:right;margin-right:10px;">
									
                                 </div>
                            </form>
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
"""%(id,r[2],r[11],r[12]))