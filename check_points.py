# -*- coding: utf-8 -*-
def elisibility(n):
    status = None
    for x in n:
        if x == "/":
            status = False

    if status == False:
        return False
    else:
        return True