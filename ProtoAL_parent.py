__author__ = 'Wover'

import time
import sys
import shutil
import random
import string
import subprocess
import os

class ProtoAL:

    def __init__(self, reproductionCycle = 10):

        self.age = 0
        self.name = sys.argv[0]
        self.reproductionCycle = reproductionCycle

        #Endless loop
        while True:

            #Higher-level AL should have an event loop.
            #Propogation should be measured according to readiness, not time.
            while self.age <= 1:

                time.sleep(self.reproductionCycle)

                self.age += 1

                #Create child with an 8-char id.
                self.reproduce(8)

    def reproduce(self, nameLength):

        #Higher-level AL, should have machine learning integrated. New learning should be passed on to child.
        #To create multiple children as part of same reproductive cycle, use loop with counter.

        prefix = "ProtoAL_"

        #generate an id using uppercase ASCII and digits

        id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(nameLength))

        suffix = ".py"

        childName = prefix + id + suffix

        #create copy of itself
        shutil.copy(sys.argv[0], os.getcwd() + "\\" + childName)

        print os.getcwd() + "\\" + childName

        #Being child's life as a new process.
        #Won't accept termination commands "nohup"
        #Will be nice and run as a low priority
        subprocess.Popen(["python", os.getcwd() + "\\" + childName])

        #Note: Printing is useless unless you are monitering STDOUT.
        #Create a file logger to exfil records.
        print "Propogation complete."

        print childName + " successfully reproduced."

if __name__ == '__main__':

    life = ProtoAL()
