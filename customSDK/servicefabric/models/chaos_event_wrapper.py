# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChaosEventWrapper(Model):
    """Wrapper object for Chaos event.

    :param chaos_event: Represents an event generated during a Chaos run.
    :type chaos_event: ~azure.servicefabric.models.ChaosEvent
    """

    _attribute_map = {
        'chaos_event': {'key': 'ChaosEvent', 'type': 'ChaosEvent'},
    }

    def __init__(self, chaos_event=None):
        self.chaos_event = chaos_event
