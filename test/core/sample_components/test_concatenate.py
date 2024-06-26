# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import Concatenate
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_input_lists():
    component = Concatenate()
    res = component.run(first=["This"], second=["That"])
    assert res == {"value": ["This", "That"]}


def test_input_strings():
    component = Concatenate()
    res = component.run(first="This", second="That")
    assert res == {"value": ["This", "That"]}


def test_input_first_list_second_string():
    component = Concatenate()
    res = component.run(first=["This"], second="That")
    assert res == {"value": ["This", "That"]}


def test_input_first_string_second_list():
    component = Concatenate()
    res = component.run(first="This", second=["That"])
    assert res == {"value": ["This", "That"]}
