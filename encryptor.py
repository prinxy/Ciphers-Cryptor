"""
    This is a File Encryptor and Decryptor
"""
import time
import tkinter as tk

root = tk.Tk()
root.geometry ( "550x500" )
root.title ( "Ciphers Hub" )
root.resizable ( False, False )


MAX_VALUE = 26

DEVELOPERS = [ "Abonze Prince" ]


# colors
MYCOLORS = [
                "#DC143C",       # Crimson
                "#FFF0F5",       # Lavenderblush 1
                "#8B5F65",       # LIghtpink4
                "#00E5EE",       # Turquoise 1
                "#00688B",       # DeepSkyBlue
           ]

# fonts 
H_TIMES = ('Times', 22, 'bold')
B_TIMES = ('Times', 12, 'bold')
T_TIMES = ('Times', 18, 'italic')
TIMES = ('Times', 15)
TIMES_I = ( 'Times', 12, 'italic')



file_name = tk.StringVar()
encryption_level = tk.IntVar()


class CipherHub ( tk.Frame ):

    """
         This class basically helps to switch windows in this app by
         calling classes
    """

    def __init__ ( self, *args, **kwargs ):
        tk.Frame.__init__ ( self, *args, **kwargs )

        self.box = tk.Frame ( root )
        self.box.grid ( column = 0, row = 0 )
        self.box.grid_rowconfigure ( 0, weight = 1 )
        self.box.grid_columnconfigure ( 0, weight = 1 )
        
        self.class_switcher()


    def class_switcher ( self ):

        self.frames = {}

        for counter in ( Startpage, Encrypt, Decrypt, Bruteforce):

            frame  = counter ( self.box, self )
            self.frames [counter] = frame
            frame.grid ( row = 3, column = 0, sticky = 'nsew' )

        self.show_frame ( Startpage )


    def show_frame ( self, cont ):

        frame = self.frames [ cont ]
        frame.tkraise()





