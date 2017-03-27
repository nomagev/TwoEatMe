# Testing for Issue 13:
# Handling Proper CHCP setup on Shell
# https://github.com/nomagev/TwoEatMe/issues/13

import subprocess
 
p = subprocess.Popen("chcp.com", stdout=subprocess.PIPE, shell=True)
 
(output, err) = p.communicate()
 
p_status = p.wait()
print "Command output : ", output
print "Command exit status/return code : ", p_status