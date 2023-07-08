#!C:/Users/Naveen kumar/AppData/Local/programs/python/python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql,os,cgitb;cgitb.enable()

conn=pymysql.connect(host="localhost",user="root",password="",database="nexus")
cur=conn.cursor()

f=cgi.FieldStorage()
st=f.getvalue("st")
cid=f.getvalue("cid")
if st!=None and cid!=None:
	q="""update contractors set status='%s' where cnr_id='%s'"""%(st,cid)
	cur.execute(q)
	conn.commit()
	print("""
		<script>
			alert("Request %sed Successfully !!");
			location.href="admc_exis.py";
		</script>
		"""%(st))

q="""select * from contractors where status='Pending'"""
cur.execute(q)
r=cur.fetchall()
cnt=0
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
    <link rel="stylesheet" href="assets/css/lib/datatable/dataTables.bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">

    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800' rel='stylesheet' type='text/css'>

	
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
                        <a href="admmain.py">Dashboard</a>
                    </li>
					<li class="menu-item-has-children dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Workers</a>
                        <ul class="sub-menu children dropdown-menu">
                            <li><a href="admw_new.py">New</a></li>
                            <li><a href="admw_exis.py">Existing</a></li>
                        </ul>
                    </li>
					<li class="menu-item-has-children dropdown active">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Contractors</a>
                        <ul class="sub-menu children dropdown-menu">
                            <li><a href="admc_new.py">New</a></li>
                            <li><a href="admc_exis.py">Existing</a></li>
                        </ul>
                    </li>
					<li class="menu-item-has-children dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Users</a>
                        <ul class="sub-menu children dropdown-menu">
                            <li><a href="admu_new_req.py">New Requests</a></li>
                            <li><a href="admu_exis_orders.py">Existing Orders</a></li>
                            <li><a href="admu_view.py">Users</a></li>
                        </ul>
                    </li>
					<li>
                        <a href="adm_feedback.py">Feedback</a>
                    </li>
					<li>
                        <a href="adm_payments.py">Payments</a>
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
            <div class="top-right">
                <div class="header-menu">
                    <div class="header-left">

						<div class="user-area dropdown float-right">
							<a href="#" class="dropdown-toggle active" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							<img class="user-avatar rounded-circle" src="images/admin.jpg" alt="User Avatar">
							</a>

							<div class="user-menu dropdown-menu">
								<a class="nav-link" href="#"><i class="fa fa- user"></i>Admin</a>
							</div>
						</div>
                    </div>
                </div>
            </div>
        </header>
        <!-- /#header -->
		 <div class="content" style="margin-top:60px;">

            <div class="animated fadeIn">
                <div class="row">

                    <div class="col-md-12">
                        <div class="card">
                            <div class="card-header">
                                <strong class="card-title">New Contractors Requests</strong>
                            </div>
                            <div class="card-body">
                                <table id="bootstrap-data-table" class="table table-striped table-bordered">
                                    <thead>
                                        <tr>
                                            <th>S.No.</th>
                                            <th>Company</th>
                                            <th>Profile</th>
                                            <th>Name</th>
                                            <th>Contact</th>
                                            <th>E-Mail</th>
                                            <th>City</th>
                                            <th>Type of Services</th>
                                            <th>Working day</th>
                                            <th>Id Proof</th>
                                            <th>Status</th>
                                        </tr>
                                    </thead>
                                    <tbody>""")
for i in r:    
	cnt=cnt+1
	fn="files/"+i[9]
	fn1="files/"+i[10]
	print("""                          
			<tr>
				<td>%s</td>
				<td>%s</td>
				<td class="avatar">
					<div class="round-img">
						<a href="%s" target="blank"><img class="rounded-circle" src="%s" width="50" height="50"alt=""></a>
					</div>
				</td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
				<td>%s</td>
				<td class="avatar">
					<div class="round-img">
						<a href="%s" target="blank"><img class="rounded-circle" src="%s" width="50" height="50" alt=""></a>
					</div>
				</td>
				<td><a href="admc_new.py?st=%s&cid=%s">Accept</a><br><a href="admc_new.py?st=%s&cid=%s">Reject</a></td>
				
			</tr>"""%(cnt,i[1],fn,fn,i[3],i[4],i[5],i[6],i[7],i[8],fn1,fn1,'Accept',i[1],'Reject',i[1]))
print("""
       </tbody>
                                </table>
                            </div>
                        </div>
                    </div>


                </div>
            </div><!-- .animated -->
        </div><!-- .content -->
<script src="https://cdn.jsdelivr.net/npm/jquery@2.2.4/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.4/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/jquery-match-height@0.7.2/dist/jquery.matchHeight.min.js"></script>
    <script src="assets/js/main.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"></script>

    <script src="assets/js/lib/data-table/datatables.min.js"></script>
    <script src="assets/js/lib/data-table/dataTables.bootstrap.min.js"></script>
    <script src="assets/js/lib/data-table/dataTables.buttons.min.js"></script>
    <script src="assets/js/lib/data-table/buttons.bootstrap.min.js"></script>
    <script src="assets/js/lib/data-table/jszip.min.js"></script>
    <script src="assets/js/lib/data-table/vfs_fonts.js"></script>
    <script src="assets/js/lib/data-table/buttons.html5.min.js"></script>
    <script src="assets/js/lib/data-table/buttons.print.min.js"></script>
    <script src="assets/js/lib/data-table/buttons.colVis.min.js"></script>
    <script src="assets/js/init/datatables-init.js"></script>


    <script type="text/javascript">
        $(document).ready(function() {
          $('#bootstrap-data-table-export').DataTable();
      } );
  </script>


</body>
</html>
""")