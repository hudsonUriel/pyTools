# GIT TOOLS
# ************************************** #
# This library allows convert numbers
# to different bases
#
# The conversion process is made through
# the isomorphic relation between the
# individual aliases of an input string
# with an defined DECODE_ARRAY
#
# ************************************** #
# This tool is licensed under MIT terms.
#
# Be free to:
# [+] run
# [+] study
# [+] change
# [+] improve
# [+] redistribute
# [+] share
# [+] use commercially and privately
#
# ************************************** #

# import
from os import system
from os import chdir
from os import getcwd

# aux file
file_name = 'aux.txt'
file_handler = open(file_name, 'w+')

# aux variables
c_dir = (getcwd() + '/').replace(' ', '\\ ')

# defines
def git():
    """
        This function checks if GIT is installed.

        Returns 'True' or 'False'
    """
    system('whereis git > ' + file_name)

    git_i = file_handler.read().split(':')

    file_handler.close()
    system('rm ' + file_name)

    if git_i[1] == '\n':
        return False
    else:
        return True


def is_repo(directory):
    """
        This function checks if an specified directory
        is a git repository

        Returns 'True' or 'False'
    """

    chdir(directory)
    if system('git log > ' + file_name) != 0:
        return False
    else:
        return True


def first_commit(directory):
    """
        This function returns a list with
        the first commit date. Case the
        directory is not a git repositiory,
        returns 0

        RETURN_LIST = ['WEEK_DAY', 'MONTH', 'DAY', 'TIME', 'YEAR']

        Returns 'True' or 'False'
    """
    if not is_repo(directory):
        return 0
    else:
        system('git log | grep Date: > ' + c_dir + file_name)

        first = file_handler.read().split('Date: ')

        first = first[len(first) -1].replace('  ', '').split()

        first.remove(first[len(first)-1])

        file_handler.close()
        system('rm ' + c_dir + file_name)

        return first

