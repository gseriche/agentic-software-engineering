# Guion del expositor — De Prompts a Agentes

**Evento:** DevOps Chile Workshops × Terralith Labs · 21 de octubre de 2026  
**Formato:** charla técnica con demos y ejercicio.  
**Duración sugerida:** 45–55 minutos (incluye 10–15 minutos de práctica).  
**Uso:** este texto es un guion oral, no contenido para proyectar. Ajusta el ritmo según preguntas.

## Slide 1 — De Prompts a Agentes (2 min)

**Relato:**

«Hoy quiero que dejemos de hablar de la IA únicamente como un generador de código. Cuando trabajamos en ingeniería de software, nuestro problema no es escribir cien líneas más rápido: es saber si esas líneas cumplen lo que el negocio necesita, si respetan las restricciones y si podemos mantenerlas en producción.

Vamos a usar un ejemplo deliberadamente pequeño: una API para gestionar cuentas y dominios de hosting. Lo importante no es FastAPI; es el proceso. Veremos cómo cambia el resultado cuando pasamos de un prompt libre a requisitos explícitos, herramientas conectadas mediante MCP y pruebas automáticas».

**Acción:** mostrar el recorrido Prompt → Spec → Agente → Tests. Explicar que los asistentes no sustituyen el criterio del ingeniero.

**Transición:** «Primero, ¿dónde está el riesgo?».

## Slide 2 — La IA escribe código rápido (2 min)

**Relato:**

«Hoy generar un endpoint puede tomar segundos. Eso es valioso, pero el tiempo de escritura no mide la corrección. Pensemos en un endpoint que registra dominios. Puede compilar, responder 200 y aun así permitir que dos clientes reclamen el mismo dominio.

En un sistema real, ese error afecta propiedad de recursos, soporte, facturación y confianza. La pregunta importante no es “¿el agente generó código?”, sino “¿qué evidencia tenemos de que hace lo correcto?”».

**Pregunta al público:** «¿A quién le ha pasado que una respuesta de IA se ve impecable, pero falla en un caso límite?».

**Transición:** «Vamos a provocarlo con una instrucción ambigua».

## Slide 3 — Un pedido, muchas interpretaciones (3 min)

**Relato:**

«Si digo “crea una API para gestionar dominios de hosting”, estoy dejando demasiadas decisiones implícitas. ¿El dominio puede pertenecer a dos cuentas? ¿Cómo se identifican los recursos? ¿Qué respuesta corresponde cuando un dominio ya existe? ¿Qué hacemos con una cuenta que no existe?

El modelo no conoce automáticamente las políticas del negocio. Puede elegir convenciones razonables, pero razonable no significa correcto para nuestro producto. Si no declaramos esas reglas, el agente debe asumirlas».

**Acción:** revelar las tres tarjetas progresivamente: Propiedad, Errores, Calidad.

**Pregunta al público:** «¿Qué otra regla falta?». Esperar 1–2 respuestas.

**Transición:** «Convirtamos esos supuestos en un contrato».

## Slide 4 — Del prompt a criterios verificables (3 min)

**Relato:**

«La diferencia entre una instrucción y una especificación es que la segunda permite verificar el resultado. En nuestro ejemplo, un dominio pertenece a una sola cuenta. Si intento registrarlo de nuevo, espero HTTP 409. Si la cuenta no existe, espero HTTP 404. Y cada una de esas reglas necesita un test.

Esto no significa escribir documentación infinita antes de programar. Significa explicitar las decisiones que, si el agente toma mal, generan defectos. Una buena especificación es pequeña, concreta y comprobable».

**Acción:** comparar ambos paneles. Señalar qué requisito se transforma en qué prueba.

**Transición:** «Aquí entra el enfoque que queremos mostrar con OpenSpec».

## Slide 5 — OpenSpec (3 min)

**Relato:**

«OpenSpec representa la idea de tratar la intención, los requisitos y los cambios como artefactos revisables. Primero describimos qué comportamiento queremos; luego analizamos el cambio, implementamos y validamos.

