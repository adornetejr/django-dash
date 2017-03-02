from django.utils.translation import ugettext

__title__ = 'dash.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'RESTRICT_PLUGIN_ACCESS',
    'PLUGINS_MODULE_NAME',
    'LAYOUTS_MODULE_NAME',
    'ACTIVE_LAYOUT',
    'LAYOUT_CELL_UNITS',
    'DEFAULT_WORKSPACE_NAME',
    'DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME',
    'WAIT_BETWEEN_TEST_STEPS',
    'DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME',
    'DISPLAY_AUTH_LINK',
    'RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT',
    'WAIT_AT_TEST_END',
    'PLUGIN_CLIPBOARD_KEY',
    'DEBUG'
)

gettext = lambda s: s

# If set to True, plugins would be only accessible by the white-listed user(s) 
# or group(s). If set to False, all users have the same access rights to all
# plugins.
RESTRICT_PLUGIN_ACCESS = True

# If set to True, exceptions are raised when user has insufficient permissions.
RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT = True

# Name of the module in which the dash plugins are registered.
PLUGINS_MODULE_NAME = 'dash_plugins'

# Name of the module in which the dash layouts are registered.
LAYOUTS_MODULE_NAME = 'dash_layouts'

# UID of the active layout.
ACTIVE_LAYOUT = 'android'

# Allowed layout cell units.
LAYOUT_CELL_UNITS = (
    'em',
    'px',
    'pt',
    '%',
    'rem',
    'in',
    'cm',
    'mm',
    'ex',
    'pc'
)

# Name of the default dashboard workspace (no workspace).
DEFAULT_WORKSPACE_NAME = 'Default'

DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME = \
    'dash/layouts/base_placeholder_view.html'
DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME = \
    'dash/layouts/base_placeholder_edit.html'

# If set to True, the logout link is shown in the menu.
DISPLAY_AUTH_LINK = True

WAIT_BETWEEN_TEST_STEPS = 2
WAIT_AT_TEST_END = 4

# Key of the clipboard variable used in sessions to store the plugin clipboard
# data.
PLUGIN_CLIPBOARD_KEY = 'dash_plugin_clipboard'

DEBUG = False
