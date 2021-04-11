import subprocess as sp
import getopt
import sys
import time


(opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')
command = ""
outfile = ""
log = ""

for args in opt:
    if args[0] == "-c":
        command = args[1]
    elif args[0] == "-f":
        outfile = args[1]
    elif args[0] == "-l":
        log = args[1]
    else:
        print("Error parametros invalidos : ")
        exit()

process = sp.Popen([command], stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True )
output = process.communicate()
stdout = output[0]
stderr = output[1]
output_file = open(outfile, "a")
log_file = open(log, "a")
if stdout != "":
    output_file.write(stdout + "\n")
    log_file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S")+ "Comando " + command +  "Ejecutado correctamente\n")
else:
    log_file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S")+ "Comando "+ command + stderr)
output_file.close()
log_file.close()
