# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from deepstack.testing.sample_components import Threshold
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_threshold():
    component = Threshold()

    results = component.run(value=5, threshold=10)
    assert results == {"below": 5}

    results = component.run(value=15, threshold=10)
    assert results == {"above": 15}
