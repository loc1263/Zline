import re

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def dosToUnix(inputfile, outputfile):
    winRegex = re.compile(b'\r\n')

    with open(inputfile, 'rb') as old_file, open(outputfile, 'wb') as new_file:
        while True:
            linea = old_file.readline()
            if not linea:
                break

            if winRegex.findall(linea):
                linea = linea.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
                new_file.write(linea)
            else:
                new_file.write(linea)


def unixToDos(inputfile, outputfile):
    winRegex = re.compile(b'\n')

    with open(inputfile, 'rb') as old_file, open(outputfile, 'wb') as new_file:
        while True:
            linea = old_file.readline()
            if not linea:
                break

            if winRegex.findall(linea):
                linea = linea.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
                new_file.write(linea)
            else:
                new_file.write(linea)

# dosToUnix('file.DOS.txt','file.UNIX.txt')
# unixToDos('file.UNIX.txt','file.DOS.txt')
