class Dorks:
    def __init__(self, domain):
        self.domain = domain

    def get_info_dorks(self):
        return [
            f"site:{self.domain} (-www | inurl:admin | inurl:login | inurl:dashboard)",
            f"site:{self.domain} (inurl:api | inurl:dev | inurl:test | inurl:secure)",
            f"site:{self.domain} (inurl:portal | inurl:ftp | inurl:mail | inurl:blog)",
            f"site:{self.domain} (inurl:shop | inurl:static | inurl:cdn)",
            f"site:{self.domain} (inurl:staging | inurl:qa | inurl:beta | inurl:uat)",
            f"site:{self.domain} (inurl:server-status | inurl:server-info)",
            f"site:{self.domain} (inurl:config | inurl:settings | inurl:setup)",
            f"site:{self.domain} (inurl:backup | inurl:old | inurl:archive)",
            f"site:{self.domain} (inurl:temp | inurl:tmp | inurl:cache)",
            f"site:{self.domain} (inurl:debug | inurl:trace | inurl:log)"
        ]

    def get_subdomain_dorks(self):
        return [
            f"site:*.{self.domain}",
            f"site:*.*.{self.domain}",
            f"site:*.*.*.{self.domain}",
            f"site:{self.domain} -www"
        ]

    def get_exposed_files_dorks(self):
        return [
            f"site:{self.domain} (ext:pdf | ext:doc | ext:xls | ext:txt | ext:conf | ext:bak | ext:sql | ext:log)",
            f"site:{self.domain} (filetype:pdf | filetype:doc | filetype:xls | filetype:ppt | filetype:txt | filetype:csv)",
            f"site:{self.domain} (ext:log | ext:git | ext:env | ext:ini | ext:cfg | ext:conf | ext:bak | ext:sql | ext:json | ext:xml)",
            f"site:{self.domain} (filetype:log | filetype:git | filetype:env | filetype:ini | filetype:cfg | filetype:conf | filetype:bak | filetype:sql | filetype:json | filetype:xml)"
        ]

    def get_vulnerability_dorks(self):
        return [
            f"site:{self.domain} (inurl:php?id= | inurl:asp?id= | inurl:jsp?id= | inurl:pl?id= | inurl:cfm?id=)",
            f"site:{self.domain} (inurl:action= | inurl:file= | inurl:download= | inurl:cmd= | inurl:exec=)",
            f"site:{self.domain} (inurl:config= | inurl:include= | inurl:view= | inurl:load= | inurl:redirect=)",
            f"site:{self.domain} (inurl:admin inurl:login | inurl:wp-content | inurl:wp-admin | inurl:wp-includes)",
            f"site:{self.domain} (inurl:phpmyadmin | inurl:shell | inurl:backup | inurl:sql | inurl:db)",
            f"site:{self.domain} (inurl:config.php | inurl:wp-config.php | inurl:web.config | inurl:.env)",
            f"site:{self.domain} (inurl:.git | inurl:.svn | inurl:.htaccess | inurl:robots.txt)",
            f"site:{self.domain} (inurl:crossdomain.xml | inurl:clientaccesspolicy.xml)",
            f"site:{self.domain} (inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page=)",
            f"site:{self.domain} (inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf=)",
            f"site:{self.domain} (inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping=)"
        ]

    def get_camera_iot_dorks(self):
        return [
            "inurl:(viewerframe?mode= | axis-cgi/jpg | axis-cgi/mjpg | view/index.shtml | webcam.html | webcam/ | cam/view.shtml | cam/view.php)"
        ]

    def get_cloud_storage_dorks(self):
        return [
            f"site:(s3.amazonaws.com | s3-external-1.amazonaws.com | s3.dualstack.us-east-1.amazonaws.com) '{self.domain}'",
            f"site:(blob.core.windows.net | dev.azure.com) '{self.domain}'",
            f"site:(googleapis.com | drive.google.com | docs.google.com inurl:'/d/') '{self.domain}'",
            f"site:(onedrive.live.com | sharepoint.com) '{self.domain}'",
            f"site:(digitaloceanspaces.com | dropbox.com/s | box.com/s) '{self.domain}'",
            f"site:(jfrog.io | firebaseio.com) '{self.domain}'"
        ]

    def get_code_docs_dorks(self):
        return [
            f"site:pastebin.com '{self.domain}'",
            f"site:jsfiddle.net '{self.domain}'",
            f"site:codebeautify.org '{self.domain}'",
            f"site:codepen.io '{self.domain}'",
            f"site:{self.domain} (inurl:api | inurl:docs | inurl:documentation)"
        ]

    def get_open_directories_dorks(self):
        return [
            f"site:{self.domain} intitle:index.of",
            f"site:{self.domain} inurl:/public/",
            f"site:{self.domain} inurl:/files/",
            f"site:{self.domain} inurl:/downloads/"
        ]

    def get_sensitive_files_dorks(self):
        return [
            f"site:{self.domain} (filetype:env | filetype:ini | filetype:cfg)",
            f"site:{self.domain} (inurl:password | inurl:secret | inurl:key)",
            "site:{self.domain} inurl:admin",
            f"site:{self.domain} inurl:config",
            f"site:{self.domain} inurl:secure",
            f"site:{self.domain} inurl:private"
        ]

    def get_sql_error_dorks(self):
        return [
            f"site:{self.domain} intext:'SQL syntax'",
            f"site:{self.domain} intext:'mysql_fetch_array'",
            f"site:{self.domain} intext:'Warning: mysql_connect'",
            f"site:{self.domain} intext:'error'",
            f"site:{self.domain} intext:'not found'",
            f"site:{self.domain} intext:'404'",
            f"site:{self.domain} intext:'500'"
        ]

    def get_private_routers_dorks(self):
        return [
            "inurl:(router | gateway | modem) intitle:login",
            "inurl:(router | gateway | modem) intext:'Administration'",
            "inurl:(router | gateway | modem) intext:'Configuration'"
        ]

    def get_login_pages_dorks(self):
        return [
            f"site:{self.domain} inurl:login",
            f"site:{self.domain} inurl:signin",
            f"site:{self.domain} inurl:auth",
            f"site:{self.domain} inurl:account"
        ]

    
        

    def get_backup_files_dorks(self):
        return [
            f"site:{self.domain} ext:bak",
            f"site:{self.domain} ext:backup",
            f"site:{self.domain} ext:old",
            f"site:{self.domain} ext:zip"
        ]

    

    def get_all_dorks(self):
        all_dorks = (
            self.get_info_dorks() +
            self.get_subdomain_dorks() +
            self.get_exposed_files_dorks() +
            self.get_vulnerability_dorks() +
            self.get_camera_iot_dorks() +
            self.get_cloud_storage_dorks() +
            self.get_code_docs_dorks() +
            self.get_open_directories_dorks() +
            self.get_sensitive_files_dorks() +
            self.get_sql_error_dorks() +
            self.get_private_routers_dorks()
        )
        return list(set(all_dorks))

# Example usage:
# dorks = Dorks("example.com")
# print(dorks.get_all_dorks())
