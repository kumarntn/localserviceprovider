#!C:/Users/Naveen kumar/AppData/Local/programs/python/python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql,os,cgitb;cgitb.enable()

conn=pymysql.connect(host="localhost",user="root",password="",database="nexus")
cur=conn.cursor()
q1="""select max(id) from services"""
cur.execute(q1)
r=cur.fetchone()
if r[0]!=None:
    n=r[0]
else:
    n=0
z=""
if n<10:
    z="000"
elif n<100:
    z="00"
elif n<1000:
    z="0"
else:
    z=""
sid="srvc"+z+str(n+1)

form=cgi.FieldStorage()
id=form.getvalue("id")
sub=form.getvalue("sub")

q1="""select * from users where id=%s""" % (id)
cur.execute(q1)
r=cur.fetchone()
fn='files/'+r[6]

if sub!=None:
	tos=form.getvalue("tos")
	sdate=form.getvalue("date")
	city=form.getvalue("city")
	q="""insert into services(srvc_id,service,sdate,venue,status,usr_id,usr_name) values('%s','%s','%s','%s','%s','%s','%s')"""%(sid,tos,sdate,city,'New',r[1],r[2])
	cur.execute(q)
	conn.commit()
	q="""insert into feedbacks(srvc_id,service,usr_id,usr_name) values('%s','%s','%s','%s')"""%(sid,tos,r[1],r[2])
	cur.execute(q)
	conn.commit()
	print("""
	<script>
		alert("Request sent successfully!!");
		location.href="u_req_new.py?id=%s";
	</script>
	"""%(id))
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
""")
print("""<body>
    <aside id="left-panel" class="left-panel" style="margin-top:50px;">
        <nav class="navbar navbar-expand-sm navbar-default">
            <div id="main-menu" class="main-menu collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="usersmain.py?id=%s">User Dashboard</a>
                    </li>
					<li>
                        <a href="uviewprofile.py?id=%s">View Profile</a>
                    </li>
					<li class="menu-item-has-children dropdown active">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Work Request</a>
                        <ul class="sub-menu children dropdown-menu">
                            <li><a href="u_req_new.py?id=%s">New</a></li>
                            <li><a href="u_req_exis.py?id=%s">Existing</a></li>
                        </ul>
                    </li>
					<li>
                        <a href="userpayment.py?id=%s">Payment</a>
                    </li>
					<li>
                        <a href="userfeedback.py?id=%s">Feedback</a>
                    </li>
					
					<li>
                        <a href="index.html">Logout</a>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>
    </aside>
"""%(id,id,id,id,id,id))    
print("""    <!-- Right Panel -->
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

						<div class="user-area dropdown float-right">""")
print(""" 			<a href="#" class="dropdown-toggle active" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
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
print("""<div class="content" style="margin-top:60px;">
				<div class="animated fadeIn">
					<div class="row">
						<div class="col-lg-3"></div>
							 <div class="col-lg-6">
                    <div class="card">
                        <div class="card-header">Request</div>
                        <div class="card-body card-block">
                            <form action="u_req_new.py" method="post" enctype="multipart/form-data">
                                <input type="hidden" name="id" value="%s">
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="select" class=" form-control-label">Select Service</label></div>
                                        <div class="col-12 col-md-9">
                                            <select name="tos" class="form-control">
                                                <option value="">Select Service</option>
                                                <option value="Painter">Painter</option>
                                                <option value="Carpenter">Carpenter</option>
                                                <option value="Plumber">Plumber</option>
                                                <option value="Electrician">Electrician</option>
                                                <option value="House Keeping">House Keeping</option>
                                                <option value="Security">Security</option>
                                            </select>
                                        </div>
                                </div>
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="file-input" class=" form-control-label">Date</label></div>
                                        <div class="col-12 col-md-9"><input type="date" name="date" class="form-control"></div>
                                </div>
								
								<div class="row form-group">
                                        <div class="col col-md-3"><label for="text-input" class=" form-control-label">City</label></div>
                                        <div class="col-12 col-md-9"><input type="text" name="city" class="form-control" value="%s"></div>
                                </div>

								<div class="form-actions form-group" style="padding:10px;">
									
									<input type="reset" class="btn btn-danger btn-sm" value="Clear" style="float:right;">
									<input type="submit" class="btn btn-success btn-sm" value="Send" name="sub" style="float:right;margin-right:10px;">
									
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
"""%(id,r[5]))