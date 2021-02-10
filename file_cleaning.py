import pandas as pd
import numpy as np
import os
import getopt
import sys
global df, copy_df, changed_df_dtypes, user_input, csv_files, inputFile1, inputFile2, outputFile


def user_inputs(argv):
    """Run Command Line Arguments program : Open Command Prompt. Go to the File location.
       Type in [python file_name commands and their arguments]"""
    global inputFile1, inputFile2, outputFile
    inputFile1 = ''
    inputFile2 = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv, 'hf:o:', ['cfile1=', 'output='])
        """hf:q:o: are short arguments and ['file1=', 'file2=', 'output='] are long arguments. 
           [colon means that we have to provide directory]"""
    except getopt.GetoptError as e:
        print("1 : Some unexpected error occurred :", e)
        sys.exit(1)

    try:
        for opt, arg, in opts:
            if opt in ('-h', '--help'):
                print(">>> -f or --file1 and location of file and file name to be entered.\n"
                      ">>> -o or --output and location of file and file name to be saved with.")
                sys.exit()
            elif opt in ('-f', '--cfile1'):
                inputFile1 = arg
            elif opt in ('-o', '--output'):
                outputFile = arg
        print("Input Directory is : " + str(inputFile1) )
    except Exception as e:
        print("2 : Some unexpected error occurred :\n", e)
        sys.exit()


class File:

    def __init__(self, shape, dimensions, columns, data_types):
        global df, copy_df
        """Objects Used to see the shape, dimension, columns, data_types of a file"""
        self.shape = shape
        self.dimensions = dimensions
        self.columns = columns
        self.data_types = data_types

    def read_csv_file(self, data_frame):
        print("Shapes, dimensions, columns, dtypes of the file are also provided.")
        try:
            if data_frame is not None:
                read = input(">>> Do you want to read file or no ? (y/n) ")
                if read.casefold().__eq__("y" or 'yes'):
                    line_10 = input("Would you like to read First 10 rows of the File ? (y/n) ")
                    if line_10.casefold().__eq__("y" or "yes"):
                        print(data_frame.head(10))
                    elif line_10.casefold().__eq__("n" or "no"):
                        print(data_frame)
            elif data_frame is None:
                raise Exception('Empty File : ')
        except Exception as e:
            print("3 : Some unexpected error occurred :\n", e)
            exit()


class Clean_and_get_data(File):

    def __init__(self):
        global changed_df_dtypes
        """super() can be used with both parameters as below."""
        super().__init__(df.shape, df.ndim, df.columns, df.dtypes)
        # super(Clean_data, self).__init__(copy_df.shape, copy_df.ndim, copy_df.columns, copy_df.dtypes)

    def fill_nans(self, data_frame):  # if this function is not called use drop_nans() Function
        """whenever there will be a 0, then that means it is nan."""
        try:
            fill = int(input("Enter 1 to select '0'.\nEnter 2 to select np.nan.\n>>> : "))
            if fill == 1:
                data_frame.fillna('0', inplace=True)
            else:
                data_frame.fillna(np.nan, inplace=True)
            """df.fillna(arg1, arg2) arg1 is compulsory argument"""
        except Exception as e:
            print("Cannot Fill the missing values :\n" + str(e))

    def drop_nans(self, data_frame):  # if this function is not called use fill_nans() Function
        """we can either fill nans like we did above or we can drop/remove nans"""
        try:
            data_frame.dropna(inplace=True)
        except Exception as e:
            print("Error Cannot drop values : " + str(e))


class Write_File(Clean_and_get_data):

    def __init__(self):
        super().__init__()

    def write(self, file_to_write):
        """to_csv is a function to write file. outputFile is a variable that is defined in user_inputs function"""
        try:
            if outputFile is not None:
                file_to_write.to_csv(outputFile, index=False)  # by default index is True
            print("Cleaned File saved at %s" % outputFile)
        except Exception as e:
            print("4 : Some unexpected error occurred :\n", e)


if __name__ == '__main__':
    print(f"{199*'*'}{95*'*'}BISMILLAH{95*'*'}")
    """If we change the File and give me another csv file as input, the functions change_dtype_to_str(args).
       would change every object to string"""
    global df, csv_files
    try:
        user_inputs(sys.argv[1:])
    except Exception as e:
        print("5 : Some unexpected error occurred :\n", e)
    try:
        # df = pd.concat(map(pd.read_csv, [inputFile1, inputFile2])).convert_dtypes()
        """pd.concat is a useful function. We can read more than one file using this function. map is an in-built
           python function. map(arg1, arg2)"""
        df = pd.read_csv(inputFile1).convert_dtypes()
        command = Write_File()  # command object
        command.read_csv_file(df)
        if input("Print Data Types of your File ? (y/n) : ").casefold().__eq__('y' or 'yes'):
            print(command.data_types)
        command.fill_nans(df)  # fill_nans(df) will fill the missing values
        command.drop_nans(df)
        if input("Do you want to write cleaned filed ? (y/n) : ").casefold().__eq__('y' or 'yes'):
            command.write(df)
        """We will be using the function convert_dtypes function because it give us flexibility.
           The function automates and changes every dtype to required dtypes. It has in-built functions like
           convert_string which by default is True."""
        # """Printing File after cleaning............"""
        print("Thank you Sir. You have successfully cleansed your File.")
        print(f'{198*"*"}')
    except Exception as e:
        print("Main : Some unexpected error occurred :\n" + str(e))
        exit()

