#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from TestCase.CenterUnit import *
from PageObject.page_Configuration_object import *

class TestConfiguration(CenterUnit):

    def enterCommon(self):
        """
        点击应用配置，点击通用
        :return:
        """
        Common = Configuration(self.driver)
        Common.buttonConfiguration()
        Common.buttonCommon()

    def test_DataCatalog(self):
        """资料目录测试用例"""
        FileName = self.rdmstr('测试添加',4)
        self.enterCommon()
        DC = DataCatalog(self.driver)
        # 添加文件夹
        DC.buttonDataCatalog()
        DC.buttonAdd()
        DC.inputName(FileName)
        DC.buttonEnterAdd()
        # 搜索文件夹
        DC.inputSearchName(FileName)
        DC.buttonEnterSearch()
        assert DC.hintName() == FileName
        # 编辑文件夹
        DC.buttonEdit()
        DC.inputEditName(FileName+'EDIT')
        DC.buttonEnterEdit()
        sleep(1)
        assert DC.hintName() == FileName+'EDIT'
        # 删除文件夹
        DC.buttonDeleteBox()
        DC.buttonDelete()
        DC.buttonEnterDelete()
        # 验证是否删除成功
        assert DC.hintNoData() == '暂无数据'

    # def test_labeLManagement(self):
    #     labelName = rdmstr('测试添加',4)
    #     enterCommon()
    #     LM = LabelManagement(driver)
    #     LM.button_label_management()
    #     LM.buttonAdd() # 添加标签
    #     LM.inputName(labelName)
    #     LM.buttonEnter_label()
    #     LM.inputSearchName(labelName)    # 搜索标签
    #     LM.buttonEnterSearch()
    #     hint_msg = LM.hint_labelName()
    #     print(hint_msg)
    #     assert labelName == LM.hint_labelName()
    #     LM.buttonEdit()    # 编辑标签
    #     LM.inputName(labelName+'EDIT')
    #     LM.buttonEnter_label()
    #     assert labelName+'EDIT' == LM.hint_labelName()
    #     LM.buttonDeleteBox()  # 删除标签
    #     LM.buttonDelete()
    #     assert '暂无数据' == LM.hintNoData()

if __name__ == '__main__':
    unittest.main()