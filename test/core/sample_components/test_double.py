# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0

from deepstack.testing.sample_components import Double
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_double_default():
    component = Double()
    results = component.run(value=10)
    assert results == {"value": 20}
