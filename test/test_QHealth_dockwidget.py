# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'kotishiva@gmail.com'
__date__ = '2018-04-25'
__copyright__ = 'Copyright 2018, Indian Insitute of Remote Sensing, ISRO, Dehradun, India'

import unittest

from PyQt5.QtGui import QDockWidget

from QHealth_dockwidget import QHealthDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class QHealthDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = QHealthDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(QHealthDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

