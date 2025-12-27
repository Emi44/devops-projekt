## DevOps Projekt
## Architektura i komponenty
### Usługi (Docker Compose)
- **nginx** - reverse proxy kierujące ruch HTTP do aplikacji Flask
- **app** - aplikacja Flask
- **db** - PostgreSQL 
- **migration_runner** - kontener jednorazowy przygotowujący schemat bazy
- **seed_runner** - kontener jednorazowy seedujący bazę i generujący pliki wyjściowe

### Sieci
- **front_net** - komunikacja NGINX - Flask.
- **back_net** - komunikacja Flask - PostgreSQL

### Wolumeny
- **db_data** - trwałe dane PostgreSQL
- **nginx_logs** - logi NGINX (access/error)
- **seed_output** - pliki wygenerowane przez seeder

### Kolejność uruchomienia
'db' -> 'migration_runner' -> 'seed_runner' -> 'app' -> 'nginx'

## Uruchomienie lokalne
W katalogu głównym repozytorium:
docker compose up --build
