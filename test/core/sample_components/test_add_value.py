# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import AddFixedValue
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_run():
    component = AddFixedValue()
    results = component.run(value=50, add=10)
    assert results == {"result": 60}
