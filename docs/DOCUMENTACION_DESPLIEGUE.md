# Documentación de Despliegue - Medical System

## 1. Descripción del proyecto

Medical System es una aplicación web para la gestión médica desplegada en un servidor VPS utilizando Docker, Traefik y PostgreSQL.

La arquitectura está basada en contenedores independientes comunicados mediante una red Docker.


---

# 2. Arquitectura utilizada

Componentes:

- Frontend
- Backend API REST
- Base de datos PostgreSQL
- PgAdmin
- Traefik Reverse Proxy
- Portainer
- Docker Swarm
- GitHub Actions


Flujo:

Usuario
↓
Traefik HTTPS
↓
Frontend / Backend / Portainer / PgAdmin
↓
PostgreSQL


---

# 3. Servicios publicados


## Aplicación Web

https://medicalsystem.byronrm.com


## Backend API

https://backmedicalsystem.byronrm.com


## Administrador Base de Datos

https://pgmedicalsystem.byronrm.com


## Portainer

https://portainermedicalsystem.byronrm.com



---

# 4. Contenedores desplegados


- medical-system_frontend
- medical-system_backend
- medical-system_postgres
- medical-system_pgadmin
- medical-system_portainer
- medical-system_traefik



---

# 5. Tecnologías utilizadas


Frontend:
- HTML
- CSS
- JavaScript
- Nginx


Backend:
- Python
- Flask
- JWT


Base de datos:
- PostgreSQL


Infraestructura:
- Docker
- Docker Swarm
- Traefik
- Portainer


Control de versiones:
- GitHub
- GitHub Actions
- GitHub Container Registry



---

# 6. Seguridad


Implementaciones:

- HTTPS mediante certificados Let's Encrypt.
- Autenticación JWT.
- Roles de usuario.
- Red privada Docker.
- Separación de servicios mediante contenedores.



---

# 7. CI/CD


GitHub Actions realiza:

1. Descarga del código.
2. Construcción de imágenes Docker.
3. Publicación en GitHub Container Registry.
4. Validación automática del proyecto.



---

# 8. Comandos principales


Ver servicios:

docker service ls


Ver contenedores:

docker ps


Desplegar stack:

docker stack deploy -c docker-compose.yml medical-system


Escalar servicio:

docker service scale nombre_servicio=0

docker service scale nombre_servicio=1



---

# 9. Administración


Portainer permite:

- Ver contenedores.
- Administrar servicios.
- Detener servicios.
- Escalar réplicas.
- Revisar logs.


Ejemplo:

Backend activo:

1 réplica


Dar de baja:

0 réplicas


Activar:

1 réplica
