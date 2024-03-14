# -*- coding: utf-8 -*-
"""
  test_mt_tables_sync.py
  Author : Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 14.03.2024, 13:11:42
  
  Purpose: Tests for main class
"""

from unittest import TestCase

from mt_tables_sync.main import MtTablesSync


class TestForMtTablesSync(TestCase):
    """MtTablesSync class tests unit."""

    def setUp(self) -> None:
        """Set up tests."""
        self.obj = MtTablesSync()

    def test_01_create_object(self) -> None:
        self.assertIsInstance(self.obj, MtTablesSync)

    def test_02_get_version(self) -> None:
        self.assertTrue(hasattr(self.obj, "version"))
        self.assertIsInstance(self.obj.version, str)
        self.assertTrue(len(self.obj.version) > 0, "version string is not set")


# #[EOF]#######################################################################