En este repositorio hemos incluido una especificación en Markdown para el dominio de hosting y una propuesta de cambio para transferir un dominio. Es importante distinguir el enfoque de la herramienta: estos archivos son material didáctico y no implican, por sí solos, que el flujo completo del CLI de OpenSpec esté instalado o automatizado».

**Acción:** abrir `openspec/specs/domain-management.md` y `openspec/changes/transfer-domain/proposal.md`. Recorrer el diagrama sin leer cada caja.

**Transición:** «Una especificación ayuda, pero el agente también necesita conocer el código real».

## Slide 6 — Arquitectura: contexto y controles (3 min)

**Relato:**

«Miremos la arquitectura como un circuito de responsabilidades. El desarrollador define el objetivo y las restricciones. El agente propone cambios. OpenSpec le da criterios, MCP le permite consultar herramientas como GitHub y el repositorio contiene el estado real del proyecto. Finalmente, pytest y CI nos ayudan a comprobar el comportamiento.

Noten algo: no estamos diciendo que un agente conectado a GitHub ya sea confiable. Estamos construyendo un sistema donde sus decisiones se pueden revisar y sus cambios se pueden probar».

**Acción:** seguir el flujo horizontal Desarrollador → Agente → Código. Después explicar la fila inferior como tres capacidades de soporte.

**Transición:** «Veamos con precisión qué aporta MCP».

## Slide 7 — MCP (3 min)

**Relato:**

«Model Context Protocol estandariza la forma en que un cliente puede descubrir e invocar herramientas ofrecidas por servidores compatibles. En nuestro caso, una conexión con GitHub puede permitir que el agente consulte archivos, historial o cambios del repositorio, sujeto a los permisos concedidos.

Esto reduce la dependencia de copiar y pegar contexto manualmente. Pero MCP no certifica que una fuente sea correcta, ni que el agente interprete bien su contenido. Por eso mantenemos permisos acotados, revisamos las acciones y verificamos el resultado con pruebas».

**Acción:** revelar Consultar, Actuar y Verificar. Recalcar que consultar no equivale a verificar.

**Transición:** «Ahora comparemos dos maneras de resolver el mismo problema».

## Slide 7 — Demo 1: solo prompt (3 min)

**Preparación:** abrir una conversación nueva con el agente y evitar mostrarle la especificación.

**Prompt sugerido:**

```text
Implementa una API para registrar dominios de clientes de hosting.
Antes de responder, explica qué endpoints propones.
```

**Relato:**

«Voy a pedirle algo que suena perfectamente razonable. Quiero que observen qué decisiones toma sin preguntarnos. No busco que falle: busco identificar qué partes de la solución no están sustentadas en requisitos».

**Acción:** pedir endpoints, revisar propiedad, duplicados y manejo de errores. No ejecutar acciones destructivas ni fusionar cambios automáticamente.

**Pregunta al público:** «¿Qué supuestos aceptarían y cuáles tendríamos que discutir con producto?».

**Transición:** «Repitamos el proceso, pero ahora con evidencia».

## Slide 8 — Demo 2: Spec + MCP + tests (6 min)

**Preparación:** abrir la especificación y tener el repositorio disponible mediante el conector MCP autorizado.

**Prompt sugerido:**

```text
Consulta el repositorio gseriche/agentic-software-engineering
y lee openspec/specs/domain-management.md.
Antes de modificar archivos, enumera los criterios de aceptación,
los endpoints existentes y los tests que los validan.
No inventes funcionalidades que no estén documentadas.
```

**Relato:**

«Esta vez no pedimos “haz algo”. Pedimos al agente que investigue el código y los requisitos, que nos devuelva una lista verificable y que separe lo que encontró de lo que está infiriendo.

Después ejecutamos las pruebas. El resultado de pytest es evidencia del comportamiento cubierto por esos tests; no demuestra que el sistema esté libre de todos los defectos».

**Comandos:**

```bash
cd demo
pip install -r requirements.txt
pytest -q
uvicorn app:app --reload
```

**Acción:** contrastar respuestas con `demo/app.py` y `demo/test_app.py`. Mostrar el estado de las pruebas.

