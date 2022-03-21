#------------------------------------------#
# Title: CDInventory.py
# Desc: CD Inventory Program for Assignment  08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KChiu, 2022-Mar-20, added codes to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD

    methods:
        __int__(cd_id, cd_title, cd_artist): -> CD object
        print_screen(): -> string in screen display format
        save_file(): -> string in csv format
    """
    # TODone Add Code to the CD class
    #--Fields--#
    #--Constructor--#
    def __init__(self, cd_id, cd_title, cd_artist):
    #--Attributes--#
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    #--Properties--#
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        if type(value) == str:
            try:
                self.__cd_id = int(value)
            except: 
                raise Exception('Excuse Me? CD ID should be numeric!')
        elif type(value) == int:
            self.__cd_id = value
        else:
            raise Exception('Excuse Me? CD ID should be numeric!')
    @property
    def cd_title(self):
        return self.__cd_title.title()

    @cd_title.setter
    def cd_title(self, value):
        if value == '':
            raise Exception('Excuse Me? CD title can\'t be blank!')
        else:
            self.__cd_title = value

    @property
    def cd_artist(self):
        return self.__cd_artist.title()

    @cd_artist.setter
    def cd_artist(self, value):
        if value == '':
            raise Exception('Excuse Me? CD artist can\'t be blank!')
        else:
            self.__cd_artist = value    
    #--Methods--#

    def print_screen(self):
        cd = '{}\t{} (by: {})'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
        return cd

    def wrtie_file(self):
        cd = '{},{},{}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
        return cd

# -- PROCESSING -- #
class FileIO():
    """Processes data to and from file:

    properties:
        None.

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file    
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name and use CD class to 
        convert data into a list of objects

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            None.
        """
        # clear the CD table before loading from the inventory file.
        lstOfCDObjects.clear()
        # read data from file and use CD class to convert each CD into an object.
        # append CD object to the lstOfCDObjects list.
        try:
            with open(file_name, 'r') as objFile:
                for row in objFile:
                    obj = row.strip().split(',')
                    obj = CD(obj[0], obj[1], obj[2])
                    lstOfCDObjects.append(obj)
        except FileNotFoundError:# added error handling if CDInventory file doesn't exist.
            print('\nFileNotFoundError: ' + file_name +' File does not exist!')
    # TODone Add code to process data to a file    
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        # TODone Add code here
        """Function to sync the data in memory to file by saving current table in csv format

        Writes CD data in the lstOfCDObjects in memory to the CDInventory.txt file.
        Each CD object in list uses the wrtie_file() function in CD class to create 
        csv format data to be saved in the file.

        Args:
            file_name (string): name of file used to write/save the data to
            table (list of objects): list that holds the current CD objects during runtime

        Returns:
            None.
        """
        # save data
        try:
            with open(file_name, 'w') as objFile:
                for obj in lst_Inventory:
                    objFile.write(obj.wrtie_file() + '\n')
        except Exception:# added error handling if error arrise during writing data to file.
            print('Something went wrong, please check the CDInventory file.')

# -- PRESENTATION (Input/Output) -- #
class IO():
    # TOoneO add docstring
    """Handling Input / Output

    properties: 
        None.

    methods:
        print_menu(): -> display CD menu
        menu_choice(): -> user choice (string)
        show_inventory(list of inventory): -> string of CD data in a 2D table
        add_cd(cd_id = int, cd_title = str, cd_artist = str): -> CD objects
    """
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD')
        print('[i] Display Current Inventory\n[s] Save Inventory to file\n[x] Exit')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of 
            the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            if choice not in ['l', 'a', 'i', 'd', 's', 'x']:
                print('Please enter a valid option!')
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(cd_list):
        """Displays current inventory table

        Args:
            table (list of object): that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in cd_list:
            print(obj.print_screen())
        print('======================================')
    # TODone add code to get CD data from user

    @staticmethod
    def add_cd(cd_id, cd_title, cd_artist):         
        """Function to add a new cd to lstOfCDObjects table if user chooses to

        Use the CD ID, Title and Artist Name of the new CD to create a CD new object 
        and append to the lstOfCDObjects table

        Args:
            cd_id (integer): ID number of the new CD
            cd_title (string): Title of the new CD
            cd_artist (string): Arist name of the new CD            

        Returns:
            None.
        """
        # create a new object for new cd
        obj = CD(cd_id, cd_title, cd_artist)
        try:
            # use CD class properties to ensure CD ID is an integer 
            # and CD title and artist are not blank
            obj.cd_id = obj.cd_id
            obj.cd_title = obj.cd_title
            obj.cd_artist = obj.cd_artist
            # append new CD object to lstOfCDObjects list
            lstOfCDObjects.append(obj)
        except Exception as e:
            print(e)
# -- Main Body of Script -- #
# TODone Add Code to the main body
# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName)
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        IO.add_cd(strID, strTitle, strArtist)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 's':
        # 3.5.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.5.2 Process choice
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')