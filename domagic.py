import magic
import argparse
import os

"""
Gaps
-ELF *
-MachO
-Other file types:pe32 executable *

ARM,MIPS,x86-64 etc. *
-More APT (e.g. sophisticated)
-more varied tool types

vbscript
javascript / jscript
python
golang
Delphi
Powershell
.net/ dotnet

"""

# Different kinds of file types



# Other info


# Different kinds of architectures




# Dictionaries to store file types, architecture counts, and endians





# Store amount of files counted and count of files not read
file_count=0


# Create argument parser
parser = argparse.ArgumentParser(description='A python-magic parser',)
# Add the arguments: Enter filepath(s)
parser.add_argument("dir_path",help="paste path to file")
args = parser.parse_args()

for root, dirs, files in os.walk(args.dir_path,topdown=False):
    for file in files:
        f = os.path.join(root,file)
        x=magic.from_file(f)
        print(x)
        file_count+=1





# for file in args.File_Path:
#     x=magic.from_file(file)
#     print(f"Magic:{x}")
#     file_count+=1

# Code to get file type counts

def getfile_types():
    running_totalHTML = 0
    running_totalPE32 = 0
    running_totalELF32 = 0
    running_totalELF64 = 0
    running_totalPE32DotNet = 0
    file_type_other = 0
    file_not_read = 0
    File_Types = {"PE32": 0, "HTML": 0, "ELF 32": 0, "ELF 64": 0}

    if "PE32" in x:
        File_Types["PE32"] += 1
        running_totalPE32 = File_Types["PE32"]
    elif "HTML" in x:
        File_Types["HTML"] += 1
        running_totalHTML = File_Types["HTML"]
    elif "ELF 32" in x:
        File_Types["ELF 32"] += 1
        running_totalELF32 = File_Types["ELF 32"]
    elif "ELF 64" in x:
        File_Types["ELF 64"] += 1
        running_totalELF64 = File_Types["ELF 64"]
    elif x == "data":
        file_not_read += 1
    else:
        file_type_other += 1
    return f"""Count of File Types\n-------------------\nPE32 Files: {running_totalPE32}\nHTML Files: {running_totalHTML}
ELF 32-bit Files: {running_totalELF32}\nELF 64-bit Files: {running_totalELF64}\nOther File Type:{file_type_other}"""


# Get the running totals for architectures
def getArchitecture():
    running_totalx8664 = 0
    running_totalMIPS = 0
    running_totalARM = 0
    architecture_other = 0
    Architectures = {"x86-64": 0, "ARM": 0, "MIPS": 0}


    if "x86-64" in x:
        Architectures["x86-64"] += 1
        running_totalx8664=Architectures["x86-64"]
    elif "MIPS" in x:
        Architectures["MIPS"] += 1
        running_totalMIPS=Architectures["MIPS"]
    elif "ARM" in x:
        Architectures["ARM"] += 1
        running_totalARM = Architectures["ARM"]
    else:
        architecture_other += 1
# Get Other information

def getOther():
    running_total_BigEndian = 0
    running_total_LittleEndian = 0
    running_total_AdobePhotoshopCS6W = 0
    running_total_AdobeReaderXI = 0
    Other = {"big-endian": 0, "Little Endian": 0, "PE32 .NET": 0}

    if "Little Endian" in x:
        Other["Little Endian"] +=1
        running_total_LittleEndian = Other["Little Endian"]
    elif "big-endian" in x:
        Other["big-endian"]+=1
        running_total_BigEndian=Other["big-endian"]
    elif "Mono" in x:
        Other["PE32 .NET"] += 1
        running_totalPE32DotNet = Other["PE32 .NET"]
    return


## Gets percentage value of the amount of files that are not read
# file_accuracy = (file_not_read / file_count) * 100


# Print info here
# print(
#
# Count of Architectures\n----------------------\nx86-64 Architecture: {running_totalx8664}
# MIPS Architecture: {running_totalMIPS}\nARM Architecture: {running_totalARM}\nOther Architecture: {architecture_other}
#
# Other Counts\n--------------------\nLittle Endian Files:{running_total_LittleEndian}
# Big Endian Files:{running_total_BigEndian}\nPE32 dotnet:{running_totalPE32DotNet}
#
# File Count: {file_count} files
#
# Files not Read:{file_not_read} files
#
# """)


# % Files not Read:  {round(file_accuracy,2)} %




# Function Calls
print(getfile_types())


































































