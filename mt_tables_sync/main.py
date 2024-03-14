# -*- coding: utf-8 -*-
"""
  main.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 14.03.2024, 13:03:47
  
  Purpose: main class
"""

from jsktoolbox.libs.base_data import BData

import mt_tables_sync._version


class MtTablesSync(BData):
    """MtTablesSync main class."""

    def __init__(self) -> None:
        """Constructor."""
        super(MtTablesSync, self).__init__()

    # class properties
    @property
    def version(self) -> str:
        return mt_tables_sync._version.__version__


# #[EOF]#######################################################################
