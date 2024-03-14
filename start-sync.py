#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  start-sync.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 14.03.2024, 13:00:33
  
  Purpose: MikroTik routers address table sync.
"""

import sys
from mt_tables_sync.main import MtTablesSync

if __name__ == "__main__":
    obj = MtTablesSync()
    sys.exit(0)

# #[EOF]#######################################################################
