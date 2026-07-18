# 🏥 MEDICAL SYSTEM
## Proyecto Final - DevOps

---

# Información General

**Proyecto:** Medical System

**Materia:** DevOps

**Institución:**
Instituto Superior Tecnológico Yavirac

**Docente:**
Ing. Byron Moreno

**Integrantes**

- Yajanuha Grefa
- Jessica Cunalata

---

# Descripción

Medical System es una aplicación web desarrollada para la administración de un consultorio médico.

El sistema permite administrar:

- Usuarios
- Pacientes
- Doctores
- Citas Médicas

Toda la solución fue desplegada sobre un VPS utilizando Docker, Docker Swarm, Traefik y Portainer.

---

# Objetivos

El objetivo del proyecto fue implementar una arquitectura moderna basada en contenedores, permitiendo:

- Virtualización de servicios.
- Publicación mediante HTTPS.
- Administración remota.
- Escalabilidad.
- Automatización mediante GitHub Actions.

---

# Arquitectura del Proyecto

```
                     INTERNET
                         │
                         ▼
                 Traefik Reverse Proxy
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼

 Frontend          Backend API       Portainer

 HTML/CSS/JS          Flask

                         │
                         ▼

                   PostgreSQL

                         │

                      PgAdmin
```

---

# Tecnologías Utilizadas

## Backend

- Python
- Flask
- SQLAlchemy
- JWT
- Flask-Bcrypt

## Frontend

- HTML5
- CSS3
- JavaScript

## Base de Datos

- PostgreSQL 16

## DevOps

- Docker
- Docker Swarm
- Docker Compose
- Portainer
- Traefik
- GitHub
- GitHub Actions

---

# Desarrollo del Proyecto

## Primera etapa

Se diseñó la arquitectura del sistema.

Se definieron los módulos:

- Usuarios
- Pacientes
- Doctores
- Citas

---

## Segunda etapa

Se desarrolló el Backend utilizando Flask.

Se implementó:

- API REST
- JWT
- Roles
- CRUD

---

## Tercera etapa

Se desarrolló el Frontend utilizando HTML, CSS y JavaScript.

Se implementaron:

- Login
- Registro
- Dashboard
- CRUD de Pacientes
- CRUD de Doctores
- CRUD de Citas

---

## Cuarta etapa

Se integró PostgreSQL.

Se crearon las tablas:

- usuarios
- pacientes
- doctores
- citas

---

## Quinta etapa

Se creó Docker para cada servicio.

Servicios:

- Backend
- Frontend
- PostgreSQL
- PgAdmin
- Portainer
- Traefik

---

## Sexta etapa

Se configuró Traefik.

Se publicaron todos los servicios mediante subdominios HTTPS.

---

## Séptima etapa

Se configuró Docker Swarm.

Se desplegó el proyecto mediante servicios.

Se verificó el escalado.

Ejemplo:

```
docker service scale medical-system_backend=0
```

y posteriormente

```
docker service scale medical-system_backend=1
```

---

## Octava etapa

Se configuró Portainer.

Desde Portainer se administran todos los servicios.

Se pueden:

- iniciar
- detener
- reiniciar
- escalar

los servicios del proyecto.

---

## Novena etapa

Se implementó GitHub Actions.

Cada Push hacia la rama Main ejecuta automáticamente:

- Checkout
- Build Backend
- Build Frontend

---

# Funcionalidades

## Usuarios

- Registro
- Login
- JWT
- Roles

---

## Pacientes

- Crear
- Editar
- Eliminar
- Listar

---

## Doctores

- Registrar
- Editar
- Eliminar
- Listar

---

## Citas

- Crear
- Consultar

---

# Seguridad

El sistema utiliza:

- JWT
- Roles
- HTTPS
- Docker Network
- Traefik

---

# Contenedores

El proyecto utiliza los siguientes servicios:

- Traefik
- Backend
- Frontend
- PostgreSQL
- PgAdmin
- Portainer

---

# Servicios Docker Swarm

Los servicios fueron desplegados mediante Docker Swarm.

Verificación:

```
docker service ls
```

Escalado:

```
docker service scale medical-system_backend=0
```

```
docker service scale medical-system_backend=1
```

---

# URLs

## Aplicación

https://medicalsystem.byronrm.com

---

## Backend

https://backmedicalsystem.byronrm.com

---

## PgAdmin

https://pgmedicalsystem.byronrm.com

---

## Portainer

https://portainermedicalsystem.byronrm.com

---

# GitHub

Repositorio

https://github.com/Yajanuha597/medical-system

---

# GitHub Actions

Cada Push ejecuta automáticamente:

- Checkout
- Build Backend
- Build Frontend

---

# Comandos Utilizados

Clonar

```bash
git clone https://github.com/Yajanuha597/medical-system.git
```

Levantar

```bash
docker compose up -d
```

Construir

```bash
docker compose up --build -d
```

Ver servicios

```bash
docker service ls
```

Escalar

```bash
docker service scale medical-system_backend=0
```

```bash
docker service scale medical-system_backend=1
```

Logs

```bash
docker service logs medical-system_backend
```

---

# Resultados

Se obtuvo un sistema completamente funcional.

El proyecto cumple con los requisitos de la asignatura:

✔ Docker

✔ Docker Swarm

✔ Traefik

✔ Portainer

✔ PostgreSQL

✔ PgAdmin

✔ Frontend

✔ Backend

✔ HTTPS

✔ GitHub

✔ GitHub Actions

✔ Docker Services

✔ CRUD completo

---

# Autores

Yajanuha Grefa

Jessica Cunalata

Instituto Superior Tecnológico Yavirac

Materia: DevOps

Docente: Ing. Byron Moreno