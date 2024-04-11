# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=empty-docstring,no-value-for-parameter,no-member,no-name-in-module

"""
The OpenTelemetry ``loguru`` integration automatically injects tracing context into log statements.

The integration registers a custom log record factory with the library loguru module that automatically inject
tracing context into log record objects.

The following keys are injected into log record objects by the factory:

- ``otelSpanID``
- ``otelTraceID``
- ``otelServiceName``
- ``otelTraceSampled``

The integration uses the following loguru format by default:

API
-----

.. code-block:: python

    from opentelemetry.instrumentation.loguru import LoguruInstrumentor

    LoguruInstrumentor().instrument()

"""

from typing import Collection

from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.loguru.package import _instruments


class LoguruInstrumentor(BaseInstrumentor):
    """An instrumentor for stdlib loguru module.

    This instrumentor injects tracing context into loguru records and optionally sets the global logging format to the following:

    Args:
        tracer_provider: Tracer provider instance that can be used to fetch a tracer.

    See `BaseInstrumentor`
    """

    def instrumentation_dependencies(self) -> Collection[str]:
        return _instruments

    def _instrument(self, **kwargs):
        """Instrument the library"""

    def _uninstrument(self, **kwargs):
        """Uninstrument the library"""
