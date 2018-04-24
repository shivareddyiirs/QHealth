# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QHealth
                                 A QGIS plugin
 This plugin provides step by step tools required to analyse health data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-04-25
        copyright            : (C) 2018 by Indian Insitute of Remote Sensing, ISRO, Dehradun, India
        email                : kotishiva@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QHealth class from file QHealth.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .QHealth import QHealth
    return QHealth(iface)