#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Omni ERP
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Omni ERP.
#
# Hive Omni ERP is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Omni ERP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Omni ERP. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

configuration = {
    "domain_regex" : r"(?P<domain>[^\:\/\?\#]+).frontdoorhq.com",
    "base_domains" : [
        "app",
        "api",
        "pos",
        "www",
        "mobile",
        "m"
    ],
    "alias" : {
        "omni_adm" : "adm",
        "omni_crm" : "crm",
        "omni_doc" : "doc",
        "omni_ivm" : "ivm",
        "omni_pos" : "pos",
        "omni_pum" : "pum",
        "omni_sam" : "sam",
        "omni_srm" : "srm",
        "omni_util" : "util"
    }
}
