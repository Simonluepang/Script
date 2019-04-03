#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Public.page_base import *

class Configuration(Page):
    """应用配置菜单"""
    def buttonConfiguration(self):
        # 应用配置
        self.location('CSS','CLICK','li.el-menu-item:nth-child(9)')

    def buttonCommon(self):
        # 通用
        self.location('CSS','CLICK','li.config-menus-item:nth-child(1)')


class DataCatalog(Page):
    # 资料目录三级菜单
    def buttonDataCatalog(self):
        # 资料目录
        self.location('CSS','CLICK','ul.main-shadow > li:nth-child(1)')

    def buttonAdd(self):
        # 添加资料目录
        self.location('CSS','CLICK','button.basic-btn>i.el-icon-plus')

    def inputName(self,folderName):
        # 添加文件夹名称
        self.location('CSS','SENDKEYS',"div.el-input> input.el-input__inner[autofocus='autofocus']",folderName)

    def buttonEnterAdd(self):
        # 确认添加
        self.location('CSS','CLICK','span.icon-tips-success')

    def inputSearchName(self,folderName):
        # 搜索文件夹名称
        self.location('CSS','SENDKEYS',"input.el-input__inner[icon = 'search']",folderName)

    def buttonEnterSearch(self):
        # 确定搜索
        self.location('CSS', 'CLICK', '.el-icon-search')

    def hintName(self):
        # 验证文件夹名称
        return self.location('CSS','HINT','div.name-wrapper:nth-child(1)')

    def buttonEdit(self):
        # 编辑
        self.location('CSS','CLICK','tr.el-table__row:nth-child(1) > td:nth-child(5) > div:nth-child(1) > span:nth-child(1)')

    def inputEditName(self,folderName):
        # 修改文件夹名称
        self.location('CSS','SENDKEYS',"div.el-form-item__content[style='margin-left: 85px;']>div.el-input>input.el-input__inner",folderName)

    def buttonEnterEdit(self):
        # 确认修改
        self.location('CSS','CLICK','div.el-dialog__footer:nth-child(3) > span:nth-child(1) > button:nth-child(1)')

    def buttonDeleteBox(self):
        # 勾选删除框
        self.location('CSS','CLICK','td.el-table_1_column_1 > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)')

    def buttonDelete(self):
        # 删除
        self.location('CSS','CLICK','button.basic-btn.absol')

    def buttonEnterDelete(self):
        # 确认删除
        self.location('CSS','CLICK','.el-message-box__btns > button:nth-child(2)')

    def hintNoData(self):
        # 验证是否删除成功
        return self.location('CSS', 'HINT', '.el-table__empty-text')

class LabelManagement(Page):
    """标签管理三级菜单"""

    def buttonLabelManagement(self):
        # 标签管理
        self.location("CSS",'CLICK','ul.main-shadow > li:nth-child(4)')

    def buttonAdd(self):
        # 添加
        self.location('CSS','CLICK','button.basic-btn:nth-child(1)')

    def inputName(self,labelName):
        # 添加标签名称
        self.location('CSS','SENDKEYS','.el-form-item__content > div:nth-child(1) > input:nth-child(1)',labelName)

    def buttonEnterLabel(self):
        # 确定添加名称
        self.location('CSS','CLICK','div.el-dialog__footer:nth-child(3) > span:nth-child(1) > button:nth-child(1)')

    def hintLabelName(self):
        # 验证标签名称
        self.location('CSS','HINT','td.el-table_1_column_52 > div.cell.el-tooltip')

    def inputSearchName(self,labelName):
        # 搜索标签名称
        self.location('CSS','SENDKEYS','div.el-col:nth-child(3) > div:nth-child(1) > input:nth-child(2)',labelName)

    def buttonEnterSearch(self):
        # 确定搜索
        self.location('CSS', 'CLICK', '.el-icon-search')

    def buttonEdit(self):
        # 修改标签
        self.location('CSS','CLICK','.icon-edit_')

    def buttonDeleteBox(self):
        # 勾选删除框
        self.location('CSS','CLICK','td.el-table_1_column_6 > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)')

    def buttonDelete(self):
        # 删除标签
        self.location('CSS','CLICK','button.basic-btn:nth-child(2)')

    def hintNoData(self):
        # 验证是否删除成功
        return self.location('CSS', 'HINT', '.el-table__empty-text')

class FormManagement(Page):
    """表单管理三级菜单"""
    def buttonFormManagement(self):
        # 表单管理
        self.location('CSS','CLICK','ul.main-shadow > li:nth-child(5)')

    def buttonAdd(self):
        # 添加表单
        self.location('CSS','CLICK','button.basic-btn:nth-child(1)')

    def buttonUploadTemplateFile(self):
        # 上传表单
        self.location('CSS','CLICK','.el-button--small')

    def buttonEnterAdd(self):
        # 确定
        self.location('CSS','CLICK','div.el-dialog__footer:nth-child(3) > span:nth-child(1) > button:nth-child(1)')

    def hintFormName(self):
        # 验证表单名称
        return self.location('CSS','HINT','tr.el-table__row:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1)')

    def buttonEdit(self):
        # 编辑表单
        self.location('CSS','CLICK','span.icon-edit_')

    def inputEditName(self,formName):
        # 修改表单名称
        self.location('CSS','SENDKEYS','div.el-form-item__content:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)',formName)

    def buttonDeleteBox(self):
        # 勾选删除框
        self.location('CSS','CLICK','tr.el-table__row>td.el-table-column--selection>div.cell>label.el-checkbox>span.el-checkbox__input>span.el-checkbox__inner')

    def buttonDelete(self):
        # 删除表单
        self.location('CSS','CLICK','button.basic-btn:nth-child(2)')