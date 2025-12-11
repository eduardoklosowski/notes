# SQLAlchemy

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.sqlalchemy.org/)

## Conexão

```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, echo_pool='debug')

with engine.connect() as conn:
    result = conn.execute(text('SELECT 1'))
    print(result.all())
    conn.commit()
```

Conexão com configuração dinâmica:

```python
from sqlalchemy import Dialect, Pool, event

# args
@event.listens_for(engine, 'do_connect')
def receive_do_connect(dialect: Dialect, conn_rec: Pool, cargs: list, cparams: dict) -> None:
    cargs[0] = 'db.sqlite3'

# kwargs
@event.listens_for(engine, 'do_connect')
def receive_do_connect(dialect: Dialect, conn_rec: Pool, cargs: list, cparams: dict) -> None:
    cargs.clear()
    cparams['database'] = 'db.sqlite3'

# Conexão manual
@event.listens_for(engine, 'do_connect')
def receive_do_connect(dialect: Dialect, conn_rec: Pool, cargs: list, cparams: dict) -> None:
    return dialect.connect('db.sqlite3')
```

### ORM

```python
# Manual
from sqlalchemy.orm import Session

with Session(engine) as session:
    result = session.execute(text('SELECT 1'))
    print(result.all())
    session.commit()

# Factory
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)

with Session() as session:
    result = session.execute(text('SELECT 1'))
    print(result.all())
    session.commit()
```
