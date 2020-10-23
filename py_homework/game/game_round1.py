#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 17:14
# @Author  : zyw
# @File    : game_round1.py

"""
回合制游戏
"""

# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
#     if my_final_hp > enemy_final_hp:
#         print("我赢了")
#     elif my_final_hp < enemy_final_hp:
#         print("我输了")
#     else:
#         print("平局")
#
    # 三目运算，等同于if-else，语法更简洁
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")

fight()


