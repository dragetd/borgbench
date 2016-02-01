#!/usr/bin/env python3

import subprocess
import re
import sys

# single benchmark run
def runConfig(comp, cmin, cmax, cavg, data):
    # make sure there is no leftover repository. This will throw a warning on the shell if there is no folder, but it can be ignored
    subprocess.call(["rm", "-r", "/tmp/borgbench/"+comp])
    # run borg
    subprocess.call(["borg", "init", "/tmp/borgbench/"+comp])
    proc=subprocess.Popen(["borg", "create", "/tmp/borgbench/"+comp+"::test", "-v", "-s", "-C", comp, "--chunker-params", str(cmin)+","+str(cmax)+","+str(cavg)+",4095", data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.stderr.read()
    # parse output
    m = re.match(".*This archive: +(\d+\.?\d+ ..) +(\d+\.?\d+ ..) +(\d+\.?\d+ ..).*Chunk index: +(\d+) +(\d+)", str(output))
    if m:
        print(comp+";"+str(cmin)+";"+str(cmax)+";"+str(cavg)+";"+m.group(1)+";"+m.group(2)+";"+m.group(3)+";"+m.group(4)+";"+m.group(5))
    else:
        print("Error")
    # and clean up
    subprocess.call(["rm", "-r", "/tmp/borgbench/"+comp])


# Benchmark calls
# For speed reasons, this should be a tmpfs
testData = "/tmp/borgbench/testdata"
# set compression by commandline
comp = str(sys.argv[1])
runConfig(comp, 8, 12, 10, testData)
runConfig(comp, 9, 14, 10, testData)
runConfig(comp, 8, 13, 11, testData)
runConfig(comp, 9, 17, 11, testData)
runConfig(comp, 9, 14, 12, testData)
runConfig(comp, 10, 17, 12, testData)
runConfig(comp, 10, 15, 13, testData)
runConfig(comp, 11, 18, 13, testData)
runConfig(comp, 11, 16, 14, testData)
runConfig(comp, 12, 20, 14, testData)
runConfig(comp, 12, 19, 15, testData)
runConfig(comp, 13, 20, 16, testData)
runConfig(comp, 14, 21, 17, testData)
runConfig(comp, 14, 20, 18, testData)
runConfig(comp, 15, 21, 19, testData)
runConfig(comp, 16, 22, 20, testData)
runConfig(comp, 20, 23, 21, testData)
runConfig(comp, 18, 18, 18, testData)
