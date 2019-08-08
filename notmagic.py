import os
import time

start = time.time()

# Dictionaries to store information
File_Types = {"PE32": 0, "HTML": 0, "ELF 32": 0, "ELF 64": 0, "PE32 .NET": 0, "Python": 0, "XML": 0,
              "ASCII": 0, "Perl": 0, "Java": 0, "PHP": 0}
Architectures = {"x86-64": 0, "ARM": 0, "MIPS": 0, "Intel 80386": 0}
Endian = {"x86-64 LSB": 0, "x86-64 MSB": 0, "ARM LSB": 0, "ARM MSB": 0, "MIPS LSB": 0, "MIPS MSB": 0,
          "ELF 64 LSB": 0, "ELF 64 MSB": 0, "ELF 32 LSB": 0, "ELF 32 MSB": 0, "Intel 80386 MSB": 0,
          "Intel 80386 LSB": 0}

# Reminder MSB is big Endian LSB is little endian

# File info
running_totalHTML = 0
running_totalPE32 = 0
running_totalELF32 = 0
running_totalELF64 = 0
running_totalPE32DotNet = 0
running_totalPython = 0
running_totalXML = 0
running_totalASCII = 0
running_totalPERL = 0
running_totalJava = 0
running_totalPHP=0
file_type_other = 0
file_count = 0
file_not_read = 0

# Endians
running_totalx8664smallE = 0
running_totalx8664bigE = 0
running_totalARMsmallE = 0
running_totalARMbigE = 0
running_totalMIPSsmallE = 0
running_totalMIPSbigE = 0
running_totalELF64smallE = 0
running_totalELF64bigE = 0
running_totalELF32smallE = 0
running_totalELF32bigE = 0
running_totalIntel80386smallE = 0
running_totalIntel80386bigE = 0

# Different kinds of architectures
running_totalx8664 = 0
running_totalMIPS = 0
running_totalARM = 0
running_totalIntel80386 = 0
architecture_other = 0

# File Path
filepath = os.chdir("../../Documents")

