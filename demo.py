# -*- coding: utf-8 -*-
from ladon.ladonizer import ladonize

class Calculator(object):
    u"""
    数学计算函数服务,提供几个函数例子
    """
    @ladonize(int,int,rtype=int)
    def add(self,a,b):
        """
        求两个整数的和
        @param a: 参数一 值a
        @param b: 参数二 值b
        @rtype: 返回 执行结果
        """
        return a+b
    
    @ladonize(long,long,rtype=long)
    def long_add(self,a,b):
        """
        求两个长整型的和
        @param a: 参数一 值a
        @param b: 参数二 值b
        @rtype: 返回 执行结果
        """
        return a+b
    
    @ladonize(int,int,rtype=str)
    def join(self,a,b):
        """
        将两个数合并显示
        @param a: 参数一 值a
        @param b: 参数二 值b
        @rtype: 返回 执行结果
        """
        return '%s%s'%(a,b)