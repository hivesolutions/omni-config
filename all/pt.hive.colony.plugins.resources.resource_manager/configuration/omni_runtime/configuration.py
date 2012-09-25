#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Omni ERP
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Omni ERP.
#
# Hive Omni ERP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Omni ERP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Omni ERP. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2010-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

configuration = {
    "entity_manager" : {
        "arguments" : {
            "id" : "pt.hive.omni.database",
            "engine" : "sqlite",
            "options" : {
                "ensure_integrity" : False
            },
            "connection_parameters" : {
                "autocommit" : False
            }
        },
        "parameters" : {
            "default_database_prefix" : "base_runtime_"
        }
    },
    "authentication" : {
        "base_authentication" : {
            "authentication_handler" : "python",
            "arguments" : {
                "file_path" : "%configuration:pt.hive.colony.plugins.authentication.python%/authentication.py"
            }
        }
    },
    "signature" : {
        "sign_locally" : True,
        "encryption_key_name" : "colony_default",
        "encryption_base_url" : "https://localhost/encryption/",
        "encryption_algorithm_name" : "sha1"
    },
    "email" : {
        "sender_email" : "no-reply@frontdoorhq.com",
        "sender_name" : "Frontdoor",
        "smtp" : {
            "hostname" : "localhost",
            "port" : 25,
            "username" : None,
            "password" : None,
            "tls" : False
        }
    },
    "paths" : {
        "site" : "http://frontdoorhq.com/",
        "base_domain" : "https://%s.frontdoorhq.com/",
        "base" : "https://app.frontdoorhq.com/",
        "adm" : "https://app.frontdoorhq.com/adm/",
        "crm" : "https://app.frontdoorhq.com/crm/",
        "ivm" : "https://app.frontdoorhq.com/ivm/",
        "pos" : "https://app.frontdoorhq.com/pos/",
        "pum" : "https://app.frontdoorhq.com/pum/",
        "sam" : "https://app.frontdoorhq.com/sam/",
        "srm" : "https://app.frontdoorhq.com/srm/"
    }
}
