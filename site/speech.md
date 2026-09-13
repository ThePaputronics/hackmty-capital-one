# F.R.E.D — Pitch de cinco minutos

Un opener de cinco segundos y cinco diapositivas de pitch más referencias. Tiempo total: **5:00**, incluyendo transiciones y pausas.

## Opener · 0:00–0:05

Pulsa → y deja que la transformación presente F.R.E.D. Al terminar, queda en pantalla hasta que pulses → otra vez. Dos pulsaciones rápidas durante la animación permiten saltarla.

## Misión y visión · El problema · 0:05–0:35

F.R.E.D nace de una falla concreta: millones pueden enviar dinero a una CLABE sin indicios de alguna señal de riesgo ni una última advertencia. Esa es la razón para empezar un movimiento de Open Banking en México, con APIs y reglas abiertas, datos protegidos y una experiencia más ágil para todos. Queremos que esta primera capa de confianza abra el camino para que las personas tengan más libertad y claridad sobre sus datos bancarios.

## La propuesta · Banxico como socio · 0:35–1:05

La propuesta concreta para Banxico es patrocinar el desarrollo y financiar la infraestructura necesaria para una operación nacional. F.R.E.D opera con un objetivo de cero profit: la inversión se convierte en desarrollo, infraestructura y capacidad de protección para millones de mexicanos. El presupuesto y el mecanismo de adquisición quedan por definir con Banxico.

## 01. F.R.E.D · La escala del problema · 1:05–1:35

En agosto de 2026, Banxico registró setecientos noventa y siete punto nueve millones de operaciones SPEI y 29.93 billones de pesos operados. CONDUSEF reportó 35,762 reclamaciones por posible fraude entre enero y mayo. Esa es la escala de confianza que queremos proteger. F.R.E.D propone analizar continuamente la actividad de SPEI, detectar patrones sospechosos por CLABE y poner esa información al alcance de los bancos. Son cifras de actividad del sistema, no de víctimas ni de usuarios ya protegidos por nosotros.

## 02. Lo que ya medimos · 1:35–2:20

Ya repetimos el benchmark del motor: seiscientas quince transferencias evaluadas, seis de seis intentos de fraude por manipulación interceptados y cero falsas alertas en las ciento ochenta operaciones de consumidores y cuatrocientas veintiséis de comercios de la muestra. Los escenarios APP interceptados sumaban ciento cuarenta y seis mil ochocientos pesos de exposición. Son transacciones sintéticas: no son pérdidas reales evitadas. Tenemos API, simulador, persistencia y evaluación reproducible. Esto prueba un mecanismo y nos da una base concreta para un piloto; no demuestra todavía precisión ni capacidad a escala nacional.

## 03. High level · Protección continua · 2:20–3:05

F.R.E.D es una API as a Service respaldada por procesamiento continuo. El worker recibe transacciones SPEI, relaciona actividad por CLABE y actualiza la base de riesgo. La API sirve esas señales ya calculadas al banco. La solicitud del cliente no dispara el análisis: el motor ya está observando el flujo. Una concentración de pagadores hacia un mismo destino es una señal, no una acusación; buscamos corroboración para no perjudicar a comercios legítimos. Proponemos a Banxico como operador central, con API y reglas abiertas y datos protegidos. La integración nacional todavía está por acordar.

## Respuestas técnicas para preguntas

- **¿Ya corre en AWS?** No. Hay una base portable y una arquitectura propuesta con ECR, ECS/Fargate, ALB y RDS. La infraestructura se tiene que provisionar y validar.
- **¿Basta con replicar el worker?** No. Hace falta asignación de trabajo, particionado, idempotencia, control de concurrencia y estado compartido. El simulador actual no es un consumidor distribuido listo para replicar.
- **¿Cómo se escala PostgreSQL?** El escalado de tareas no resuelve por sí solo escrituras, consultas ni conexiones. Deben diseñarse agregaciones por CLABE, límites y pruebas de capacidad.
- **¿El benchmark prueba impacto real?** No. Es una muestra sintética reproducible; $146,800 es exposición simulada en escenarios interceptados, no dinero realmente recuperado.
- **¿Financiamiento?** Por definir; el foco del piloto es impacto público medible.
