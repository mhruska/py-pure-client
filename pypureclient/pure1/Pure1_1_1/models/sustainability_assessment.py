# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)  The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_1 import models

class SustainabilityAssessment(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'interval_start': 'int',
        'interval_end': 'int',
        'shelves': 'int',
        'chassis': 'int',
        'blades': 'int',
        'rack_units': 'int',
        'capacity_utilization': 'float',
        'array_data_reduction': 'float',
        'array_total_load': 'float',
        'power_typical_spec': 'float',
        'power_peak_spec': 'float',
        'power_average': 'float',
        'heat_typical_spec': 'float',
        'heat_peak_spec': 'float',
        'heat_average': 'float',
        'power_per_used_space': 'float',
        'power_per_usable_capacity': 'float',
        'assessment_level': 'str'
    }

    attribute_map = {
        'as_of': '_as_of',
        'interval_start': '_interval_start',
        'interval_end': '_interval_end',
        'shelves': 'shelves',
        'chassis': 'chassis',
        'blades': 'blades',
        'rack_units': 'rack_units',
        'capacity_utilization': 'capacity_utilization',
        'array_data_reduction': 'array_data_reduction',
        'array_total_load': 'array_total_load',
        'power_typical_spec': 'power_typical_spec',
        'power_peak_spec': 'power_peak_spec',
        'power_average': 'power_average',
        'heat_typical_spec': 'heat_typical_spec',
        'heat_peak_spec': 'heat_peak_spec',
        'heat_average': 'heat_average',
        'power_per_used_space': 'power_per_used_space',
        'power_per_usable_capacity': 'power_per_usable_capacity',
        'assessment_level': 'assessment_level'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        interval_start=None,  # type: int
        interval_end=None,  # type: int
        shelves=None,  # type: int
        chassis=None,  # type: int
        blades=None,  # type: int
        rack_units=None,  # type: int
        capacity_utilization=None,  # type: float
        array_data_reduction=None,  # type: float
        array_total_load=None,  # type: float
        power_typical_spec=None,  # type: float
        power_peak_spec=None,  # type: float
        power_average=None,  # type: float
        heat_typical_spec=None,  # type: float
        heat_peak_spec=None,  # type: float
        heat_average=None,  # type: float
        power_per_used_space=None,  # type: float
        power_per_usable_capacity=None,  # type: float
        assessment_level=None,  # type: str
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            interval_start (int): The timestamp of the start of the time interval.
            interval_end (int): The timestamp of the end of the time interval.
            shelves (int): The number of expansion shelves of the FlashArray appliance. It is always zero for FlashBlade appliances.
            chassis (int): The number of chassis of the appliance, always one for FlashArray appliances.
            blades (int): The number of blades of the FlashBlade appliance, always zero for FlashArray appliances.
            rack_units (int): The total number of rack units occupied by the appliance.
            capacity_utilization (float): The percentage of the used capacity. Average over the assessment window.
            array_data_reduction (float): The data reduction ratio of the appliance. Average over the assessment window.
            array_total_load (float): The load percentage. Average over the assessment window.
            power_typical_spec (float): The typical power consumption of the appliance in Watts. The value is derived from benchmark data and remains static for the model and configuration.
            power_peak_spec (float): The peak power consumption of the appliance in Watts. The value is derived from benchmark data and remains static for the model and configuration.
            power_average (float): The average of power consumption of the appliance. Average over the assessment window.
            heat_typical_spec (float): The typical heat production of the appliance in BTU/hr. The value is derived from benchmark data and remains static for the model and configuration.
            heat_peak_spec (float): The peak heat production of the appliance in BTU/hr. The value is derived from benchmark data and remains static for the model and configuration.
            heat_average (float): The average of heat production of the appliance in BTU/Hr. Average over the assessment window.
            power_per_used_space (float): The average of power consumption per TiB of used space.
            power_per_usable_capacity (float): The average of power consumption per TiB of usable capacity.
            assessment_level (str): The assessment level of an appliance. Valid values include: good - The assessment level of appliance is GOOD - all green. recommendation - There are some actions   that can be done to bring appliance to a GOOD level. action_required - The lowest level of assessment.   Some actions are required to improve the assessment level.
        """
        if as_of is not None:
            self.as_of = as_of
        if interval_start is not None:
            self.interval_start = interval_start
        if interval_end is not None:
            self.interval_end = interval_end
        if shelves is not None:
            self.shelves = shelves
        if chassis is not None:
            self.chassis = chassis
        if blades is not None:
            self.blades = blades
        if rack_units is not None:
            self.rack_units = rack_units
        if capacity_utilization is not None:
            self.capacity_utilization = capacity_utilization
        if array_data_reduction is not None:
            self.array_data_reduction = array_data_reduction
        if array_total_load is not None:
            self.array_total_load = array_total_load
        if power_typical_spec is not None:
            self.power_typical_spec = power_typical_spec
        if power_peak_spec is not None:
            self.power_peak_spec = power_peak_spec
        if power_average is not None:
            self.power_average = power_average
        if heat_typical_spec is not None:
            self.heat_typical_spec = heat_typical_spec
        if heat_peak_spec is not None:
            self.heat_peak_spec = heat_peak_spec
        if heat_average is not None:
            self.heat_average = heat_average
        if power_per_used_space is not None:
            self.power_per_used_space = power_per_used_space
        if power_per_usable_capacity is not None:
            self.power_per_usable_capacity = power_per_usable_capacity
        if assessment_level is not None:
            self.assessment_level = assessment_level

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SustainabilityAssessment`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SustainabilityAssessment`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SustainabilityAssessment`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SustainabilityAssessment`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(SustainabilityAssessment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SustainabilityAssessment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
