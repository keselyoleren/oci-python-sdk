# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class VirtualCircuitBandwidthShape(object):

    def __init__(self):

        self.swagger_types = {
            'bandwidth_in_mbps': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'bandwidth_in_mbps': 'bandwidthInMbps',
            'name': 'name'
        }

        self._bandwidth_in_mbps = None
        self._name = None

    @property
    def bandwidth_in_mbps(self):
        """
        Gets the bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        The bandwidth in Mbps.

        Example: `10000`


        :return: The bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        :rtype: int
        """
        return self._bandwidth_in_mbps

    @bandwidth_in_mbps.setter
    def bandwidth_in_mbps(self, bandwidth_in_mbps):
        """
        Sets the bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        The bandwidth in Mbps.

        Example: `10000`


        :param bandwidth_in_mbps: The bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        :type: int
        """
        self._bandwidth_in_mbps = bandwidth_in_mbps

    @property
    def name(self):
        """
        Gets the name of this VirtualCircuitBandwidthShape.
        The name of the bandwidth shape.

        Example: `10 Gbps`


        :return: The name of this VirtualCircuitBandwidthShape.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VirtualCircuitBandwidthShape.
        The name of the bandwidth shape.

        Example: `10 Gbps`


        :param name: The name of this VirtualCircuitBandwidthShape.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other