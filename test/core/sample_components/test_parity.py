# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import Parity
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_parity():
    component = Parity()
    results = component.run(value=1)
    assert results == {"odd": 1}
    results = component.run(value=2)
    assert results == {"even": 2}
