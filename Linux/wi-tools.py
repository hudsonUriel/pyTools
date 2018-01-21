#____________ WI-TOOLS.PY ____________ #
# ******* developed by hUriel ******** #
# ************************************ #
# This tool is licensed under GPL terms.
#
# Be free to:
# [+] run
# [+] study
# [+] change
# [+] improve
# [+] redistribute
# [+] share
# [+] and whatever you want to!
#
# But never forget to keep it free!
#
# "When we speak of free software,
# we are referring to freedom, not
# price."
# __ Gnu Public License 3.0 Preamble
# 



# imports os library
import os


# defines the functions
def main():
    # Welcome message
    os.system('clear')
    print('<' * 10, 'WI-TOOLS', '>' * 10, '\n')

    getIwlist()

def getWirelessInterface(mode):
    # This module searchs for the wireless interface with 'ifconfig' or 'iwconfig' command
    #
    # In Linux systems, it's usually refered as 'wl*', like:
    #   * wlan0
    #
    # The parameter 'mode' recieves the work mode of the function, with:
    #   * 1 = ifconfig
    #   * 2 = iwconfig
    #   * default = iwconfig
    #
    # The variable generic_i_name is set as 'wl', which is used as
    # parameter to a `grep` in ifconfig, which returns the wireless interface
    #
    # The differences between the modules are quite simple: by default, if
    # a wireless interface is defined in a 'iwconfig' command but it is not in
    # a 'ifconfig', the mode 1 will returns false, while 2 will return true.
    # 
    # In this case, the results could be used to turn un the wireless interface using
    # another library or terminal command.
    #
    # The function returns 'interfaceName' or -1
    #   * interfaceName = interface name getted with sucess
    #   * -1 = interface name was not getted

    # verify mode
    if mode == 1:
        mode = 'ifconfig'
    else:
        mode = 'iwconfig'

    # general variables
    fileRead = mode + '.txt'
    generic_i_name = 'wl'

    # prints
    print('-' * 3, '> WIRELESS INTERFACE - {}' .format(mode.upper()))

    # 1. verify wireless interface
    os.system(mode + ' | grep ' +  generic_i_name + ' | cut -d \' \' -f1 | sed \'s/://\' > ' + fileRead)

    # opens fileRead
    fileX = open(fileRead, 'r')

    # reads iwlist
    interface = fileX.read().split('\n')[0]

    # show message
    if interface != '':
        print('\nWireless Interface Detected: \033[42m {} \033[49m\n' .format(interface))
        rtr =  interface
    else:
        print('\n\033[41m No Wireless Interface Detected \033[49m\n')
        rtr = -1

    # removes fileRead
    fileX.close()
    os.system('rm -r ' + fileRead)

    # returns
    return rtr

def setInterface(interface, mode):
    # This module starts or stops a interface using 'ifconfig'
    #
    # 'interface' --> is some of interfaces returned in a 'iwconfig' or 'ifconfig' commands
    # 'mode'      --> is 'up', to turn the interface on, or 'down', to stops it
    #
    # the 'mode' parameter is lowercased and turned automatically in 'up' if it's original
    # value is neither 'up' or 'down'

    # configures and fixes mode
    mode = mode.lower()

    if mode != 'up' or mode != 'down':
        mode = 'up'

    # do it
    os.system('ifconfig ' + interface + mode)

def getIwlist():
    # defines the interface
    interface = getWirelessInterface(1)

    # defines the output file
    fileRead = 'iwlist.txt'
    fileOut = 'iwlistReport-' + str(interface) + '.csv'

    # prints
    print('-' * 3, '> IWLIST')

    if interface != -1:
        # calls iwlist
        os.system('iwlist ' + interface + ' scan > ' + fileRead)

        # opens the fileX
        fileX = open(fileRead, 'r')
        fileR = open(fileOut, 'w')

        # reads fileX
        iwlist = fileX.read().replace('  ', '').split('Cell')

        # number of networks found
        iwlistSize = len(iwlist)

        #iwNet
        for i in range(1, iwlistSize):
            # split per line
            thisN = iwlist[i].split('\n')

            # in 1st. line, gets the Address (BSSID)
            thisN[0] =(thisN[0].split('- ')[1]).split('Address: ')[1]
            fileR.write(thisN[0] + '\t')


            # in the 2nd. line, gets the Channel
            thisN[1] = (thisN[1].split(':')[1])
            fileR.write(thisN[1] + '\t')

            # in the 3rd. line, gets the ESSID
            thisN[2] = (thisN[5].split(':')[1]).replace('"', '')
            fileR.write(thisN[2] + '\n')

        print('\nIWLIST results written in: \033[42m {} \033[49m\n' .format(fileOut))

        # erases the fileRead
        os.system('echo \'\' > ' + fileRead)

        # closes the file
        fileX.close()
        os.system('rm -r ' + fileRead)
    else:
        print('\nNothing to be done ;)\n')

