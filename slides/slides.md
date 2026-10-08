---
theme: default
title: De Prompts a Agentes
---

# De Prompts a Agentes
## Ingeniería de Software con IA, OpenSpec y MCP
DevOps Chile Workshops · 21 octubre 2026

---

# La IA escribe código muy rápido
## ¿Cómo aseguramos que escriba el código correcto?

---

# Un prompt ambiguo
"Crea una API para gestionar dominios de hosting"

¿Qué ocurre con la unicidad, propiedad, errores y pruebas?

---

# De prompts a especificaciones
- Requisitos explícitos
- Criterios de aceptación
- Cambios trazables
- Tests reproducibles

---

# OpenSpec
**Intent → Spec → Implementación → Validación**

---

# MCP
Conectamos agentes a repositorios y herramientas reales.

El contexto consultado debe verificarse: MCP no garantiza ausencia de alucinaciones.

---

# Demo 1: sólo prompt
¿Qué supuestos toma el agente?

---

# Demo 2: spec + MCP
- Un dominio pertenece a una sola cuenta
- Una cuenta tiene múltiples dominios
- Duplicados → HTTP 409
- Cuenta inexistente → HTTP 404

---

# Un nuevo requerimiento
Transferir un dominio entre cuentas sin duplicarlo.

---

# ¿Qué cambia?
No es magia: mejores requisitos, acceso a fuentes y pruebas.

---

# Desafío para estudiantes
Implementar la transferencia, agregar tests y documentar supuestos.

---

# Clona y participa
github.com/gseriche/agentic-software-engineering

DevOps Chile Workshops · Terralith Labs