class Startpage ( tk.Frame ):

    def __init__ ( self, parent, controller ):
        
        tk.Frame.__init__ ( self, parent )
        self.controller = controller

        self.layout()


    def layout ( self ):
        """
            This is the startpage Layout
        """

        frame = tk.Frame ( self )
        frame.grid ( column = 0, row = 1 )

     
        app_name = tk.Label ( frame, text = "Ciphers Cryptor", font = H_TIMES, bg = MYCOLORS[1])
        app_name.grid ( column = 0, row = 2, padx = 9, pady = 9, ipadx = 15 )

        

        quit_label = tk.Label ( frame, text = "QUIT", font = TIMES, fg = MYCOLORS [0], anchor = "e")
        quit_label.bind ("<Button -1>", exit )
        quit_label.grid ( column = 2, row = 2, sticky = "e", padx = 15, pady = 5 )


        spacer = tk.Label ( frame, text = " " ).grid ( column = 0, row = 3, pady = 50 )


        encrypt_button = tk.Button ( frame, text = "Encrypt", font = B_TIMES, bg = MYCOLORS[1],
            fg = MYCOLORS[2], command = lambda : self.controller.show_frame ( Encrypt ))
        encrypt_button.grid ( column = 0, row = 4, padx = 20, pady = 10)


        decrypt_button = tk.Button ( frame, text = "Decrypt", font = B_TIMES, bg = MYCOLORS[3],
            fg = MYCOLORS[0], command = lambda  : self.controller.show_frame ( Decrypt ))
        decrypt_button.grid ( column = 1, row = 4, padx = 40, pady = 10 )


        brute_button = tk.Button ( frame, text = "Brute Force", font = B_TIMES, bg = MYCOLORS[0],
            fg = MYCOLORS[3], command = lambda : self.controller.show_frame ( Bruteforce ))
        brute_button.grid ( column = 2, row = 4, padx = 50, pady = 40 )


        self.image()


    def image( self ):

        path = "/home/prince/Desktop/Encryptor/image/file0.png"
        

        photo = tk.PhotoImage ( file = path )
        resized_pics = photo.subsample ( 3, 3 )

        image = tk.Label ( self, image = resized_pics, width = 300, height = 100 )
        image.image = resized_pics
        image.grid ( column = 0, row = 4, padx = 50, pady = 10 )


        #About Labels
        
        about = tk.Label ( self, text = "About Ciphers Cryptor", font = TIMES_I )
        about.grid ( column = 0, columnspan= 2, row = 6, padx = 50, pady = 60, sticky = 'w' )

        cipher_help = tk.Label ( self, text = "Help", font = TIMES_I )
        cipher_help.grid ( column = 0, row = 6, padx = 260, pady = 60, sticky = 'w' )

        about_dev = tk.Label ( self, text = "About Developers", font = TIMES_I )
        about_dev.grid ( column = 0, row = 6, padx = 50, pady = 60, sticky='e' )


        #Binding about Labels
        
        about.bind ( "<Button -1>", self.about )
        cipher_help.bind ( "<Button -1>", self.cipher_help )         
        about_dev.bind ( "<Button -1>", self.about_dev )





    def about ( self, event ):
        frame = tk.Toplevel ( self, bg = MYCOLORS[1] )
        frame.geometry ( "400x250" )
        frame.title ("About Ciphers Cryptor")
        frame.resizable ( False, False )
        frame.grid()

        title = tk.Label ( frame, text = "Ciphers Cryptor", fg = MYCOLORS[0], bg = MYCOLORS[1],
            font = H_TIMES )
        title.grid(column = 0, row = 1, padx = 110, pady = 10 )

        message = "Created by Agbonxoft Prince\n November 2017 \n @copyright"
        msg = tk.Label ( frame, text = message, fg = MYCOLORS[2], bg = MYCOLORS[1], justify = 'center')
        msg.grid ( column = 0, columnspan = 3,  row = 2, padx = 100, pady = 35, sticky = 'e' )





    def cipher_help ( self, event ):
        frame = tk.Toplevel ( self, bg = MYCOLORS[1] )
        frame.geometry ( "500x600" )
        frame.title ("Help")
        frame.resizable ( False, False )
        frame.grid()

        title = tk.Label ( frame, text = "Help", fg = MYCOLORS[0], bg = MYCOLORS[1],
            font = H_TIMES )
        title.grid(column = 0, row = 1, padx = 5, pady = 10, columnspan = 3, sticky = 'w')

        info_about = "CIPHERS CRYPTOR is an App that helps Encrypt, Brute Force File Content with an Encryption Digit Provided"
        info_text = tk.Label ( frame, text = info_about, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        info_text.grid ( column = 0, row = 2, padx = 10, pady = 15, columnspan = 3, sticky='w' )


        #ENCRYPTION DIGIT HELP
        encrypt_digit = "Encrypt Digit"
        encrypt_d_title = tk.Label ( frame, text = encrypt_digit, font = T_TIMES, bg = MYCOLORS[1],
            fg = MYCOLORS[0] )
        encrypt_d_title.grid ( column = 0, row = 3, padx = 10, pady = 5, columnspan = 3, sticky = 'w')


        encrypt_d_info = "CIPHERS CRYPTOR encryption digit is like a password that is needed to decrypt an encrypted file or encrypt a file. It is advisable to keep your encryption key as safe as possible to avoid risk of loosing  file content to spoofers"
        encrypt_d_text = tk.Label ( frame, text = encrypt_d_info, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        encrypt_d_text.grid ( column = 0, row = 4, padx = 15, pady = 3, columnspan = 3, sticky = 'w')


        #ENCRYPT HELP
        encrypt_title = tk.Label ( frame, text = "Encrypt", font = T_TIMES, bg = MYCOLORS[1],
            fg = MYCOLORS[0] )
        encrypt_title.grid ( column = 0, row = 5, padx = 10, pady = 5, columnspan = 3, sticky = 'w')

        encrypt_info = "This Option Enables you to Encrypt File Content to a cipher lock based on the encryption digit you passed to it. Encryption Key passed here should be remembered for Decryption and kept safe to avoid risk of loosing file content."
        encrypt_text = tk.Label ( frame, text = encrypt_info, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        encrypt_text.grid ( column = 0, row = 6, padx = 15, pady = 3, columnspan = 3, sticky = 'w')


        #DECRYPT HELP
        decrypt_title = tk.Label ( frame, text = "Decrypt", font = T_TIMES, bg = MYCOLORS[1],
            fg = MYCOLORS[0] )
        decrypt_title.grid ( column = 0, row = 7, padx = 10, pady = 5, columnspan = 3, sticky = 'w')

        decrypt_info = "This Option Enables you to  Decrypt File Content to an actual File based on the encryption digit you passed to it. Encryption key to be passed should be same with that used to Encrypt the File content, else file content will end up Re-Encrypted."
        decrypt_text = tk.Label ( frame, text = decrypt_info, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        decrypt_text.grid ( column = 0, row = 8, padx = 15, pady = 3, columnspan = 3, sticky = 'w')

        #BRUTE FORCE HELP
        decrypt_title = tk.Label ( frame, text = "Brute Force", font = T_TIMES, bg = MYCOLORS[1],
            fg = MYCOLORS[0] )
        decrypt_title.grid ( column = 0, row = 9, padx = 10, pady = 5, columnspan = 3, sticky = 'w')

        brute_info = "This option Forces Decryption of File to %s possible Contents. NOTE: Encryption digit is not needed for this option" % MAX_VALUE
        brute_text = tk.Label ( frame, text = brute_info, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        brute_text.grid ( column = 0, row = 10, padx = 15, pady = 3, columnspan = 3, sticky = 'w')
        

        
        

    def about_dev ( self, event ):
        # This will tell more about developers that builds Ciphers Cryptor
        frame = tk.Toplevel ( self, bg = MYCOLORS[1] )
        frame.geometry ( "500x250" )
        frame.title ("Help")
        frame.resizable ( False, False )
        frame.grid()

        title = tk.Label ( frame, text = "About Developers", fg = MYCOLORS[0], bg = MYCOLORS[1],
            font = H_TIMES )
        title.grid(column = 0, row = 1, padx = 5, pady = 10, columnspan = 3, sticky = 'w')

        Dev_name = tk.Label ( frame, text = DEVELOPERS[0], fg = MYCOLORS[2], bg = MYCOLORS[1],
            font = T_TIMES )
        Dev_name.grid(column = 0, row = 2, padx = 190, pady = 10 )

        about_me = "I am a Freelance programmer, which love working on an opensource programs. My specialty is in C++, Python, HTML, CSS, and C.\nWhatsapp no: 09034504163"
        dev_text = tk.Label ( frame, text = about_me, fg = MYCOLORS[2], bg = MYCOLORS[1],
            wraplength = 450, justify = 'left')
        dev_text.grid ( column = 0, row = 3, padx = 15, pady = 3, columnspan = 3, sticky = 'w')
        

        



        

        


class Interface( tk.Frame ):
    """
        This interface class is the basic layout of all the other classes excluding Startpage
        All other class will have to inherit from this class
    """
    
    def __init__  ( self, parent ):
        tk.Frame.__init__ ( self, parent  )
        self.parent = parent
        
        
        self.level_label = tk.Label ( parent, text = "Encryption digit", font = TIMES_I )
        self.level_label.grid ( column = 1, row = 1, sticky = "w", padx = 110, pady = 5)
        self.level_entry = tk.Entry ( parent, textvariable = encryption_level, width = 3, font = TIMES)
        self.level_entry.grid ( column = 1, row = 1, padx = 210, sticky = "e", pady = 5 )
        

        
        back_button = tk.Label ( parent, text = "Back", font = TIMES, fg = MYCOLORS[4])
        back_button.bind ( "<Button -1>", lambda e: parent.controller.show_frame ( Startpage))
        back_button.grid ( column = 1, row = 1, padx = 30, sticky = 'e')


        spacer = tk.Label ( parent, text = " " ).grid ( column = 0, row = 2, pady = 10)
        
        
        save_as = tk.Label ( parent, text = "Save as: ", font = TIMES, fg = MYCOLORS[2] )
        save_as.grid ( column = 0, row = 3, pady = 10 )
        
        
        self.file_entry = tk.Entry ( parent, textvariable = file_name, width = 40, font = TIMES )
        self.file_entry.grid ( column = 1, row = 3, ipadx= 3, ipady = 3, padx = 10, sticky = "w")

        
        txt_label = tk.Label ( parent, text = "Enter Message", font = TIMES, fg = MYCOLORS [2] )
        txt_label.grid (  column = 1, row = 4, padx = 105, pady = 5, sticky = "w")


        self.msg_box = tk.Text ( self.parent, width = 70, height = 15 )
        self.msg_box.grid ( column = 0, row = 5, padx = 10, columnspan = 2, sticky = "w")
        
        scrollbar = tk.Scrollbar ( self.parent, orient= 'vertical', command = self.msg_box.yview )
        scrollbar.grid ( column = 1, row = 5, sticky = "nse", padx = 35)

        self.msg_box['yscrollcommand'] = scrollbar.set        


    def message ( self ):
        """
            This handles the message box so text input can be entered
        """
        msg_box_text = self.msg_box.get ("1.0", 'end-1c') 
        if len ( msg_box_text ) == 0:
            self.error_frame ()
        else:
            return msg_box_text



    def error_frame ( self ):

        frame = tk.Toplevel ( self, bg = MYCOLORS[1] )
        frame.grid ()

        error_label = tk.Label ( frame, text = "Error", fg = MYCOLORS[0] , bg = MYCOLORS[1]  , justify= "left",
            font = T_TIMES )
        error_label.grid ( column = 0, row = 1, sticky = "W", padx = 3, pady = 3 )


        e_msg = "Text Box Left Empty"

        error_msg = tk.Label ( frame, text = e_msg, font = TIMES, justify = "left",
            bg = MYCOLORS[1], fg = MYCOLORS[2] )
        error_msg.grid ( column = 0, row = 2, sticky = "W", padx = 3, pady = 3 )


        ok_button = tk.Button ( frame, text = "Ok", fg = MYCOLORS[1] , bg = MYCOLORS[0] , command = frame.destroy )
        ok_button.grid ( column = 0, row = 3, padx = 50, pady = 5 )

        
        


class Encrypt (tk.Frame ):
    
    """
        This class handles all of your encryption based on the digit you provide to it.
        If the encryption digit is 0, it keeps the exact text for you.
    """

    def __init__ ( self, parent, controller ):
        tk.Frame.__init__ ( self, parent )
        self.controller = controller
        self.parent = parent 


        self.layout ()




    def layout ( self ):
        """
            This method only creates the title of each of the class in this case will be 'ENCRYPT'
        """

        frame = tk.Frame ( self )
        frame.grid ( column = 0, row = 1 )
        

        title = tk.Label ( frame, text = "Encrypt", font = H_TIMES, fg = MYCOLORS[0] )
        title.grid ( column = 0, row = 2, padx = 5, pady = 5 )


        
        save_button = tk.Button ( self, text = "Save", font = TIMES, fg = MYCOLORS[0],
            bg = MYCOLORS[1], command = lambda : self.controller.show_frame ( Startpage ))
        save_button.bind ("<Button -1>", self.encrypt_text)
        save_button.grid ( column = 0, row = 6, padx = 10, pady = 10, columnspan = 2, sticky= "s")

        info_text = tk.Label ( self, text = "Don't loose your Encrytion digit", font = TIMES_I )
        info_text.grid ( column = 0, row = 7, padx = 10, pady = 10, columnspan = 2, sticky = 's' )
        
        self.interface = Interface ( self )



        
    def encrypt_text ( self, event ):
        """
            This handles the encryption of the text collected by the get_text
        """

        text = self.interface.message()
        filename = file_name.get()
        filename += ".txt"
        encryptlevel = encryption_level.get()
        translated = ''

        for word in text.strip():
            for char in word:
                if char.isalpha ():
                        
                    level = ord ( char )
                    level += encryptlevel

                    if char.isupper():
                            
                        if level > ord ('Z'):
                            level -= MAX_VALUE
                        elif level < ord ('A'):
                            level += MAX_VALUE
                                

                    elif char.islower ():

                        if level > ord ('z'):
                            level -= MAX_VALUE
                        elif level < ord ('a'):
                            level += MAX_VALUE            
                    
                    translated += chr ( level )     
                else:
                    translated += char

                try:    
                    with open ( filename, 'w') as f:
                        f.write ( translated )
                        
                except FileNotFoundError:
                    print ( "No such file or directory: %s" % filename )

                            



class Decrypt (tk.Frame ):
    """
        This class will decrypt your files with the Max key you pass in
    """

    def __init__ ( self, parent, controller ):
        tk.Frame.__init__ ( self, parent )
        self.controller = controller
        self.parent = parent 


        self.layout ()


    def layout ( self ):
        """
            This method only creates the title of each of the class in this case will be 'ENCRYPT'
        """

        frame = tk.Frame ( self )
        frame.grid ( column = 0, row = 1 )
        

        title = tk.Label ( frame, text = "Decrypt", font = H_TIMES, fg = MYCOLORS[0] )
        title.grid ( column = 0, row = 2, padx = 5, pady = 5 )

        save_button = tk.Button ( self, text = "Save", font = TIMES, fg = MYCOLORS[0],
            bg = MYCOLORS[1], command = lambda : self.controller.show_frame ( Startpage ))
        save_button.bind ("<Button -1>", self.decrypt_text)
        save_button.grid ( column = 0, row = 6, padx = 10, pady = 10, columnspan = 2, sticky= "s")

        info_text = tk.Label ( self, text = "Don't loose your Encrytion digit", font = TIMES_I )
        info_text.grid ( column = 0, row = 7, padx = 10, pady = 10, columnspan = 2, sticky = 's' )

        

        self.interface = Interface ( self )
        

    def decrypt_text ( self, event ):
        """
            This handles the encryption of the text collected by the get_text
        """

        text = self.interface.message()
        filename = file_name.get()
        filename += ".txt"
        encryptlevel = encryption_level.get()
        translated = ''

       
        for word in text.strip():
            for char in word:
                if char.isalpha ():
                        
                    level = ord ( char )
                    level -= encryptlevel

                    if char.isupper():
                            
                        if level > ord ('Z'):
                            level -= MAX_VALUE
                        elif level < ord ('A'):
                            level += MAX_VALUE
                                

                    elif char.islower ():

                        if level > ord ('z'):
                            level -= MAX_VALUE
                        elif level < ord ('a'):
                            level += MAX_VALUE
                        
                            
                    translated += chr ( level )
                        
                else:
                    translated += char

                try:    
                    with open ( filename, 'w') as f:
                        f.write ( translated )
                        
                except FileNotFoundError:
                    print ( "No such file or directory: %s" % filename )




class Bruteforce (tk.Frame ):
    """
        This class will brute force 26 different formats of the text
    """

    def __init__ ( self, parent, controller ):
        tk.Frame.__init__ ( self, parent )
        self.controller = controller
        self.parent = parent 


        self.layout ()


    def layout ( self ):
        """
            This method only creates the title of each of the class in this case will be 'ENCRYPT'
        """

        frame = tk.Frame ( self )
        frame.grid ( column = 0, row = 1 )
        

        title = tk.Label ( frame, text = "Brute   ", font = H_TIMES, fg = MYCOLORS[0] )
        title.grid ( column = 0, row = 2, padx = 5, pady = 5 )

        

        save_button = tk.Button ( self, text = "Save", font = TIMES, fg = MYCOLORS[0],
            bg = MYCOLORS[1], command = lambda : self.controller.show_frame ( Startpage ))
        save_button.bind ("<Button -1>", self.brute_text)
        save_button.grid ( column = 0, row = 6, padx = 10, pady = 10, columnspan = 2, sticky= "s")




        msg = "Encryption digit is not needed here "
        info_text = tk.Label ( self, text = msg, font = TIMES_I )
        info_text.grid ( column = 0, row = 7, padx = 10, pady = 10, columnspan = 2, sticky = 's' )
        

        self.interface = Interface ( self )



    def brute_text ( self, event ):
        """
            This handles the encryption of the text collected by the get_text
        """

        text = self.interface.message()
        filename = file_name.get()
        filename += ".txt"
        translated = ''

        file = open ( filename, 'w')

        for counter in range (1, MAX_VALUE + 1 ):
            for word in text.strip():
                for char in word:
                    if char.isalpha ():
                        
                        level = ord ( char )
                        level += counter

                        if char.isupper():
                            
                            if level > ord ('Z'):
                                level -= MAX_VALUE
                            
                            elif level < ord ('A'):
                                level += MAX_VALUE
                                

                        elif char.islower ():

                            if level > ord ('z'):
                                level -= MAX_VALUE

                            elif level < ord ('a'):
                                level += MAX_VALUE

                            
                        translated += chr ( level )
                            
                    else:
                        translated += char
            file.write ( "( %s )\n%s\n"%(counter, translated ))
            translated = ""
        file.close()
    


        

cipher = CipherHub ()
cipher.mainloop()
