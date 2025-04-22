# EXECUTE as:
#  T:\>python c:bckUp.py "Escaneo 2024"
# where T is network shared folder to \\172.16.50.140\cefp\peticiones

#from office365 import Authentication
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext

#from office365.sharepoint.file import File
from office365.sharepoint.files.creation_information import FileCreationInformation

#from OS and SYS support File Management
import os
import sys
import datetime

#Confidential Login Data
url = 'https://camaradiputados.sharepoint.com/sites/cefptecnico'
user = 'tomas.abrego@diputados.gob.mx'
passw = 'rsnoviembre16'

# with extensive LOGGON:
authCtx = AuthenticationContext(url)
swAuth = authCtx.acquire_token_for_user(user, passw)
ctx = ClientContext(url, authCtx)


# UPLOADING a FILE :
#targetFolder = "Documentos compartidos/peticiones/Escaneo 2023"

#if the sys.argv[1] is "Escaneo 2xxx" then this folder must be OMITTED !!!
targetFolder = "Documentos compartidos/peticiones"
folder = ctx.web.get_folder_by_server_relative_url(targetFolder)
#folder = ctx.web.lists.get_by_title("Documents").rootFolder

print(  "target = ",targetFolder)

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

notFoundWeb = []
notFoundLocal = []
notFoundFile = []
for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    roto = root
    root = root.replace("\\", "/")
    #list_file_path = os.path.join(root, 'my-directory-list.txt')
    #print('list_file_path = ' + list_file_path)

    #with open(list_file_path, 'wb') as list_file:
    
    #for subdir in subdirs:
    #    print('\t- subdirectory ' + subdir)

    for filename in files:
        # Two paths: one for local read and one for web sharepoint write
        Win_file_path = os.path.join(roto, filename)  #This join uses the "\\" for dirs 
        m_timestamp = os.path.getmtime(Win_file_path)
        m_datestamp = datetime.datetime.fromtimestamp(m_timestamp)
        
        m_date = m_datestamp.strftime("%Y-%m-%d")
        #SET the DATE when the LAST backup was MADE !!!! =>> 4 de marzo de 2024
        if ( m_date[:10] > "2025-02-09" ):
            file_path = root + "/" + filename

            #print('\t- file %s (full path: %s)' % (filename, file_path))
            path = file_path[1:]

            fileName = file_path[1:]

            #filePath = targetFolder+"/"+fileName "/" it is included in the os.WALK function
            #filePath = targetFolder+fileName
            filePath = targetFolder+"/"+file_path
            #print("check if exists : ",filePath)
            #fileExist = ctx.web.get_folder_by_server_relative_url(filePath).select("Exists").get().execute_query()
            fileExist = ctx.web.get_file_by_server_relative_url(filePath)
            try:
                getFileExist = fileExist.select("Exists").get().execute_query()
                # ClientRequestException, HTTPError, ServerException
            except :
                    print('File NOT FOUND !!!')
                    print(" ===> : ",filePath, " <=== ")
                    swFileExists = False
                    notFoundWeb.append(filePath)
                    notFoundLocal.append(Win_file_path)
                    notFoundFile.append(filename)
                    
            else:
                #print('File Exists !!!')
                #print(" SharePoint path ==> [",filePath, "] <=== ")
                #print("  Local Win path ==> [",Win_file_path, "] <=== ")
                #print('.', end=" ") # prints until the full line is set ...
                sys.stdout.write('.') # SAME place : prints until the full line is set ...
                swFileExists = True
                # #fileExist = fileExist.get().execute_query()
                #fileExist.get().execute_query()
                #print( "File was already into : {0}".format( fileExist.serverRelativeUrl ) )

print( "" )
print( "Missing Files :", len( notFoundFile ) )
#fLog = open("c:logMissing.txt", "a")
fLog = open("c:logMissing.txt", "a")
for i in range(len(notFoundFile)):
	print( i, "\t", notFoundFile[i], "\t", notFoundWeb[i], "\t", notFoundLocal[i] )
	fLog.write(""+notFoundFile[i]+"\t"+notFoundWeb[i]+ "\t"+ notFoundLocal[i]+"\n")
fLog.close()
