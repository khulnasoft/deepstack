# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import Subtract
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_subtract():
    component = Subtract()
    results = component.run(first_value=10, second_value=7)
    assert results == {"difference": 3}
