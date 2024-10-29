# PostgreSQL

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.postgresql.org/)
- [Documentação](https://www.postgresql.org/docs/current/index.html)

## Instalação

### Debian

- Pacote servidor: [postgresql](https://packages.debian.org/stable/postgresql)
- Pacote cliente: [postgresql-client](https://packages.debian.org/stable/postgresql-client)

### Docker

Imagem: [postgres](https://hub.docker.com/_/postgres/)

## Config

### Databases

Lista banco de dados:

```sql
\l
```

Cria/Remove banco de dados:

```sql
CREATE DATABASE "database";
CREATE DATABASE "database" OWNER "role";
DROP DATABASE "database" WITH (FORCE);
```

Lista schemas:

```sql
\dn
```

Cria/Remove schema:

```sql
CREATE SCHEMA "schema";
DROP SCHEMA "schema" CASCADE;
```

### Usuários

Lista roles:

```sql
\dg
```

Cria/Exclui role:

```sql
CREATE ROLE "role";
DROP ROLE "role";
```

Cria/Remove usuário:

```sql
CREATE USER "user@domain" WITH PASSWORD '12345';
DROP USER "user@domain";
```

Altera senha do usuário:

```sql
ALTER USER "user@domain" WITH PASSWORD '54321';
```

Lista roles dos usuários:

```sql
\drg
```

Atribui/Remove role ao usuário:

```sql
GRANT "role" TO "user@domain";
REVOKE "role" FROM "user@domain";
```

Lista acesso as bases de dados:

```sql
-- Bases que cada usuário consegue conectar
SELECT
  u.usename,
  (
    SELECT string_agg(d.datname, ',' ORDER BY d.datname)
    FROM pg_database AS d
    WHERE has_database_privilege(u.usename, d.datname, 'CONNECT')
  ) AS databases
FROM pg_user AS u
ORDER BY u.usename;

-- Usuários que conseguem conectar em cada base
SELECT
  d.datname AS database_name,
  (
    SELECT string_agg(u.usename, ',' ORDER BY u.usename)
    FROM pg_user AS u
    WHERE has_database_privilege(u.usename, d.datname, 'CONNECT')
  ) AS users
FROM pg_database AS d
ORDER BY d.datname;
```

Lista acesso aos schemas:

```sql
SELECT
  pg_namespace.nspname AS schema,
  a.privilege_type,
  a.is_grantable,
  e.role AS role
FROM pg_namespace
JOIN LATERAL (SELECT * FROM aclexplode(nspacl)) AS a ON true
JOIN (
  SELECT usesysid AS id, usename AS role FROM pg_user
  UNION
  SELECT oid AS id, rolname AS role FROM pg_roles
) AS e ON a.grantee = e.id;
```

Da/Remove acesso ao schema:

```sql
GRANT USAGE ON SCHEMA "schema" TO "role";
REVOKE USAGE ON SCHEMA "schema" FROM "role";
```

Lista acesso as tabelas:

```sql
SELECT * FROM information_schema.role_table_grants;

SELECT
  grantee AS role,
  table_catalog AS database,
  table_schema AS schema,
  table_name AS table,
  string_agg(privilege_type, ', ' ORDER BY privilege_type) AS privileges
FROM information_schema.role_table_grants
WHERE grantee != 'postgres' AND grantee != 'PUBLIC'
GROUP BY grantee, table_catalog, table_schema, table_name;
```

Da/Remove acesso à tabela:

```sql
GRANT SELECT ON TABLE "schema"."table" TO "role";
REVOKE SELECT ON TABLE "schema"."table" FROM "role";
```

## Health Check

[Documentação](https://www.postgresql.org/docs/current/app-pg-isready.html)

## Exemplos

### docker-compose

```yaml
services:
  app:
    image: app-image:latest
    command: sleep infinity
    environment:
      PGHOST: "pg"
      PGPORT: "5432"
      PGUSER: "username"
      PGPASSWORD: "password"
      PGDATABASE: "database"
      DATABASE_URL: "postgresql://username:password@pg:5432/database"
    depends_on:
      pg:
        condition: service_healthy
  pg:
    image: postgres:17.0
    restart: unless-stopped
    environment:
      POSTGRES_USER: "username"
      POSTGRES_PASSWORD: "password"
      POSTGRES_DB: "database"
    volumes:
      - pg-data:/var/lib/postgresql/data
    expose:
      - 5432
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "username", "-d", "database"]
      interval: 15s
      timeout: 5s
      retries: 4
  pgadmin:
    image: dpage/pgadmin4:8.12
    restart: unless-stopped
    environment:
      PGADMIN_DEFAULT_EMAIL: "user@test.com"
      PGADMIN_DEFAULT_PASSWORD: "password"
      PGADMIN_LISTEN_PORT: "5050"
    ports:
      - 5050:5050
    volumes:
      - ./pgadmin-servers.json:/pgadmin4/servers.json:ro
      - pgadmin-data:/var/lib/pgadmin
    depends_on:
      pg:
        condition: service_started
volumes:
  pg-data:
  pgadmin-data:
```

`pgadmin-servers.json`:

```json
{
  "Servers": {
    "1": {
      "Name": "Database",
      "Group": "Servers",
      "Host": "pg",
      "Port": 5432,
      "SSLMode": "prefer",
      "Username": "username",
      "MaintenanceDB": "postgres"
    }
  }
}
```

#### Subir diversos bancos

`/docker-entrypoint-initdb.d/databases.sql`:

```sql
CREATE USER "user" WITH PASSWORD 'password';
CREATE DATABASE "database" OWNER "user";
```

### GitHub Actions

```yaml
jobs:
  job-name:
    runs-on: ubuntu-latest
    env:
      DATABASE_URL: "postgresql://username:password@127.0.0.1:5432/database"
    services:
      pg:
        image: postgres:17.0
        env:
          POSTGRES_USER: "username"
          POSTGRES_PASSWORD: "password"
          POSTGRES_DB: "database"
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U username -d database"
          --health-interval 15s
          --health-timeout 5s
          --health-retries 4
```
