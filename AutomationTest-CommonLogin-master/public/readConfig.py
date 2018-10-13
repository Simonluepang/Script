import configparser
from Setting import *

class ReadConfig():
    def __init__(self,ConfigPath):
        self.conf = configparser.ConfigParser()
        self.conf.read(ConfigPath)
        self.ConfigPath = ConfigPath

    def read_assign_section_option(self,section,option):
        '''
        获得指定section且指定option里的值
        :param section:
        :param option:
        :return:
        '''
        value = self.conf.get(section, option)
        return value


    def read_assign_sections(self):
        '''
        获得所有的section
        :return:
        '''
        sections = self.conf.sections()
        return sections

    def read_assign_section_options(self,section):
        '''
        获得指定section下所有的options
        :param section:
        :return:
        '''
        options = self.conf.options(section)
        return options

    def write_config_assign_section_option(self,section,option,value=0):
        self.conf.set(section,option,value)
        with open(self.ConfigPath, 'w') as fw:  # 循环写入
            self.conf.write(fw)

