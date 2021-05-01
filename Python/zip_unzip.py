f=open('file1.txt','w+')
f.write('one file')
f.close()

f=open('file2.txt','w+')
f.write('two file')
f.close()

# zipping a file
import zipfile
comp_file=zipfile.ZipFile('comp_file.zip','w')

comp_file.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# extraction 

zip_object=zipfile.ZipFile('comp_file.zip','r')
zip_object.extractall('extracted')

import shutil

dirToZip='C:\\Users\\ujjwa\\Documents\\Python\\extracted'
output_filename='example'
shutil.make_archive(output_filename,'zip',dirToZip)


#extract

shutil.unpack_archive('example.zip','final_unzip','zip')