**Transición:** «¿Cómo evitamos que esta validación dependa de la memoria del desarrollador?».

## Slide 9 — CI/CD: filtro de evidencia (2 min)

**Relato:**

«Cuando trabajamos con agentes, el pipeline importa más, no menos. Si la IA puede producir cambios más rápido, también puede producir errores más rápido. Necesitamos feedback automático y consistente.

En el repositorio tenemos un workflow con pruebas de la API y build de las diapositivas. Es un ejemplo simple de una idea más grande: todo cambio debería producir evidencia verificable antes de ser aceptado. Las pruebas no reemplazan el code review; lo complementan».

**Acción:** abrir `.github/workflows/ci.yml` y mostrar el estado real de GitHub Actions. No afirmar que está verde sin comprobarlo.

**Transición:** «Ahora vamos a llevar el enfoque a un requerimiento nuevo».

## Slide 10 — Ejercicio: transferir un dominio (10–15 min)

**Relato:**

«Hasta ahora registrábamos dominios. El nuevo requerimiento es transferir un dominio de una cuenta a otra sin duplicarlo. Parece una línea de código, pero primero debemos definir el contrato: ¿qué pasa si el dominio no existe? ¿Y si la cuenta destino no existe? ¿Se permite transferir a la misma cuenta? ¿Cómo comprobamos que el dominio ya no aparece en la cuenta anterior?

Tienen unos minutos para escribir los criterios de aceptación, proponer la implementación y agregar al menos una prueba de éxito y una de error».

**Prompt de trabajo sugerido:**

```text
Lee openspec/changes/transfer-domain/proposal.md y la API existente.
Propón criterios de aceptación para transferir un dominio entre cuentas.
Indica supuestos no resueltos antes de implementar.
Después agrega el endpoint y tests, preservando la unicidad del dominio.
```

**Criterios para comentar en conjunto:** no duplicación, pertenencia actualizada, errores previsibles y pruebas repetibles.

**Plan alternativo:** si no hay tiempo, discutir casos límite en voz alta y mostrar la propuesta del repositorio.

**Transición:** «Cerremos con tres ideas que pueden aplicar mañana».

## Slide 11 — Síntesis (2 min)

**Relato:** «La especificación reduce ambigüedad, MCP permite consultar contexto y herramientas, y las pruebas aportan evidencia. Ninguna pieza funciona como garantía aislada: la calidad surge del proceso completo y de la revisión humana».

**Acción:** recorrer las tres tarjetas y pedir a los asistentes que identifiquen cuál incorporarían primero a su equipo.

## Slide 12 — Recursos y repositorio (2 min)

**Relato:**

«Quiero que se lleven tres cosas. Primero, una especificación reduce la ambigüedad. Segundo, MCP ayuda al agente a trabajar con herramientas y contexto real, pero no elimina la necesidad de revisar. Tercero, las pruebas y el CI producen evidencia que podemos compartir con el equipo.

El código, las especificaciones, las diapositivas y el ejercicio están en este repositorio. Escaneen el QR, clónenlo y prueben una variante: cambien una regla, hagan que el test falle y después implementen la corrección. Ese ciclo es el aprendizaje que buscamos».

**Acción:** dejar el QR visible mientras los asistentes abren el repositorio. Confirmar que la URL escrita coincide con el destino del QR.

---

## Checklist de operación

1. Abrir las slides con `cd slides && npm install && npm run dev`.
2. Confirmar conexión del agente con GitHub MCP antes de iniciar.
3. Ejecutar `cd demo && pip install -r requirements.txt && pytest -q` antes del evento.
4. Tener terminal, editor, spec y workflow abiertos.
5. Usar modo presentador de Slidev para mantener este guion fuera de la proyección.
6. Evitar mostrar tokens, claves o datos privados.
7. **QR:** la imagen se obtiene de un servicio externo. Mantener visible también la URL del repositorio por si la imagen no carga o falla la conexión.
8. **Plan B:** usar el código, la especificación y los tests ya versionados si el agente no está disponible.
