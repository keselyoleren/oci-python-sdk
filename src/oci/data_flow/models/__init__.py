# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .application import Application
from .application_parameter import ApplicationParameter
from .application_summary import ApplicationSummary
from .create_application_details import CreateApplicationDetails
from .create_run_details import CreateRunDetails
from .run import Run
from .run_log_summary import RunLogSummary
from .run_summary import RunSummary
from .update_application_details import UpdateApplicationDetails
from .update_run_details import UpdateRunDetails

# Maps type names to classes for data_flow services.
data_flow_type_mapping = {
    "Application": Application,
    "ApplicationParameter": ApplicationParameter,
    "ApplicationSummary": ApplicationSummary,
    "CreateApplicationDetails": CreateApplicationDetails,
    "CreateRunDetails": CreateRunDetails,
    "Run": Run,
    "RunLogSummary": RunLogSummary,
    "RunSummary": RunSummary,
    "UpdateApplicationDetails": UpdateApplicationDetails,
    "UpdateRunDetails": UpdateRunDetails
}
