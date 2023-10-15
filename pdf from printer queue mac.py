# Firstly change the properties of the original folder
#/private/var/spool/ than right- Click on the CUPS folder and use Get Info to change the permission (everyone - Readonly)
#https://apple.stackexchange.com/questions/174841/saving-a-pending-print-job-as-pdf

import os
import shutil

# Path to dstination folder - where to save extracted PDF
desktop_path = os.path.expanduser("~/Desktop")

# Path to directory: /private/var/spool/
spool_path = "/private/var/spool/cups"

# Get the list of files beginnig with letter "d" - hiden PDF files in peinting queue
files_to_copy = [f for f in os.listdir(spool_path) if f.startswith("d")]

# Copy each files as .pdf to the destination folder
for file_name in files_to_copy:
    source_file_path = os.path.join(spool_path, file_name)
    destination_file_path = os.path.join(desktop_path, file_name + ".pdf")

    # Copy files
    shutil.copy2(source_file_path, destination_file_path)

print("Files ware copoed as PDFs.")
