#!usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'yanqiong'

import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from random import Random


def _generate_uuid(RD: 'Random', prefix=''):
    return f"{prefix + '_' if prefix else ''}{uuid.UUID(int=RD.getrandbits(128)).hex}"
