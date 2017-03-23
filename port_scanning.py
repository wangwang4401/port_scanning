# -*- coding: utf-8 -*-
"""
Module Description:
Date: 2017/3/22
Author:Wang pj
"""
import socket
socket.setdefaulttimeout(0.1)


def socket_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print ip, u':', port, u'端口开放'
        s.close()
    except:
        print u'端口扫描异常'


def get_ip_list(list):
    ip_list = []
    if list[0] is -1:
        one_list = []
        for i in range(0, 256):
            one_list.append(i)
    else:
        one_list = [list[0]]

    if list[1] is -1:
        two_list = []
        for i in range(0, 256):
            two_list.append(i)
    else:
        two_list = [list[1]]

    if list[2] is -1:
        three_list = []
        for i in range(0, 256):
            three_list.append(i)
    else:
        three_list = [list[2]]

    if list[3] is -1:
        four_list = []
        for i in range(0, 256):
            four_list.append(i)
    else:
        four_list = [list[3]]

    for _one in one_list:
        for _two in two_list:
            for _three in three_list:
                for _four in four_list:
                    ip_list.append(str(_one) + '.' + str(_two) + '.' + str(_three) + '.' + str(_four))

    return ip_list


if __name__ == "__main__":
    ip_list = get_ip_list([140, 205, 94, 189])
    port_list = [80, 88, 1, 2]
    print ip_list
    for ip in ip_list:
        for port in port_list:
            socket_port(ip, port)
