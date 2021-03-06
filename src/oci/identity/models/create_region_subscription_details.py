# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRegionSubscriptionDetails(object):
    """
    CreateRegionSubscriptionDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRegionSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_key:
            The value to assign to the region_key property of this CreateRegionSubscriptionDetails.
        :type region_key: str

        """
        self.swagger_types = {
            'region_key': 'str'
        }

        self.attribute_map = {
            'region_key': 'regionKey'
        }

        self._region_key = None

    @property
    def region_key(self):
        """
        **[Required]** Gets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`
        - `LHR`
        - `YYZ`
        - `NRT`
        - `ICN`

        Example: `PHX`


        :return: The region_key of this CreateRegionSubscriptionDetails.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        """
        Sets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`
        - `LHR`
        - `YYZ`
        - `NRT`
        - `ICN`

        Example: `PHX`


        :param region_key: The region_key of this CreateRegionSubscriptionDetails.
        :type: str
        """
        self._region_key = region_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