# Read file line-by-line
with open("/home/aglorioso/Documents/malware_filetypes.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
        file_count += 1

        # File Types
        if "PE32" in line:
            File_Types["PE32"] += 1
            running_totalPE32 = File_Types["PE32"]
        elif "HTML" in line:
            File_Types["HTML"] += 1
            running_totalHTML = File_Types["HTML"]
        elif "ELF 32" in line:
            File_Types["ELF 32"] += 1
            running_totalELF32 = File_Types["ELF 32"]
            if "ELF 32-bit" and "MSB" in line:
                Endian["ELF 32 MSB"] += 1
                running_totalELF32bigE = Endian["ELF 32 MSB"]
            elif "ELF 32-bit" and "LSB" in line:
                Endian["ELF 32 LSB"] += 1
                running_totalELF32smallE = Endian["ELF 32 LSB"]
        elif "ELF 64" in line:
            File_Types["ELF 64"] += 1
            running_totalELF64 = File_Types["ELF 64"]
            if "ELF 64-bit" and "LSB" in line:
                Endian["ELF 64 LSB"] += 1
                running_totalELF64smallE = Endian["ELF 64 LSB"]
            elif "ELF 64" and "MSB" in line:
                Endian["ELF 64 MSB"] += 1
                running_totalELF64bigE = Endian["ELF 64 MSB"]
        elif "Python" in line:
            File_Types["Python"] += 1
            running_totalPython = File_Types["Python"]
        elif "XML" in line:
            File_Types["XML"] += 1
            running_totalXML = File_Types["XML"]

        elif "Perl" in line:
            File_Types["Perl"] += 1
            running_totalPERL = File_Types["Perl"]
        elif "ASCII" in line:
            File_Types["ASCII"] += 1
            running_totalASCII = File_Types["ASCII"]
        elif "Java" in line:
            File_Types["Java"] += 1
            running_totalJava = File_Types["Java"]
        elif "PHP" in line:
            File_Types["PHP"] += 1
            running_totalPHP = File_Types["PHP"]
        else:
            file_type_other += 1
        # Extra case for dotnet
        if "Mono" in line:
            File_Types["PE32 .NET"] += 1
            running_totalPE32DotNet = File_Types["PE32 .NET"]

        # Architectures
        if "x86-64" in line:
            Architectures["x86-64"] += 1
            running_totalx8664 = Architectures["x86-64"]
            if "LSB Executable" and "x86-64" in line:
                Endian["x86-64 LSB"] += 1
                running_totalx8664smallE = Endian["x86-64 LSB"]
            elif "MSB Executable" and "x86-64" in line:
                Endian["x86-64 MSB"] += 1
                running_totalx8664bigE = Endian["x86-64 MSB"]
        elif "ARM" in line:
            Architectures["ARM"] += 1
            running_totalARM = Architectures["ARM"]
            if "ARM" and "MSB" in line:
                Endian["ARM MSB"] += 1
                running_totalARMbigE = Endian["ARM MSB"]
            elif "ARM" and "LSB" in line:
                Endian["ARM LSB"] += 1
                running_totalARMsmallE = Endian["ARM LSB"]
        elif "MIPS" in line:
            Architectures["MIPS"] += 1
            running_totalMIPS = Architectures["MIPS"]
            if "MIPS" and "MSB" in line:
                Endian["MIPS MSB"] += 1
                running_totalMIPSbigE = Endian["MIPS MSB"]
            elif "MIPS" and "LSB" in line:
                Endian["MIPS LSB"] += 1
                running_totalMIPSsmallE = Endian["MIPS LSB"]
        elif "Intel 80386" in line:
            Architectures["Intel 80386"] += 1
            running_totalIntel80386 = Architectures["Intel 80386"]
            if "Intel 80386" and "LSB" in line:
                Endian["Intel 80386 LSB"] += 1
                running_totalIntel80386smallE = Endian["Intel 80386 LSB"]
            elif "Intel 80386" and "MSB" in line:
                Endian["Intel 80386 MSB"] += 1
                running_totalIntel80386bigE = Endian["Intel 80386 MSB"]
        else:
            architecture_other += 1


end=time.time()



# print statements
print(f""" 
Total Files Read: {file_count}

Count by File Type
------------------
PE32: {running_totalPE32} files
HTML: {running_totalHTML} files
ELF 32-bit: {running_totalELF32} files
ELF 64-bit: {running_totalELF64} files
Dotnet: {running_totalPE32DotNet} files
Python: {running_totalPython} files
Perl: {running_totalPERL} files
ASCII text: {running_totalASCII} files
XML: {running_totalXML} files
Java: {running_totalJava} files
PHP: {running_totalPHP} files


Unread Files: {file_not_read}
Other File Types: {file_type_other}

Count By Architecture
---------------------
x86-64: {running_totalx8664} files
ARM: {running_totalARM} files
MIPS: {running_totalMIPS} files
Intel 80386: {running_totalIntel80386} files
Other Architecture: {architecture_other}

Count by Endianness
-------------------
***Big Endian***
ELF 32-Bit: {running_totalELF32bigE} files
ELF 64-Bit: {running_totalELF64bigE} files
x86-64: {running_totalx8664bigE} files
ARM: {running_totalARMbigE} files
MIPS: {running_totalMIPSbigE} files
Intel 80386: {running_totalIntel80386bigE} files

***Little Endian***
ELF 32-Bit: {running_totalELF32smallE} files
ELF 64-Bit: {running_totalELF64smallE} files
x86-64: {running_totalx8664smallE} files
ARM: {running_totalARMsmallE} files
MIPS: {running_totalMIPSsmallE} files
Intel 80386: {running_totalIntel80386smallE} files

Totals
-------
File types Known: {sum(File_Types.values())}
File types Unknown:{(file_count) - sum(File_Types.values())}
Files with Known Architectures:{sum(Architectures.values())}
Files with no Architecture/ unknown architecture: {architecture_other - sum(Architectures.values())}


Runtime:{round((end-start),3)} seconds

""")
