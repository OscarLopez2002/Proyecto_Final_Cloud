
# Proyecto Final - Despliegue de Aplicación Web en Azure ☁️

## Descripción General 📄

Este proyecto demuestra cómo desplegar una aplicación web conectada a una base de datos SQL utilizando **Microsoft Azure**, una de las plataformas de computación en la nube más importantes del mundo. El objetivo fue crear una solución escalable donde una aplicación se comunique con una base de datos a través de servicios administrados, todo alojado en la nube.

A lo largo de este proyecto se implementaron recursos como:

- Azure App Service (para alojar una aplicación web en Python)
- Azure SQL Database
- Reglas de firewall para permitir conexiones seguras
- Variables de entorno para la configuración segura
- Flujo de conexión entre cliente → aplicación → base de datos

---

## ¿Qué es Azure? 🧠

**Microsoft Azure** es una plataforma de computación en la nube que permite crear, probar, implementar y administrar aplicaciones y servicios a través de sus centros de datos globales. Proporciona servicios como:

- Máquinas virtuales
- Bases de datos
- Aplicaciones web (App Service)
- Redes virtuales y balanceadores de carga
- Seguridad, monitoreo y escalabilidad automática

Azure permite pagar solo por lo que usas, es escalable y confiable.

---

## Arquitectura del Proyecto 🧱

El diagrama siguiente resume la arquitectura lógica del despliegue:

![Diagrama de arquitectura](Images/5c0ead68-7417-471d-98b6-0a77db45a1c1.png)

> Diagrama inspirado en [DevQueenPR/Proyecto-Final-Cloud](https://github.com/DevQueenPR/Proyecto-Final-Cloud)

---

## Instrucciones Detalladas 🔧
![Paso 1](Images/Screenshot_1.png)
![Paso 2](Images/Screenshot_2.png)
![Paso 3](Images/Screenshot_3.png)
![Paso 4](Images/Screenshot_4.png)
![Paso 5](Images/screencapture-portal-azure-2025-05-20-07_10_23.png)
![Paso 6](Images/screencapture-portal-azure-2025-05-20-07_11_00.png)
![Paso 7](Images/screencapture-portal-azure-2025-05-20-07_18_53.png)
![Paso 8](Images/screencapture-portal-azure-2025-05-20-07_19_26.png)
![Paso 9](Images/screencapture-portal-azure-2025-05-20-07_51_11.png)
![Paso 10](Images/screencapture-portal-azure-2025-05-20-07_51_53.png)
![Paso 11](Images/screencapture-portal-azure-2025-05-20-07_52_37.png)
![Paso 12](Images/screencapture-portal-azure-2025-05-20-08_20_13.png)
![Paso 13](Images/screencapture-portal-azure-2025-05-20-08_20_26.png)

---

## ¿Cómo Funciona la Solución? ⚙️

1. El usuario accede a la **URL pública** generada por Azure.
2. La aplicación en **Azure App Service** toma las variables de entorno y se conecta a la base de datos SQL.
3. La base de datos responde a la aplicación, que renderiza resultados al cliente.
4. Todo el tráfico es administrado por Azure, incluyendo seguridad y escalabilidad.

---

## Estimación de Costos 💰

| Recurso             | Plan         | Estimación mensual (USD) |
|---------------------|--------------|---------------------------|
| Azure App Service   | Free (F1)    | $0.00                     |
| Azure SQL Database  | Basic Tier   | ~$5.00 - $5.70            |
| Almacenamiento      | Incluido     | $0.00                     |
| Total Aproximado    |              | **$5.00 - $6.00 USD**     |

> Nota: Estos valores pueden variar según la región, uso exacto y promociones académicas.

---

## Requisitos Previos 📌

- Cuenta activa en Microsoft Azure
- Código de una aplicación en Python (Flask, FastAPI, etc.)
- Conocimientos básicos de redes y bases de datos
- Internet estable para pruebas

---

## Créditos 👏

Proyecto inspirado en la estructura de [DevQueenPR/Proyecto-Final-Cloud](https://github.com/DevQueenPR/Proyecto-Final-Cloud)

---

## Autor 💡

- [Tu Nombre Aquí]  
  Proyecto académico desarrollado como parte del curso de computación en la nube.

---

## Licencia 📜

Uso libre para fines educativos y demostrativos.
