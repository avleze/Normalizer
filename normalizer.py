###############################################################################
############################### NORMALIZER v1.0 ###############################
###############################################################################
# Author: Antonio Vélez Estévez                                               #       
# Date: 11-25-2016                                                            #
# Dependencies: sox is needed in order to normalize the .mp3 files            #
###############################################################################

import os, re
from subprocess import call

def main():
    parameters = "--norm=-1"
    avaiableExtensions = [".mp3"]


    rootDirectory = os.getcwd()
    currentWorkingDirectory = os.getcwd()

    filenames = []

    for directory in os.walk(rootDirectory):
        currentWorkingDirectory = directory[0]
        os.chdir(currentWorkingDirectory)

        print("Entering into directory " + os.getcwd() + "...")
        filenames = directory[2]
        for filename in filenames:
            if os.path.splitext(filename)[1] in avaiableExtensions:
                print("\tNormalizing " + filename + ".")
                call("sox {0} '{1}' 'new{2}'".format(parameters, filename, filename), shell=True)
                call("rm '{0}'".format(filename), shell=True)
                call("mv 'new{0}' '{1}'".format(filename, filename), shell=True)
        
    print("Completed.")


if __name__=='__main__': 
    main()
