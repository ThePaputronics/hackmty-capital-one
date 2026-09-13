# F.R.E.D — Fuentes, evidencia y alcance

Revisión: 12 de septiembre de 2026.

## Qué estamos proponiendo

F.R.E.D es una API as a Service respaldada por un worker que procesa continuamente transacciones SPEI. Relaciona actividad sospechosa por CLABE y actualiza su base de riesgo conforme procesa el flujo. La API sirve las señales ya calculadas; una transferencia o una lectura del banco no inicia el análisis.

La propuesta es que Banxico opere esa infraestructura, y que los bancos consuman sus señales para advertir al cliente. La actualización continua exige medir el desfase entre evento y estado disponible: no se promete desfase cero ni cobertura nacional ya desplegada.

El paquete actual se llama `Sentinel`. Se distinguen dos niveles de evidencia: el modelo operativo definido por el equipo y la implementación del checkout. El repositorio tiene un worker de simulación que ingiere eventos y llama a la evaluación síncrona, además de persistir eventos y evaluaciones. Eso no demuestra por sí mismo un worker productivo que materialice riesgo por CLABE ni una ruta de lectura de ese estado. No se inventaron endpoints ni se cambió el backend en esta revisión.

## Referencias externas

1. [FICO — Scam Signal, 2024](https://s23.q4cdn.com/175719177/files/doc_news/New-Scam-Detection-Product-from-FICO-and-Jersey-Telecom-Wins-Datos-Insights-Award-2024.pdf). Referencia competitiva de detección de estafas con telecomunicaciones y pagos. La diferenciación propuesta de F.R.E.D es una señal interoperable a escala SPEI con criterios revisables. No se realizó una comparación contra FICO ni se demuestra superioridad.
2. [Banxico — SIE CF620, transferencias SPEI por monto operado](https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CF620&locale=es), datos consultados en septiembre de 2026. Agosto de 2026 registra 797,901,706 operaciones tercero a tercero y $29,932,758,000,638 MXN. Es actividad del sistema, no víctimas ni pérdidas evitadas.
3. [CONDUSEF — Consulta y Reporta, posible fraude enero–mayo 2026](https://www.condusef.gob.mx/documentos/prensa/Consulta%20y%20Reporta.pdf), junio de 2026. Reporta 35,762 reclamaciones por posible fraude en el periodo enero–mayo de 2026. Son reclamaciones recibidas, no casos atribuidos a F.R.E.D.
3. [Ley para Regular las Instituciones de Tecnología Financiera](https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf), art. 76. Referencia de interfaces estandarizadas y distinción entre datos abiertos, agregados y transaccionales. La propuesta requiere determinar las facultades, autorizaciones y condiciones aplicables: este artículo no otorga por sí mismo permiso para integrar F.R.E.D a SPEI.
4. [Banxico — Disposiciones SPEI, Circular 14/2017](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/sistema-pagos-spei-disposicio.html). Referencia para acordar integración y operación con el administrador y participantes.

## Apertura y financiamiento

- La API actual está documentada mediante OpenAPI generado por FastAPI. OpenAPI es un formato de contrato; no equivale a un estándar institucional adoptado.
- Dirección confirmada por el equipo: API y reglas abiertas, datos protegidos y una propuesta de estándar para Banxico. Se propone una solución de Open Banking con contratos interoperables, reglas revisables, versiones y gobierno común. Compartir datos exige acceso autorizado y protección; no se propone una base pública de transacciones o acusaciones sobre cuentas.
- No se encontró una licencia open source en el repositorio. No se añadió una licencia ni se publicó el código. TODO: Verify el alcance de apertura y las condiciones jurídicas con el equipo.
- Por indicación del equipo, el financiamiento queda por definir y el pitch se centra en impacto público. No se propone un esquema de cobro ni se presenta presupuesto, precio, contratación o modelo de ingresos validado. TODO: Verify recursos y responsabilidades de financiación antes de un despliegue.
- Se eliminaron la licencia hipotética de $240,000 por banco y el cálculo anterior de mercado por venta de licencias; no corresponden a esta dirección de producto.

## TAM / SAM / SOM de cobertura

| Nivel | Definición del pitch | Estado |
| --- | --- | --- |
| TAM, alcance potencial | 797.9 millones de operaciones SPEI en agosto de 2026 | Cifra mensual de Banxico; no usuarios de F.R.E.D ni víctimas |
| SAM, alcance habilitable | Flujos conectados al worker, datos autorizados y bancos que consumen el estado por API | TODO: Verify volumen elegible con participantes |
| SOM, primer piloto | Un operador central propuesto y dos participantes por convocar | Meta de implementación, sin acuerdos ni volumen comprometido |

Estos niveles describen cobertura social y operativa, no ingresos. No se infiere una tasa de fraude a partir del número de usuarios. No se promete una puntuación por cumplir una rúbrica: monetización, demanda y adopción requieren evidencia adicional.

## Evidencia técnica revisada

| Archivo | Qué respalda |
| --- | --- |
| `apps/api/src/sentinel/risk/recipient_scorer.py` | Tres o más `payer_id` distintos financiando la misma CLABE en una ventana de 24 horas generan una señal de fan-in; considera eventos hasta `proposed_at`. |
| `apps/api/src/sentinel/risk/engine.py` | Corroboración de acceso, intención y destino; umbral 0.40 por dimensión; decisiones `allow/challenge/pause`; combinación prioritaria de llamada/pantalla compartida y destino nuevo. |
| `apps/api/src/sentinel/feature_store.py` | Historial de 90 días, ventanas de 1/24 horas, destino, beneficiario y contexto temporal calculados con `as_of`. |
| `apps/api/src/sentinel/schemas.py` y `main.py` | Contratos, entrada de contexto del banco, motivos, señales, mensajes en español, versión y persistencia. |
| `apps/generator/src/generator/server.py` y `player.py` | Worker de simulación en segundo plano: ingiere eventos y ejecuta evaluaciones; replay finito, no prueba de un servicio nacional persistente. |
| `apps/generator/src/generator/simulation.py` | Personas sintéticas, reproducción con semilla y etiquetas de verdad oculta. |
| `apps/ui/index.html` | Dashboard operativo existente, separado de la web del pitch. |

La señal de fan-in cubre los datos presentes en la base del prototipo. No equivale a visibilidad de todo SPEI ni basta por sí sola para identificar una cuenta fraudulenta. El ejemplo con tres bancos ilustra lo que permitiría una integración autorizada entre instituciones. El motor no obtiene por sí mismo llamadas, pantallas ni señales del dispositivo.

## Validación ejecutada

En un entorno temporal con Python 3.14:

```bash
PYTHONPATH=apps/api/src pytest apps/api/tests -q
PYTHONPATH=apps/generator/src pytest apps/generator/tests -q
PYTHONPATH=apps/api/src:apps/generator/src python tools/evaluate/harness.py --days 30 --seed 42 --json
```

- API: **5 pruebas aprobadas**. Generador: **2 aprobadas**.
- Benchmark: **2,940 eventos de calentamiento**, **52 pagadores**, **615 transferencias**, **6/6 ataques APP interceptados**, **3/3 ataques ATO interceptados**.
- Falsos positivos: **0%** para **180 transferencias de consumidores** y **426 de comercios** en esta muestra.
- Latencia registrada por el harness: p50 **2.19 ms**, p95 **3.64 ms**. Medición local del prototipo; no representa latencia de extremo a extremo ni rendimiento nacional.
- En esta ejecución, la comparación con suma ponderada ingenua también obtuvo 0% de falsos positivos y 100% de recall APP. No respalda una afirmación de superioridad medida de la corroboración sobre esa alternativa en esta muestra.
- Hubo avisos de deprecación de dependencias y `datetime.utcnow`; no fallos de pruebas. No se modificó código del motor.
- Resultados de la ejecución guardados en [benchmark.json](benchmark.json).

## Pendientes antes de operar a escala nacional

- TODO: Verify acuerdos y facultades para el flujo continuo, el worker y el consumo institucional de señales. No se ha anunciado respaldo de Banxico.
- TODO: Verify materialización por CLABE, contrato de lectura, tiempo procesado, deduplicación, eventos tardíos y recuperación del worker. La API debe expresar la vigencia del estado.
- TODO: Verify disponibilidad, permisos y calidad de los datos de participantes; identidad consistente de pagadores entre instituciones y minimización de información.
- TODO: Verify autenticación y autorización efectivas, aislamiento, cifrado, retención y auditoría de acceso. Las opciones de configuración no demuestran controles implantados.
- TODO: Verify preagregación y almacenamiento adecuado para señales por CLABE: el scorer actual recorre eventos de 24 horas y filtra el destino en Python.
- TODO: Verify manejo de errores: el scorer de destinatario actualmente captura excepciones y continúa sin exponerlas. No se debe convertir un fallo de evaluación en una respuesta normal silenciosa.
- TODO: Verify tiempos máximos, idempotencia, degradación acordada, alta disponibilidad y pruebas de carga/recuperación.
- TODO: Verify criterios de revisión y corrección de señales, rendimiento sobre comercios legítimos, comprensión del aviso y resultados de los usuarios.

## Pitch ejecutivo de cinco minutos

La versión actual tiene cinco diapositivas de pitch más un opener y una diapositiva de referencias IEEE: visión, propuesta, escala SPEI, benchmark ejecutado,
funcionamiento continuo, valor para producto/negocio, escala AWS propuesta,
ruta de migración y petición de piloto. Se retiraron la persona ficticia, el
recorrido narrativo y las explicaciones repetidas. Los tiempos del speech
suman 300 segundos; su duración real depende del ritmo y las pausas.

| Slide | Tiempo | Propósito |
| --- | --- | --- |
| 1. Escala | 30 s | 797.9 M de operaciones y $29.93 T operados en agosto de 2026, con periodo y fuente |
| 2. Evidencia | 45 s | 615 operaciones, 6/6 APP, 0% falsas alertas y $146,800 de exposición sintética |
| 3. High level | 45 s | Worker continuo → base de riesgo → API → banco |
| 4. Negocio | 40 s | Pérdida, continuidad de pagos y operación; resultados por medir |
| 5. Low level AWS | 60 s | Escalar worker y API por separado; estado compartido |
| 6. Migración | 45 s | Base portable y trabajo pendiente para ECS/Fargate |
| 7. Petición | 30 s | Piloto autorizado, evidencia de impacto y cobertura progresiva |

El financiamiento sigue por definir. La revisión prioriza el pedido del equipo:
valor ejecutivo y escalabilidad en cinco minutos, sin pretender demostrar un
modelo de ingresos validado ni cubrir cada elemento de la rúbrica en una slide.

## Arquitectura AWS propuesta: evidencia y condiciones

5. [AWS — Imágenes de ECR en ECS](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html).
6. [AWS — ECS Service Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html).
7. [AWS — Fargate task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html).

ECR almacena imágenes que ECS puede ejecutar; Fargate permite ejecutar las tareas.
ECS Service Auto Scaling modifica la cantidad de tareas según políticas configuradas.
Las tareas Fargate usan red `awsvpc`; un ALB para esas tareas utiliza destinos IP.
Estas capacidades de AWS no implican que el proyecto las tenga desplegadas.

**Verificado en archivos:** existen Dockerfiles para API, generador y UI;
`compose.yaml` usa PostgreSQL; la aplicación configura su conexión por entorno;
Alembic contiene el esquema. Son una base portable. No se construyeron imágenes
ni se ejecutó una migración a AWS en esta revisión.

**Ruta propuesta:** construir y validar imágenes → publicar versiones en ECR →
definir tareas y servicios ECS/Fargate → conectar PostgreSQL administrado en RDS.
Agregar ALB, permisos IAM, secretos, red privada y observabilidad según el diseño.
No se creó infraestructura, IaC, pipeline ni recursos de nube.

**Escalamiento horizontal con sentido:**

- API de lectura como servicio independiente detrás de ALB, con réplicas que
  comparten estado y límites de conexiones. Escalar por solicitudes/utilización.
- Workers independientes del servidor del simulador. Repartir el trabajo,
  proponer particionado por CLABE y diseñar idempotencia y control de concurrencia.
  Escalar por backlog y retraso de procesamiento; no duplicar consumidores sin
  asignación coordinada. El estado de pagadores que abarque particiones necesita
  agregación compartida; partir por destino no resuelve todos los cómputos.
- La base no escala automáticamente al agregar tareas. Preparar agregaciones e
  índices, controlar escrituras/conexiones y medir capacidad y consistencia.
- `apps/api/Dockerfile` actualmente ejecuta `alembic upgrade head` al arrancar
  cada contenedor. Antes de replicar, ejecutar migraciones como una tarea única
  controlada y aplicar despliegues compatibles con el esquema.
- El generador actual es un simulador con estado en proceso y un replay finito.
  No debe replicarse como si ya fuera un worker productivo distribuido.

La aspiración es conservar las reglas del motor durante la migración. No se
promete un traslado automático o sin ajustes. Faltan infraestructura, separación
del worker productivo, estado por CLABE/contrato de lectura, coordinación,
seguridad y validación de carga/recuperación. Las cifras del benchmark local no
son una prueba de throughput ni de costos en Fargate.
