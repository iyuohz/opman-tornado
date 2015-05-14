# coding=utf-8
#import os, sys
import ConfigParser
config = ConfigParser.ConfigParser()

class Get_data:
    def __init__(self,ini_file):
        self.ini_file = ini_file
        config.read(ini_file)

    def Show_section(self):
        self.section = config.sections()
        return self.section

    def Show_option(self,section):
        self.option = config.options(section)
        return self.option

    def Show_option_data(self,section,option):
        self.option_data = config.get(section,option)
        return self.option_data
'''
if __name__ == "__main__":
    getdata = Get_data('./config.ini')
    print getdata.Show_option_data('db','db_host')
'''
