# F.R.E.D — Pitch de cinco minutos

Un opener de cinco segundos y siete diapositivas. Tiempo total: **5:00**, incluyendo transiciones y pausas.

## Opener · 0:00–0:05

Pulsa → y deja que la transformación presente F.R.E.D. Al terminar, queda en pantalla hasta que pulses → otra vez. Dos pulsaciones rápidas durante la animación permiten saltarla.

## 01. F.R.E.D · La escala del problema · 0:05–0:35

En agosto de 2026, Banxico registró setecientos noventa y siete punto nueve millones de operaciones SPEI y 29.93 billones de pesos operados. CONDUSEF reportó 35,762 reclamaciones por posible fraude entre enero y mayo. Esa es la escala de confianza que queremos proteger. F.R.E.D propone analizar continuamente la actividad de SPEI, detectar patrones sospechosos por CLABE y poner esa información al alcance de los bancos. Son cifras de actividad del sistema, no de víctimas ni de usuarios ya protegidos por nosotros.

## 02. Lo que ya medimos · 0:35–1:20

Ya repetimos el benchmark del motor: seiscientas quince transferencias evaluadas, seis de seis intentos de fraude por manipulación interceptados y cero falsas alertas en las ciento ochenta operaciones de consumidores y cuatrocientas veintiséis de comercios de la muestra. Los escenarios APP interceptados sumaban ciento cuarenta y seis mil ochocientos pesos de exposición. Son transacciones sintéticas: no son pérdidas reales evitadas. Tenemos API, simulador, persistencia y evaluación reproducible. Esto prueba un mecanismo y nos da una base concreta para un piloto; no demuestra todavía precisión ni capacidad a escala nacional.

## 03. High level · Protección continua · 1:20–2:05

F.R.E.D es una API as a Service respaldada por procesamiento continuo. El worker recibe transacciones SPEI, relaciona actividad por CLABE y actualiza la base de riesgo. La API sirve esas señales ya calculadas al banco. La solicitud del cliente no dispara el análisis: el motor ya está observando el flujo. Una concentración de pagadores hacia un mismo destino es una señal, no una acusación; buscamos corroboración para no perjudicar a comercios legítimos. Proponemos a Banxico como operador central, con API y reglas abiertas y datos protegidos. La integración nacional todavía está por acordar.

## 04. High level · Valor para producto y negocio · 2:05–2:45

Para un equipo de producto, el valor se aterriza en tres resultados. Primero, reducir exposición a pérdidas: medir qué ocurre después de advertir, sin contar una alerta como dinero recuperado. Segundo, preservar pagos legítimos: una herramienta que alerta demasiado también destruye confianza y conversión. Tercero, facilitar la operación de fraude: cada señal debe traer motivos y evidencia para que un equipo pueda revisarla. El piloto medirá resultado del aviso, falsas alertas, abandono y tiempo de revisión. No estamos atribuyéndonos un ahorro que todavía no medimos.

## 05. Low level · Escalamiento propuesto en AWS · 2:45–3:45

La ruta de nube separa dos cargas. Publicamos imágenes en ECR y ejecutamos servicios ECS sobre Fargate. Para el procesamiento, proponemos repartir el flujo por CLABE entre workers y aumentar tareas según pendientes y retraso. Ese reparto necesita idempotencia, control de concurrencia y estado compartido para no duplicar análisis. Para las lecturas, un balanceador ALB distribuye solicitudes entre réplicas de API; ese servicio escala de forma independiente. RDS PostgreSQL concentra el estado. Agregar contenedores no multiplica automáticamente la capacidad de la base: necesitamos controlar conexiones, escrituras y agregaciones. ECS admite políticas de autoescalado; hay que configurarlas. Esta es una arquitectura propuesta: hoy no tenemos infraestructura AWS desplegada.

## 06. La ruta de despliegue · 3:45–4:30

La base para migrar ya existe: Dockerfiles, FastAPI, PostgreSQL, configuración por entorno y Alembic. Eso nos permite conservar las reglas del motor al cambiar el entorno de ejecución. El siguiente paso es construir y verificar las imágenes, publicarlas en ECR y definir tareas, redes, permisos y secretos para ECS. Hay dos ajustes relevantes: separar el worker productivo del simulador y ejecutar las migraciones una sola vez por despliegue, no desde cada réplica de API como hace hoy el arranque. Después validamos carga, recuperación y capacidad de la base. Buscamos una transición directa, sin prometer una migración automática que todavía no hemos probado.

## 07. Cinco minutos · Una petición concreta · 4:30–5:00

La petición es concreta: una mesa técnica con Banxico y participantes, un flujo autorizado y un piloto en sombra. Primero medimos detección, falsas alertas y frescura de las señales. Después validamos que el aviso ayude al cliente y preserve pagos legítimos. El financiamiento queda por definir. Tenemos una base técnica demostrable y una ruta de nube; ahora queremos convertirlas en impacto medido. F.R.E.D: observar continuamente para proteger el siguiente SPEI.

## Respuestas técnicas para preguntas

- **¿Ya corre en AWS?** No. Hay una base portable y una arquitectura propuesta con ECR, ECS/Fargate, ALB y RDS. La infraestructura se tiene que provisionar y validar.
- **¿Basta con replicar el worker?** No. Hace falta asignación de trabajo, particionado, idempotencia, control de concurrencia y estado compartido. El simulador actual no es un consumidor distribuido listo para replicar.
- **¿Cómo se escala PostgreSQL?** El escalado de tareas no resuelve por sí solo escrituras, consultas ni conexiones. Deben diseñarse agregaciones por CLABE, límites y pruebas de capacidad.
- **¿El benchmark prueba impacto real?** No. Es una muestra sintética reproducible; $146,800 es exposición simulada en escenarios interceptados, no dinero realmente recuperado.
- **¿Financiamiento?** Por definir; el foco del piloto es impacto público medible.
