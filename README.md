# Medical System 🏥

Sistema web de gestión médica desplegado en un VPS utilizando Docker, Traefik y PostgreSQL.

## Arquitectura del sistema

La solución está formada por los siguientes servicios:

- Frontend: HTML, CSS y JavaScript servido mediante Nginx.
- Backend: API REST desarrollada con Flask.
- Base de datos: PostgreSQL.
- Administrador de base de datos: PgAdmin.
- Proxy inverso: Traefik.
- Administración de contenedores: Portainer.


## Diagrama de arquitectura
                 Usuario
                    |
                    |
              Traefik HTTPS
                    |
        ------------------------
        |          |           |
   Frontend    Backend    Portainer
    Nginx       Flask
                  |
              PostgreSQL
                  |
               PgAdmin


## Funcionalidades

### Usuarios

- Registro de usuarios.
- Inicio de sesión.
- Autenticación mediante JWT.
- Manejo de roles.


### Pacientes

- Crear pacientes.
- Listar pacientes.
- Actualizar pacientes.
- Eliminar pacientes.


### Doctores

- Registrar doctores.
- Listar doctores.


### Citas

- Crear citas médicas.
- Consultar citas.


## Servicios Docker desplegados

Contenedores:

- medical-backend
- medical-frontend
- medical-postgres
- medical-pgadmin
- portainer
- traefik


## Base de datos

Motor utilizado:

PostgreSQL.

Tablas principales:

- usuarios
- pacientes
- doctores
- citas


## Seguridad

Implementado:

- JWT para autenticación.
- Roles de usuario.
- Red interna Docker.
- HTTPS mediante Traefik.


## CI/CD

Se implementó GitHub Actions.

El flujo realiza:

1. Descarga del código.
2. Configuración de Docker.
3. Construcción del backend.
4. Construcción del frontend.


## Tecnologías utilizadas

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Traefik
- Portainer
- GitHub Actions
- HTML5
- CSS3
- JavaScript


## Ejecución del proyecto

Levantar servicios:

```bash
docker compose up -d
