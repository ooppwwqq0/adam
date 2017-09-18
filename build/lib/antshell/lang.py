#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################################
# _______  __    _  _______  _______  __   __  _______  ___      ___     #
#|   _   ||  |  | ||       ||       ||  | |  ||       ||   |    |   |    #
#|  |_|  ||   |_| ||_     _||  _____||  |_|  ||    ___||   |    |   |    #
#|       ||       |  |   |  | |_____ |       ||   |___ |   |    |   |    #
#|       ||  _    |  |   |  |_____  ||       ||    ___||   |___ |   |___ #
#|   _   || | |   |  |   |   _____| ||   _   ||   |___ |       ||       |#
#|__| |__||_|  |__|  |___|  |_______||__| |__||_______||_______||_______|#
#                                                                        #
##########################################################################

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
# zh or en
# help info lang set
LANG = {
    "default" :"en",
    "zh" : {
        "init" : "初始化配置文件以及数据库",
        "update" : "hosts信息升级成数据库",
        "version" : "打印版本信息并退出",
        "help" : "打印帮助信息并退出",
        "add" : "添加主机信息并登陆",
        "commod" : "主机远程执行命令",
        "edit" : "编辑主机信息",
        "delete" : "删除主机信息并退出",
        "file" : "文件名",
        "fs" : "指定分隔符，默认<,>",
        "get" : "获取文件路径",
        "put" : "指定文件路径",
        "group" : "过滤群组主机",
        "lists" : "输出主机列表并退出",
        "mode" : "列表显示列数1-5",
        "num" : "选择连接的主机编号",
        "para" : "paramiko模式",
        "search" : "模糊匹配主机信息",
        "old" : "old-sh-file模式登陆主机",
        "v" : "fast模式位置变量",
        "desc" : "AntShell 远程登录管理工具",
        "name" : "标记名",
        "user" : "用户名",
        "passwd" : "密码",
        "port" : "端口",
    },
    "en" : {
        "init" : "Initialize the configuration file and the database",
        "update" : "The hosts information is upgraded to a database",
        "version" : "show program's version number and exit",
        "help" : "show this help message and exit",
        "add" : "add host info and login",
        "commod" : "host execute command",
        "edit" : "edit host info",
        "delete" : "delete host info and exit",
        "file" : "file name",
        "fs" : "set up separator, default<,>",
        "get" : "get file_path",
        "put" : "put file_path",
        "group" : "filter group host info",
        "lists" : "list host info and exit",
        "mode" : "list shows the number of columns 1-5",
        "num" : "choose host num to login",
        "para" : "paramiko pattern",
        "search" : "fuzzy matching host info",
        "old" : "old-sh-file pattern login host",
        "v" : "fast mode position variable",
        "desc" : "AntShell Nexus Terminal",
        "name" : "tag name",
        "user" : "username",
        "passwd" : "password",
        "port" : "ports",
    }
}
