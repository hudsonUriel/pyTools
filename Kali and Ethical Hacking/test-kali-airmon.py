#import librarys required
import os

def welcome(textFile):
    # welcome message
    os.system('clear')
    print('*.' * 5, 'Automate Airmon-NG\033[1;m', '*.' * 5)

    # writes the user name in the aux.txt file
    user = os.system('whoami > ' + textFile)


def main():
    # defines textFile
    textFile = 'aux.txt'

    # calls welcome
    welcome(textFile)

    # open aux.txt to read value
    aux = open(textFile, 'r')

    # reads the user in textFile
    user = aux.read().split('\n')
    print('# Hello, {}' .format(user[0]))

    # verify who is the user
    if user[0] != 'root': # if user is not root, exits
        print('Sorry, you are not able to run this script\nContact the \'root\' user' .format(user[0]))
        rtr = -1
    else: # else, runs as root
        print('Let\'s start!\n')



        # 1. detecting main wireless interface
        print('>' * 5, 'Detecting main wireless interface', '<' * 5)

        os.system('iwconfig | grep "wl" | cut -d " " -f1 | sed "s/://" >>' + textFile)

        interface = (aux.read().split('\n'))[0]

        if interface == '': # if there is no wireless interface
            print('\033[41mNo Wireless Interface detected :(\033[49m\nTurn on your wifi card and try again\n')
            rtr = 1
        else:
            print('Wifi Interface Detected: \033[42m{}\033[49m\n' .format(interface))

        # 2. detecting if airmon-ng is installed
            print('>' * 5, 'Detecting airmon-ng', '<' * 5)

            # search for airmon-ng
            os.system('whereis airmon-ng > ' + textFile)
            airmon = aux.read().split(':')[0]

            # verify if airmon-ng is installed
            if airmon != '':
                print ('AIRMON-NG detected!\n')

        # 3. Scaning nearby wireless networks
                print('>' * 5, 'Scaning nearby access point', '<' * 5)
                os.system('iwlist ' + interface + ' scan')

        # 4. Checking and killing process
                print('>' * 5, 'Killing Possible Troubleshot Processes', '<' * 5)
                os.system('airmon-ng check kill')
                print('\033[46mDONE!\033[49m\n')

        # 5. Entering monitor mode
                print('>' * 5, 'Starts Monitor Mode', '<' * 5)
                os.system('airmon-ng start ' + interface + '| grep \'0mon\' | cut -d \']\' -f2 >> ' + textFile)
                interfaceMonitor = aux.read()

                print("Monitor created as \033[46m{}\033[49m\n" .format(interfaceMonitor))

        #6. Capturing packets
                print('>' * 5, 'Capturing packets', '<' * 5)
                os.system('airodump-ng ' + interfaceMonitor + ' --channel 6')

        #n. exits monitor mode
                print('>' * 5, 'Stops Monitor Mode', '<' * 5)
                os.system('airmon-ng stop ' + interfaceMonitor)
                print('\033[46mDONE!\033[49m\n')

            else:
                print('\033[41mAIRMON-NG was not detected.\033[49m\nInstall it and try again.\n')
                rtr = 2

        rtr = 0

    # closes the file
    aux.close()

    # removes the file
    os.system('rm -r ' + textFile)

    # bring interface back to online
    os.system('ifconfig ' + interface + ' up')

    return(rtr)
    # return 0 - normal; -1 = error;
    # 2 = without airmon; 1 = without interface wireless

main()
