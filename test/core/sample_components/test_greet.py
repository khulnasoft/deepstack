# SPDX-FileCopyrightText: 2022-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
import logging

from deepstack.testing.sample_components import Greet
from deepstack.core.serialization import component_to_dict, component_from_dict


def test_greet_message(caplog):
    caplog.set_level(logging.WARNING)
    component = Greet()
    results = component.run(value=10, message="Hello, that's {value}", log_level="WARNING")
    assert results == {"value": 10}
    assert "Hello, that's 10" in caplog.text
