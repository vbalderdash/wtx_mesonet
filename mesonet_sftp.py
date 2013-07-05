import os
import paramiko

'''Script for pulling all of the data from the mesonet ftp page for a 
given month as specified below into a 'raw_data' directory in the working
directory
'''

year  = '12' # Last two digits only
month = '05' # Two digit month

host = 'llj.wind.ttu.edu'
port = 22
username = ''
password = ''

if not os.path.exists('raw_data'):
    os.makedirs('raw_data')

transport = paramiko.Transport((host, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

files = sftp.listdir()
for i in files:
    if i[-8:-4] == year + month:
        sftp.get(i, 'raw_data/%s' %(i))

sftp.close()
transport.close()
