# Python com OpenTelemetry

<div class="page-toc">

<!-- toc -->

</div>

- [Nota sobre OpenTelemetry](../../services/opentelemetry/index.md)

## Instrumentalização Automática

```sh
.venv/bin/pip install opentelemetry-distro opentelemetry-exporter-otlp
.venv/bin/opentelemetry-bootstrap -a requirements > requirements.txt
.venv/bin/opentelemetry-bootstrap -a install

export OTEL_SERVICE_NAME="nome-aplicacao"
export OTEL_RESOURCE_ATTRIBUTES="env=local,attr=value"
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED="true"  # Necessário em versões anteriores a 1.40.0
.venv/bin/opentelemetry-instrument <comando-da-aplicacao>
```

> [!WARNING]
> Opções de recarregamento automático, como `--reload`, podem quebrar a observabilidade do OpenTelemetry.

## Instrumentalização Manual

Dependência:
```toml
[project]
dependencies = ["opentelemetry-api >=1.40,<2"]
```

Exemplo de código:
```python
from logging import INFO, basicConfig, getLogger
from random import randint

from opentelemetry import metrics
from opentelemetry import trace

basicConfig(level=INFO)  # Opcional

log = getLogger(__name__)
tracer = trace.get_tracer(__name__)
meter = metrics.get_meter('app')

event_counter = meter.create_counter(
    'event_counter',
    description='Número de eventos',
)

def get_random_value(options: metrics.CallbackOptions) -> Generator[metrics.Observation]:
    yield metrics.Observation(randint(0, 10), {'key': '1'})
    yield metrics.Observation(randint(0, 10), {'key': '2'})

random_value_metric = meter.create_observable_gauge(
    'random.value',
    description='Valor aleatório',
    callbacks=[get_random_value],
)

@tracer.start_as_current_span('minha_funcao')
def minha_funcao(param1: str, param2: str):
    trace_span = trace.get_current_span()
    trace_span.set_attributes({'param1': param1, 'param2', param2})
    log.info('Minha mensagem de log')
    result = 10
    trace_span.set_attribute('result', result)
    trace_span.set_status(trace.StatusCode.OK)
    event_counter.add(1, {'param1': param1, 'param2': param2, 'result': result})
    return result
```
