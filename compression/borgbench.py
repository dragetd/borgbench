#!/usr/bin/env python3

import subprocess
import re
import sys
from timeit import default_timer as timer

# single benchmark run
def runConfig(comp, cmin, cmax, cavg, data):
    # make sure there is no leftover repository. This will throw a warning on the shell if there is no folder, but it can be ignored
    subprocess.call(["rm", "-r", "/tmp/borgbench/"+comp])
    # run borg
    subprocess.call(["borg", "init", "-e", "none", "/tmp/borgbench/"+comp])
    start = timer()
    proc=subprocess.Popen(["borg", "create", "/tmp/borgbench/"+comp+"::test", "-v", "-s", "-C", comp, data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.stderr.read()
    duration = timer() - start
    # parse output
    m = re.match(".*This archive: +(\d+\.?\d+ ..) +(\d+\.?\d+ ..) +(\d+\.?\d+ ..).*Chunk index: +(\d+) +(\d+)", str(output))
    if m:
        print(comp+";"+str(cmin)+";"+str(cmax)+";"+str(cavg)+";"+m.group(1)+";"+m.group(2)+";"+m.group(3)+";"+m.group(4)+";"+m.group(5)+";"+str(duration))
    else:
        print("Error")
    # and clean up
    subprocess.call(["rm", "-r", "/tmp/borgbench/"+comp])


# Benchmark calls
# For speed reasons, this should be a tmpfs
testData = "/tmp/borgbench/testdata"
# test different compression values

#print(datetime.now().time())
#exit

runConfig("zlib,0", 0, 0, 0, testData)
runConfig("zlib,1", 0, 0, 0, testData)
runConfig("zlib,2", 0, 0, 0, testData)
runConfig("zlib,3", 0, 0, 0, testData)
runConfig("zlib,4", 0, 0, 0, testData)
runConfig("zlib,5", 0, 0, 0, testData)
runConfig("zlib,6", 0, 0, 0, testData)
runConfig("zlib,7", 0, 0, 0, testData)
runConfig("zlib,8", 0, 0, 0, testData)
runConfig("zlib,9", 0, 0, 0, testData)
runConfig("lzma,0", 0, 0, 0, testData)
runConfig("lzma,1", 0, 0, 0, testData)
runConfig("lzma,2", 0, 0, 0, testData)
runConfig("lzma,3", 0, 0, 0, testData)
runConfig("lzma,4", 0, 0, 0, testData)
runConfig("lzma,5", 0, 0, 0, testData)
runConfig("lzma,6", 0, 0, 0, testData)
runConfig("lzma,7", 0, 0, 0, testData)
runConfig("lzma,8", 0, 0, 0, testData)
runConfig("lzma,9", 0, 0, 0, testData)
