import sys
import time



if len(sys.argv) == 4:  # Must have 3 arguments passed to program file / i / j

    result_path = "results.txt"

    file_open = open(sys.argv[1], "r")
    file_result = open(result_path, "w+")

    # Create a list of the lines in the text file
    entries = file_open.readlines()

    # parse to integer the argument passed to the program
    i = int(sys.argv[2])
    j = int(sys.argv[3]) + 1

    print "Loaded %s entries from file" % len(entries)

    # Go through all file lines and write the substrings to the result file
    for entry in entries:
        entry = entry[i:j]+'\n'
        file_result.write(entry)
        

    file_open.close()
    file_result.close()
else:
    print "Insufficient or too much arguments passed to program."
    print "Must specify the file name, starting index and endinf index"
