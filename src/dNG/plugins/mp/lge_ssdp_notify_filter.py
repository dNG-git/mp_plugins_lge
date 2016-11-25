# -*- coding: utf-8 -*-
##j## BOF

"""
MediaProvider
A device centric multimedia solution
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?mp;plugins_lge

The following license agreement remains valid unless any additions or
changes are being made by direct Netware Group in a written form.

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(mpPluginsLgeVersion)#
#echo(__FILEPATH__)#
"""

from dNG.plugins.hook import Hook
from dNG.runtime.value_exception import ValueException

def filter_headers(params, last_return = None):
#
	"""
Called for "dNG.pas.upnp.SsdpRequest.filterHeaders"

:param params: Parameter specified
:param last_return: The return value from the last hook called.

:return: (mixed) Return value
:since:  v0.2.00
	"""

	_return = last_return

	if ("headers" not in params): raise ValueException("Missing required argument")
	elif ("HOST" in params['headers']
	      and "LOCATION" not in params['headers']
	     ):
	#
		if (_return is None): _return = params['headers'].copy()
		_return['LOCATION'] = "ssdp://{0}/".format(params['headers']['HOST'])
	#

	return _return
#

def register_plugin():
#
	"""
Register plugin hooks.

:since: v0.2.00
	"""

	Hook.register("dNG.pas.upnp.SsdpRequest.filterHeaders", filter_headers)
#

def unregister_plugin():
#
	"""
Unregister plugin hooks.

:since: v0.2.00
	"""

	Hook.unregister("dNG.pas.upnp.SsdpRequest.filterHeaders", filter_headers)
#

##j## EOF