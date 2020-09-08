#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

from .db import TSUTAYA_MEMBER
import uuid

def generate_id() -> str:
    """ generate random ID """
    return str(uuid.uuid4().hex)[0:8]

def is_adult(x_card_id : str) -> bool:
    if TSUTAYA_MEMBER[x_card_id]['age'] >= 18: 
        return True
    else:
        return False
