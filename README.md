# Zline  
## Remove character (on the fly)

Input file (DOS format)

1234567801  
123456789  
2345676543  
123454326  
232343455  
  
Output file (DOS format) (same file on the fly)  
123456781  
123456789  
234567653  
123454326  
232343455  
  
Second file in unix format (_out)  
123456781  
123456789  
234567653  
123454326  
232343455  

Run:  
Python Zline.py inputfile  

# Code

```python
import fileinput
import sys
import time
import CRLF

def remove_at(i, s):
    return s[:i] + s[i + 1:]


def inline(s):
    max_length = 10
    count_fix = 0
    for line in fileinput.input(s, inplace=True):
        if len(line) > max_length:
            num_line = fileinput.filelineno()
            sys.stderr.write("Line: %s Len: %s \n" % (num_line, len(line)))
            line2 = remove_at(8, line)
            print('{}'.format(line2), end='')
            count_fix = count_fix + 1
        else:
            print('{}'.format(line), end='')

    sys.stderr.write("Record Fix: %s \n" % count_fix)


def main(argv):
    sys.stderr.write("File: %s \n" % argv)
    sys.stderr.write("Fixing records.\n")
    start_time = time.time()
    inline(argv)
    print("Fix time: %s sec " % (time.time() - start_time))

    sys.stderr.write("Convert file to Unix.\n" )
    fileOutput=argv + '_out'
    sys.stderr.write("Output file: %s \n" % fileOutput)
    start_time = time.time()
    CRLF.dosToUnix(argv,fileOutput)
    print("Convert time %s sec " % (time.time() - start_time))
	
	
if __name__ == "__main__":
    main(sys.argv[1])
  
```

