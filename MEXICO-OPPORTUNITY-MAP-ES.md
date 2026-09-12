# Mapa de oportunidades de México: inteligencia financiera continua

**Corte de evidencia:** 11 de septiembre de 2026
**Propósito:** Descubrimiento de producto para el reto HackMTY Capital One; no se especifica ni se implica ninguna implementación de producto.

## A. Recomendación ejecutiva y alcance de la investigación

### Recomendación

Construir un **SPEI Intent & Recipient Guard** previo al envío para estafas de pagos autorizados por el usuario (APP, por sus siglas en inglés) y coerción. El momento específico es el de un cliente genuino que prepara una transferencia inusual a un beneficiario nuevo o recientemente riesgoso mientras un estafador lo manipula. El sistema combina el comportamiento del ordenante, el contexto de la sesión, el historial del beneficiario y señales de la red receptora; explica el riesgo y ofrece fricción reversible y controlada por el usuario antes de que la transferencia entre a SPEI.

Esto es más sólido que un detector de fraude genérico porque la autenticación normal puede tener éxito cuando el cliente está siendo engañado. También es más sólido que un asesor financiero genérico porque tiene un evento preciso, una ventana de intervención de segundos, acciones acotadas y resultados medibles. Además, expresa mejor el tema del patrocinador: flujo continuo de eventos, puntuación en tiempo real, explicación agéntica, una salvaguarda visible y aprobación humana.

Las dos alternativas más sólidas son:

1. **Quincena Collision Guard** para hogares asalariados: pronosticar faltantes entre el día de pago y el vencimiento, y proponer acciones reversibles sin emitir nuevo crédito.
2. **Cobro-30** para pequeños proveedores B2B: combinar CFDI, complementos de pago, depósitos bancarios y obligaciones para predecir la liquidez a 30 días y priorizar la cobranza.

### Alcance

Esta síntesis combina seis líneas de investigación sobre México: inversionistas minoristas, hogares asalariados, PYMES y negocios informales, inclusión regional, crédito al consumidor y fraude/seguridad. Evalúa oportunidades en:

1. **Autonomía financiera del consumidor y creación de historial crediticio**
2. **Inteligencia sobre flujo de efectivo y capital de trabajo para PYMES**
3. **Centinela de anomalías y seguridad en tiempo real**

La solución puede atender a consumidores, negocios, bancos, prestamistas, proveedores de remesas o instituciones de pago. El prototipo recomendado usa datos sintéticos/públicos y acciones simuladas; no supone la existencia de un feed universal mexicano de banca abierta.

### Reglas de evidencia

- **Hecho** significa una observación respaldada directamente por la fuente citada. Se prefieren fuentes oficiales mexicanas.
- **Hipótesis** significa una propuesta de producto, comportamiento o causalidad que requiere investigación con usuarios o datos transaccionales de un socio.
- **Anécdota** significa una experiencia reportada por una persona o proveedor que no constituye evidencia poblacional.
- Los conteos de quejas no se tratan como víctimas únicas, fraude confirmado, fraude intentado o pérdida exitosa, salvo que la fuente lo indique explícitamente.
- Las correlaciones y diferencias entre grupos no se presentan como causas.
- Se mantienen separados los denominadores en conflicto. Por ejemplo, la tenencia de productos de ENIF, las quejas de CONDUSEF, los reclamos bancarios y la victimización de ENVIPE no se combinan.
- Las leyes públicas que autorizan categorías de intercambio de datos no se tratan como prueba de que exista una API universal en producción.
- No se usa ninguna anécdota de comunidades o foros para la clasificación. Se conserva una etnografía únicamente como contexto de diseño, no como evidencia de prevalencia.
- Toda fecha, condición de acceso o capacidad de producción no establecida por la fuente se marca como **TODO: Verify**.

---

## B. Línea base de evidencia sobre México

### Hechos verificados

1. **El acceso formal es más amplio que el crédito activo o el ahorro formal.** En 2024, el 76.5% de los adultos de 18 a 70 años tenía al menos un producto financiero formal, el 63.0% tenía una cuenta de ahorro formal y el 37.3% tenía crédito formal. En el año anterior, el 36.6% ahorró únicamente de manera informal y el 33.6% no ahorró. Estas categorías describen el uso de productos y el comportamiento de ahorro, no la profundidad del expediente en una sociedad de información crediticia ([INEGI/CNBV, ENIF 2024, publicado en 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

2. **La fragilidad financiera es importante.** En ENSAFI 2023, el 30.5% de los adultos reportó dinero insuficiente para cubrir sus gastos; el 27.3% de los adultos con deuda reportó haberse atrasado en un préstamo o pago de crédito; y el 35.9% dijo que sus ahorros podrían cubrir una emergencia equivalente a un mes de ingresos. Son estimaciones autodeclaradas de adultos, no medidas exclusivas de trabajadores asalariados ([INEGI/CONDUSEF, ENSAFI 2023, publicado en 2024](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf)).

3. **La nómina es un punto de entrada útil, pero incompleto.** ENIF 2024 encontró que el 36.2% de los adultos tenía una cuenta de nómina o pensión y que la nómina fue la primera cuenta formal para el 46.5% de las personas que alguna vez tuvieron una ([INEGI/CNBV, 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

4. **El ingreso irregular no es un caso extremo.** En julio de 2026, el 56.2% de las personas ocupadas estaba en la informalidad laboral y 13.6 millones de personas trabajaban por cuenta propia. La informalidad no equivale a estar fuera del sistema bancario ni a ser riesgoso, pero hace incompletos los supuestos de días de pago fijos ([INEGI, ENOE julio de 2026, publicado en 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf)).

5. **Las brechas regionales y de uso de efectivo son grandes.** En la región Sur de México, el 67.7% de los adultos tenía algún producto formal, el 55.5% una cuenta y el 29.9% crédito. Para compras superiores a MXN 500, el 82.0% normalmente usaba efectivo y solo el 29.8% creía que todos o casi todos los negocios aceptaban tarjetas o transferencias ([INEGI/CNBV, ENIF 2024, publicado en 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)).

6. **La conectividad mejora, pero es desigual.** El uso de internet en 2025 fue del 88.9% en zonas urbanas y del 75.2% en zonas rurales; el acceso a internet en los hogares fue del 90.5% en Ciudad de México, del 64.0% en Oaxaca y del 53.9% en Chiapas. Estas cifras no miden la confiabilidad de la conexión, el uso compartido de dispositivos ni la facilidad de uso de las aplicaciones financieras ([INEGI, ENDUTIH 2025, publicado en 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf)).

7. **Las remesas crean un recorrido digital-a-efectivo particular.** México recibió USD 61.791 mil millones en remesas en 2025. Las transferencias electrónicas representaron el 99.1% del valor, pero el 49.6% de las remesas enviadas electrónicamente se pagó en efectivo. Los flujos agregados no identifican la demografía de los receptores, quién controla los fondos ni el comportamiento de permanencia ([Banco de México, remesas de 2025, publicado en 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf)).

8. **Las microempresas dominan la base de establecimientos.** De los 5,468,180 establecimientos cubiertos por los Censos Económicos 2024, el 95.4% tenía entre 0 y 10 trabajadores. Una clasificación censal independiente encontró que el 64.3% de los establecimientos cubiertos era informal; este no es el mismo denominador ni la misma definición que el empleo informal ([INEGI, informe definitivo de los Censos Económicos 2024, actualizado en 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf); [INEGI, minimonografía nacional, 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/ce2024_mn00.pdf)).

9. **La rotación empresarial es alta, pero su causa no está establecida.** INEGI estimó 1.7 millones de nacimientos y 1.4 millones de muertes de establecimientos MIPYME entre mayo de 2019 y mayo de 2023 en los sectores urbanos cubiertos. El estudio no atribuye las muertes a liquidez, pagos tardíos ni a una causa única ([INEGI, EDN 2023, publicado en 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf)).

10. **El pago B2B tardío es observable, aunque la mejor medida reciente es comercial.** Atradius reportó que el 48% de las facturas B2B mexicanas encuestadas estaba vencido, que el pago promediaba 38 días después de la fecha de vencimiento y que la deuda incobrable equivalía al 6% de las ventas B2B a crédito. Es una encuesta comercial, no un censo de todas las PYMES ([Atradius, Prácticas de pago en México 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024)).

11. **El sistema CFDI de México expone el estado de pago de las facturas.** El Complemento de Pago 2.0 es obligatorio para pagos parciales o diferidos relevantes y está diseñado para mostrar si una factura se pagó, lo que crea una señal de cuentas por cobrar específica de México ([SAT, Complemento de Pago, obligatorio desde 2023; página vigente al corte](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm)).

12. **SPEI es ubicuo y rápido.** En 2025, SPEI procesó 7,308.1 millones de transferencias; 7,302.4 millones fueron operaciones de usuarios, el 94.6% de las operaciones de usuarios fue de 1,500 UDIS o menos y aproximadamente 82.9 millones de personas participaron en al menos una transferencia SPEI en el cuarto trimestre de 2025. El volumen y la participación no son medidas de fraude ([Banco de México, Informe sobre las Infraestructuras de los Mercados Financieros 2025, publicado el 11 de septiembre de 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)).

13. **El fraude es importante, pero las medidas oficiales responden preguntas distintas.** ENVIPE estimó 8,290 incidentes de fraude por cada 100,000 adultos en 2025, combinando fraude bancario y al consumidor y contando incidentes, no víctimas únicas ([INEGI, ENVIPE 2026](https://www.inegi.org.mx/contenidos/programas/envipe/2026/doc/envipe2026_presentacion_nacional.pdf)). Por separado, CONDUSEF recibió 37,582 asuntos de “posible fraude” entre enero y junio de 2025, incluidas 7,045 quejas por transferencias electrónicas no reconocidas; son quejas, no fraudes confirmados, intentos ni víctimas únicas ([CONDUSEF, informe de autoevaluación del primer semestre de 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)).

14. **Las estafas APP son un punto ciego de medición.** Las categorías de operaciones no reconocidas de CONDUSEF y el mecanismo de colaboración de la Regla 43 de Banco de México se enfocan principalmente en transacciones que el cliente afirma no haber solicitado. Un cliente que autentica personalmente una transferencia mientras está siendo engañado puede no encajar en ese enfoque ([CONDUSEF, 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf); [Banco de México, Circular 14/2017 compilada hasta 2026](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf)).

15. **Los datos transaccionales pueden mejorar el otorgamiento de crédito sin score en una muestra mexicana específica.** Un estudio de 2026 sobre solicitantes de RappiCard sin score convencional de una sociedad de información crediticia reportó un AUC de 0.791 para su modelo de referencia; eliminar los datos transaccionales redujo el AUC en 0.137. Es evidencia sólida para ese prestamista y esa muestra, no una estimación nacional ni un permiso para rechazos automatizados ([Chioda, Gertler, Higgins y Medina, 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf)).

16. **El acceso a datos y la privacidad limitan todas las oportunidades.** El artículo 76 de la Ley Fintech reconoce categorías que incluyen datos transaccionales y exige autorización expresa del cliente para compartirlos, pero no demuestra que exista conectividad universal en producción ([Cámara de Diputados, Ley Fintech, vigente hasta 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf)). Los datos financieros y patrimoniales generalmente requieren consentimiento expreso conforme a la ley mexicana de protección de datos del sector privado ([Cámara de Diputados, LFPDPPP, promulgada en 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)).

### Hipótesis que requieren validación

- Combinar señales de intención del ordenante y de la red receptora puede identificar estafas APP con una tasa de intervención suficientemente baja para ser aceptable.
- Pronosticar el saldo mínimo antes del siguiente depósito de nómina evitará más atrasos que elaborar presupuestos retrospectivos.
- El estado del CFDI/complemento de pago junto con los depósitos bancarios puede predecir el momento de cobranza B2B mejor que la fecha de vencimiento por sí sola.
- Un ahorro conservador y consciente de la volatilidad puede hacer crecer los fondos de emergencia sin provocar pagos esenciales incumplidos.
- Un pasaporte portable de evidencia de flujo de efectivo puede conservar parte del valor predictivo de los datos propietarios de plataformas sin dejar de ser explicable y justo.

### Anécdotas y evidencia cualitativa

No se usan anécdotas de foros, Reddit, Facebook, TikTok ni otras comunidades. Una etnografía de una comunidad de Oaxaca solo es relevante como advertencia de no tratar a las mujeres que reciben remesas como usuarias pasivas ni ignorar las prácticas del hogar o la comunidad; no se usa para medir prevalencia ni para clasificar oportunidades ([Smyth, tesis doctoral de la University of Kentucky, 2022](https://uknowledge.uky.edu/geography_etds/83/)).

---

## C. Mapa de oportunidades clasificado

### 1. SPEI Intent & Recipient Guard

- **Segmento principal:** Cliente de un banco o wallet que envía una transferencia SPEI inusual a un beneficiario nuevo.
- **Pista relevante del reto:** Centinela de anomalías y seguridad en tiempo real.
- **Problema mexicano específico:** SPEI se liquida rápidamente, mientras que un cliente genuino sometido a ingeniería social puede superar la autenticación. Las categorías existentes de transferencias no autorizadas no capturan claramente una intención manipulada pero autenticada.
- **Evidencia/citas:** La escala de SPEI y sus reglas de operación rápida están documentadas por [Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf) y la [Circular 14/2017](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf). Las categorías de quejas de CONDUSEF muestran un daño considerable por pagos no autorizados, pero también una brecha de medición de APP ([CONDUSEF, 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)).
- **Por qué importa:** La intervención más útil ocurre antes del envío; después de la liquidación no se puede prometer la recuperación.
- **Alternativas existentes y limitaciones:** La autenticación, el riesgo del dispositivo, los límites de transacción, las alertas, las advertencias de CONDUSEF, SIPRES y la asistencia interbancaria abordan identidad, monto, educación o pagos no autorizados. No necesariamente verifican si un usuario autenticado actúa bajo engaño.
- **Dirección de producto propuesta:** Generar puntuaciones separadas de `account takeover`, `payer intent` y `recipient network`, e intervenir solo cuando múltiples señales se refuercen entre sí.
- **Datos transaccionales/conductuales continuos usados:** Monto como proporción del saldo, beneficiario visto por primera vez, historial de transferencias, momento de creación del beneficiario, continuidad de sesión/dispositivo, indicador aproximado y autorizado de llamada activa o acceso remoto, y riesgo de entradas/salidas de la red receptora.
- **Acciones agénticas/automatizadas potenciales:** Explicar la anomalía; hacer una pregunta específica sobre estafas; ofrecer una llamada verificada del banco, autenticación reforzada o una pausa de enfriamiento elegida por el usuario; armar un caso para un analista. Nunca enviar, cancelar, revertir, congelar, incluir en una lista negra ni reportar automáticamente.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** No capturar audio de llamadas, mensajes, contactos, contenido del portapapeles ni capturas de pantalla. Usar limitación de propósito, retención corta, códigos de motivo, pruebas de falsos positivos por subgrupo, apelación y anulación humana. Cualquier retención o intercambio entre bancos requiere autoridad específica de la institución.
- **Viabilidad para el hackatón:** **Alta.** Transmitir eventos sintéticos de ordenante/sesión/beneficiario/grafo receptor mediante reglas transparentes y un modelo interpretable.
- **Diferenciación frente a ideas fintech comunes:** Pregunta “¿el cliente autenticado está siendo manipulado?” en vez de “¿es este el cliente?”, y relaciona la intención del ordenante con el riesgo del grafo receptor.
- **Potencial de demo e impacto medible:** Mostrar una transferencia inusual legítima que continúa y una transferencia coercionada a un beneficiario nuevo que recibe fricción específica. Métrica principal: recuperación ponderada por valor de APP con una tasa fija de desafío a pagos genuinos; mostrar también latencia y tasa de falsos positivos.
- **Etiqueta de evidencia:** El diseño de intervención es una **hipótesis**; la escala, velocidad de los pagos y brecha de medición oficial son **hechos**.

### 2. Quincena Collision Guard

- **Segmento principal:** Trabajadores y hogares asalariados pagados semanalmente o en intervalos de hasta 15 días.
- **Pista relevante del reto:** Autonomía financiera del consumidor y creación de historial crediticio.
- **Problema mexicano específico:** Las facturas, pagos de tarjetas, cargos de préstamos de nómina y transferencias del hogar pueden coincidir antes del siguiente depósito, aunque el ingreso mensual parezca suficiente.
- **Evidencia/citas:** La fragilidad y los atrasos de adultos a nivel nacional están documentados por [INEGI/CONDUSEF, ENSAFI 2023](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf); el alcance de las cuentas de nómina por [INEGI/CNBV, ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf); y la estructura de los débitos directos de créditos de nómina y los indicadores de crédito de 2024 por [Banco de México](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf).
- **Por qué importa:** Evitar un pago atrasado o un préstamo de emergencia es más accionable que mostrar un gráfico retrospectivo de gastos.
- **Alternativas existentes y limitaciones:** Las alertas bancarias son reactivas; BBVA Apartados separa fondos manualmente; los productos de acceso anticipado al salario proporcionan liquidez, pero pueden trasladar el faltante al siguiente ciclo de pago ([BBVA México, fecha no mostrada](https://www.bbva.mx/personas/productos/cuentas/apartados.html); [Minu, fecha no mostrada](https://www.minu.mx/salario-on-demand)).
- **Dirección de producto propuesta:** Pronosticar el saldo mínimo seguro hasta los siguientes dos días de pago y explicar las obligaciones exactas que producen un déficit.
- **Datos transaccionales/conductuales continuos usados:** Depósitos de nómina, saldo, débitos recurrentes, fechas de vencimiento, cuotas de préstamos, pagos mínimos de tarjetas, transferencias del hogar y obligaciones de efectivo opcionales.
- **Acciones agénticas/automatizadas potenciales:** Reservar fondos en un apartado, redactar una solicitud para cambiar la fecha de vencimiento, proponer pausar un pago recurrente no esencial o programar un recordatorio. Cualquier transferencia, cancelación o contacto con un acreedor requiere aprobación.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Mostrar incertidumbre; nunca garantizar la fecha de la nómina; no vender crédito mediante una presión basada en el miedo; no iniciar préstamos; usar consentimiento explícito y acceso revocable.
- **Viabilidad para el hackatón:** **Muy alta.** Son suficientes eventos sintéticos de nómina, facturas, préstamos, emergencias médicas y débitos duplicados.
- **Diferenciación frente a ideas fintech comunes:** Prevención prospectiva de colisiones vinculada al ritmo de pago mexicano, no un presupuesto genérico ni otro adelanto de efectivo.
- **Potencial de demo e impacto medible:** Detectar un faltante etiquetado con 3 a 7 días de anticipación y mostrar una intervención reversible que lo elimina. Métricas: recuperación de faltantes, tasa de falsas alertas, error de pronóstico y cargos o intereses moratorios simulados evitados.
- **Etiqueta de evidencia:** La fragilidad y el acceso a nómina son **hechos**; la prevalencia de colisiones específicas del día de pago y el efecto de la intervención son **hipótesis**.

### 3. Cobro-30: copiloto de cuentas por cobrar CFDI-a-pista de liquidez

- **Segmento principal:** Proveedores B2B formales o en transición a la formalidad, con clientes recurrentes, cobros bancarizados y poco personal de tesorería.
- **Pista relevante del reto:** Inteligencia sobre flujo de efectivo y capital de trabajo para PYMES.
- **Problema mexicano específico:** Las fechas de vencimiento de las facturas no equivalen a las fechas de recepción del efectivo, mientras que la nómina, los proveedores, la renta, los impuestos y la deuda crean obligaciones fechadas.
- **Evidencia/citas:** La escala y rotación de microempresas provienen de los [Censos Económicos 2024 de INEGI](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf) y de [EDN 2023](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf). Las estimaciones de pagos tardíos provienen de [Atradius, 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024). El estado de pago estructurado proviene del [Complemento de Pago del SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm).
- **Por qué importa:** Una advertencia fechada puede activar la cobranza o una reprogramación antes de que el negocio recurra automáticamente a financiamiento costoso.
- **Alternativas existentes y limitaciones:** NAFIN documenta su oferta de Cadenas Productivas, pero esta investigación no verificó la cobertura de funciones entre productos contables y de tesorería. **Hipótesis:** los usuarios objetivo carecen de una cola de acciones que abarque cobranza, resolución de disputas, reprogramación y financiamiento. **TODO: Verify** las capacidades actuales de competidores ([NAFIN](https://nafin.com/portalnf/content/cadenas-productivas/cadenas_productivas.html)).
- **Dirección de producto propuesta:** Relacionar CFDI y complementos de pago con depósitos, estimar ventanas de recepción y pronosticar una distribución diaria del saldo de efectivo a 30 días.
- **Datos transaccionales/conductuales continuos usados:** XML de CFDI, estado PUE/PPD, complementos de pago, cancelaciones, depósitos bancarios, fechas de vencimiento, historial del pagador, nómina, renta, proveedores, deuda y fechas fiscales.
- **Acciones agénticas/automatizadas potenciales:** Redactar un recordatorio de cobranza específico para una factura; producir una lista de verificación para una disputa; simular descuentos por pronto pago; comparar factoraje con acciones que no impliquen deuda; preparar lenguaje para reprogramar pagos a proveedores. La aprobación humana es obligatoria.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Nunca almacenar la clave privada e.firma sin procesar de un contribuyente. Una factura vencida no es fraude. Mostrar intervalos de predicción y procedencia; revelar conflictos de interés por referencias de financiamiento; prohibir el financiamiento o contacto autónomo con clientes.
- **Viabilidad para el hackatón:** **Alta.** Usar CFDI, complementos, depósitos y obligaciones sintéticos; no se requieren credenciales reales del SAT.
- **Diferenciación frente a ideas fintech comunes:** Estado de pago de facturas específico de México más una cola de acciones prospectivas, en vez de un dashboard genérico para PYMES o una oferta de préstamo.
- **Potencial de demo e impacto medible:** Predecir el primer día de efectivo negativo, relacionar depósitos con facturas y mostrar qué acción aprobada elimina la brecha. Métricas: error de fecha de pago, recuperación del faltante a siete días, tasa de coincidencias y días de faltante proyectado evitados.
- **Etiqueta de evidencia:** La mecánica de pagos tardíos y CFDI son **hechos**; el desempeño de predicción de pagos es una **hipótesis**.

### 4. Autopiloto de fondo de emergencia consciente de la volatilidad

- **Segmento principal:** Trabajadores informales, independientes, de plataformas o con pago estacional que tienen una cuenta, pero no ahorran formal y consistentemente.
- **Pista relevante del reto:** Autonomía financiera del consumidor y creación de historial crediticio.
- **Problema mexicano específico:** Las transferencias recurrentes fijas suponen ingresos estables y visibilidad digital completa, mientras que muchos trabajadores tienen depósitos variables y gastos intensivos en efectivo.
- **Evidencia/citas:** La informalidad laboral y el trabajo por cuenta propia son medidos por [INEGI, ENOE julio de 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf). Las distribuciones de métodos de ahorro y uso de efectivo provienen de [INEGI/CNBV, ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf).
- **Por qué importa:** El producto puede crear resiliencia sin ampliar el crédito, siempre que nunca provoque el incumplimiento de un pago esencial.
- **Alternativas existentes y limitaciones:** El ahorro recurrente fijo y el redondeo de tarjetas no se adaptan a la volatilidad del ingreso ni al efectivo no observado. Cetesdirecto permite el ahorro recurrente, pero no es un motor de asequibilidad basado en flujo de efectivo ([Cetesdirecto](https://www.cetesdirecto.com/sites/portal/invertir-en-cetes.ahorro-recurrente)).
- **Dirección de producto propuesta:** Estimar continuamente un monto conservador “seguro para ahorrar hoy”, saldo protegido, días de fondo de emergencia y confianza sobre efectivo faltante.
- **Datos transaccionales/conductuales continuos usados:** Depósitos, cobros SPEI, pagos de plataformas, depósitos en efectivo, retiros de cajero, gastos esenciales, pagos de deuda y entradas opcionales de ingresos/obligaciones en efectivo.
- **Acciones agénticas/automatizadas potenciales:** Proponer o ejecutar un microtraspaso limitado y reversible con consentimiento permanente explícito; pausar antes de periodos de poco efectivo; devolver fondos si una factura crítica queda en riesgo; pedir confirmación cuando disminuya la visibilidad del efectivo.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Usar por defecto el límite inferior del pronóstico, ofrecer pausa con un toque y reversión inmediata, nunca crear sobregiros ni bloquear fondos esenciales y distinguir los depósitos asegurados de las inversiones.
- **Viabilidad para el hackatón:** **Muy alta.** Son suficientes flujos sintéticos de ingresos irregulares completamente simulados.
- **Diferenciación frente a ideas fintech comunes:** El agente a veces decide **no** ahorrar y explica por qué; no es una función de redondeo ni una meta mensual fija.
- **Potencial de demo e impacto medible:** Comparar 90 días simulados con ahorro recurrente fijo. Métricas: crecimiento del fondo, pagos críticos incumplidos, traspasos que causan saldo negativo (objetivo: cero) y cobertura del intervalo de pronóstico.
- **Etiqueta de evidencia:** La escala del segmento es un **hecho**; el aumento del ahorro retenido es una **hipótesis**.

### 5. RemesaGuard Sur

- **Segmento principal:** Receptores de remesas rurales y de localidades pequeñas del Sur y Centro-Sur/Oriente, especialmente adultos mayores y usuarios que necesitan interacción accesible o de baja conectividad.
- **Pista relevante del reto:** Centinela de anomalías y seguridad en tiempo real.
- **Problema mexicano específico:** Las remesas transmitidas digitalmente con frecuencia se convierten en efectivo en regiones con menor uso de productos y conectividad; la experiencia genérica de fraude con tarjetas, siempre conectada, no se adapta a este recorrido.
- **Evidencia/citas:** El volumen de remesas y el pago en efectivo provienen de [Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf); el comportamiento financiero regional de [ENIF 2024](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf); la conectividad de [ENDUTIH 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf); y las barreras de accesibilidad de [CNBV/GIZ, 2023](https://www.gob.mx/cnbv/articulos/inclusion-financiera-de-las-personas-con-discapacidad?idiom=es).
- **Por qué importa:** Una pérdida inmediatamente posterior a la recepción de una remesa puede eliminar fondos destinados a alimentos, salud u obligaciones del hogar.
- **Alternativas existentes y limitaciones:** Los proveedores de remesas, bancos, Banco del Bienestar y la educación antifraude mueven o protegen el dinero dentro de sus propios canales, pero no necesariamente ofrecen un centinela conductual accesible, consciente del retiro de efectivo y capaz de operar sin conexión.
- **Dirección de producto propuesta:** Aprender la cadencia de remesas y marcar una combinación inusual de transferencia o retiro sin tratar el uso de efectivo, la ruralidad, la edad o la discapacidad como sospechosos.
- **Datos transaccionales/conductuales continuos usados:** Depósitos de remesas, retiros en efectivo, beneficiarios nuevos, velocidad de transferencias, monto relativo a la remesa reciente, estado de conectividad y retiro en efectivo esperado confirmado por el usuario.
- **Acciones agénticas/automatizadas potenciales:** Explicar la anomalía; ofrecer confirmar, reducir, pausar, llamar mediante un canal verificado o verificar en persona. Guardar localmente la decisión cuando no haya conexión y sincronizar después los datos mínimos.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Nunca exigir un familiar o contacto de confianza; la coerción puede provenir del hogar. Probar falsos positivos por sexo, edad, ruralidad, discapacidad, idioma y conectividad. No bloquear con base en geografía o comportamiento de efectivo.
- **Viabilidad para el hackatón:** **Alta.** Bastan eventos sintéticos de remesa/retiro de efectivo, una cola sin conexión y una interfaz accesible.
- **Diferenciación frente a ideas fintech comunes:** Cadencia de remesas, comportamiento digital-a-efectivo, accesibilidad y conectividad intermitente, no una alerta de fraude genérica.
- **Potencial de demo e impacto medible:** Detener una transferencia de estafa simulada y permitir una transferencia médica legítima. Métricas: pérdida evitada por cada 1,000 alertas, límite de falsos positivos por subgrupo, latencia de la decisión sin conexión y finalización exitosa del flujo de recuperación.
- **Etiqueta de evidencia:** Los patrones regionales, de remesas y de acceso son **hechos**; la utilidad predictiva de la cadencia es una **hipótesis**.

### 6. Dimo Rebinding and First-Transfer Guard

- **Segmento principal:** Usuarios de Dimo que envían a un número telefónico poco después de volver a vincular el teléfono con una cuenta, cambiar de dispositivo o restablecer la autenticación.
- **Pista relevante del reto:** Centinela de anomalías y seguridad en tiempo real.
- **Problema mexicano específico:** Las transferencias dirigidas a números telefónicos crean un riesgo acotado de vinculación de identidad al volver a vincular y durante el primer pago posterior.
- **Evidencia/citas:** Banco de México reportó 16.4 millones de usuarios Dimo registrados y 3.1 millones de transferencias interinstitucionales por MXN 3.7 mil millones en 2025; esas cifras de uso no establecen una tasa de fraude ([Banco de México, 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)).
- **Por qué importa:** La transición de estado crea un punto preciso de intervención antes de la primera transferencia material posterior a un cambio de vinculación.
- **Alternativas existentes y limitaciones:** Dimo muestra las iniciales del receptor y requiere consentimiento para la inscripción, pero la evidencia pública no establece un centinela dedicado de re-vinculación entre eventos ([Banco de México, informe de infraestructuras 2024, publicado en 2025](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BE0085475-B1D7-DED0-60AF-05ED88153BDC%7D.pdf)).
- **Dirección de producto propuesta:** Usar una máquina de estados transparente: estable → re-vinculación → confirmación de dispositivo nuevo → primera transferencia entrante/saliente → ráfaga.
- **Datos transaccionales/conductuales continuos usados:** Eventos de vinculación/desvinculación/re-vinculación, tiempo desde la re-vinculación, cambio de dispositivo/autenticación, confirmación de iniciales del receptor, historial emisor-receptor, monto y ráfaga de recibos.
- **Acciones agénticas/automatizadas potenciales:** Exigir confirmación fuera de banda en el canal previamente confiable, enfatizar las iniciales del receptor o proponer un periodo de enfriamiento para una primera transferencia de alto riesgo.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** No tratar la portabilidad del número ni el reemplazo del dispositivo como fraude; no ingerir agendas de contactos; ofrecer recuperación por pérdida del teléfono; revelar los datos utilizados.
- **Viabilidad para el hackatón:** **Alta.** Una máquina de estados y un flujo sintético de transiciones son simples y visualmente claros.
- **Diferenciación frente a ideas fintech comunes:** Una secuencia de vinculación de identidad específica de México, en lugar de una puntuación genérica de toma de control de cuenta.
- **Potencial de demo e impacto medible:** Mostrar lado a lado un reemplazo legítimo de teléfono y una re-vinculación maliciosa. Métrica: ataques de redirección inyectados detenidos antes de la primera transferencia con una tasa fija de desafíos falsos.
- **Etiqueta de evidencia:** El uso de Dimo es un **hecho**; la prevalencia del fraude y el valor del detector son **hipótesis desconocidas**.

### 7. IVA Guard: asistente de gasto seguro y reserva fiscal

- **Segmento principal:** Personas físicas de RESICO y pequeños comerciantes de servicios con ventas mixtas en efectivo, SPEI, POS y facturadas.
- **Pista relevante del reto:** Inteligencia sobre flujo de efectivo y capital de trabajo para PYMES.
- **Problema mexicano específico:** Las ventas registradas, el efectivo cobrado, los complementos de pago, el IVA acreditable, las retenciones y las obligaciones próximas crean un saldo bancario engañoso y riesgo de fechas fiscales.
- **Evidencia/citas:** La mecánica del estado de pago de CFDI proviene del [SAT](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm). Las reglas de cobro y pago mensual del IVA están en la [Ley del Impuesto al Valor Agregado](https://www.diputados.gob.mx/LeyesBiblio/pdf_mov/Ley_del_Impuesto_al_Valor_Agregado.pdf); el tratamiento exacto depende del régimen y la operación del contribuyente.
- **Por qué importa:** Una cifra de “seguro para gastar” puede evitar que el negocio consuma fondos probablemente necesarios para impuestos y obligaciones operativas esenciales.
- **Alternativas existentes y limitaciones:** Las herramientas del SAT y el software contable apoyan el cumplimiento y los registros, pero no necesariamente ofrecen una salvaguarda de liquidez continua y consciente de la incertidumbre.
- **Dirección de producto propuesta:** Estimar un rango de obligaciones de IVA y separar los ingresos registrados del efectivo cobrado, reservando nómina, renta y un fondo definido por el usuario.
- **Datos transaccionales/conductuales continuos usados:** Depósitos bancarios, SPEI/CoDi, liquidaciones POS, cierre de efectivo introducido por el usuario, CFDI emitidos/recibidos, complementos de pago, deducciones/retenciones conocidas y calendario de fechas límite.
- **Acciones agénticas/automatizadas potenciales:** Recomendar un monto de reserva, redactar una tarea por complemento faltante, generar una conciliación para el contador y recordar antes de las fechas límite. Nunca presentar, cancelar un CFDI, clasificar conceptos fiscales inciertos ni transferir fondos sin aprobación.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Declarar claramente que las estimaciones no son una declaración ni una opinión legal; separar datos verificados de datos introducidos por el usuario; exigir revisión contable para las clasificaciones; nunca fomentar ventas de efectivo no declaradas.
- **Viabilidad para el hackatón:** **Alta.** Son suficientes los esquemas oficiales y un libro mayor sintético etiquetado.
- **Diferenciación frente a ideas fintech comunes:** IVA mexicano sobre base de efectivo y estado del complemento de pago integrados con liquidez, no un dashboard contable genérico.
- **Potencial de demo e impacto medible:** Métricas: error de pasivo proyectado sobre datos sintéticos reales, detección de complementos faltantes y déficits de fechas fiscales evitados.
- **Etiqueta de evidencia:** Las reglas fiscales y de CFDI son **hechos**; la demanda de mercado y la exactitud de las estimaciones son **hipótesis**.

### 8. Agente de integridad de pago neto y deducciones

- **Segmento principal:** Trabajadores asalariados con deducciones variables, créditos de nómina, horas extra, comisiones o discrepancias sospechadas en el pago neto.
- **Pista relevante del reto:** Autonomía financiera del consumidor y creación de historial crediticio, con conexión con el centinela de seguridad.
- **Problema mexicano específico:** El CFDI de nómina, la compensación esperada, el depósito bancario y los débitos de préstamos pueden no coincidir, pero los trabajadores deben conciliarlos manualmente.
- **Evidencia/citas:** La legislación laboral mexicana otorga a los trabajadores derechos sobre los conceptos y deducciones detallados del pago y limita las deducciones permitidas por categoría ([Cámara de Diputados, Ley Federal del Trabajo, vigente hasta 2026](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf)). Los créditos de nómina suelen debitarse de las cuentas de nómina ([Banco de México, indicadores de crédito de nómina, datos hasta 2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf)).
- **Por qué importa:** Un paquete factual de discrepancias reduce la carga cognitiva y administrativa y puede distinguir el estrés de flujo de efectivo de una deducción inexplicada.
- **Alternativas existentes y limitaciones:** Los portales de nómina, estados de cuenta bancarios, recursos humanos, PROFEDET, prestamistas y CONDUSEF tienen cada uno una parte del flujo; el usuario hace la conciliación.
- **Dirección de producto propuesta:** Conciliar salario bruto → impuestos/deducciones legales → deducciones voluntarias/de préstamos → pago neto esperado → pago neto depositado.
- **Datos transaccionales/conductuales continuos usados:** XML/PDF de CFDI de nómina, pago neto histórico, términos esperados, depósitos bancarios, calendarios de créditos de nómina y débitos de la cuenta.
- **Acciones agénticas/automatizadas potenciales:** Destacar diferencias inexplicadas materiales, redactar una consulta factual a recursos humanos/nómina, crear una línea de tiempo de discrepancias y dirigir al usuario al canal oficial o del prestamista adecuado. Nunca contactar al empleador sin aprobación.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Los archivos de nómina exponen ingresos, empleador, RFC y otros identificadores. Minimizar la retención, ocultar identificadores en los prompts del modelo y etiquetar los hallazgos como “inexplicados”, no como “fraude”, hasta verificarlos.
- **Viabilidad para el hackatón:** **Alta.** Los CFDI de nómina y registros bancarios sintéticos pueden incluir horas extra faltantes, deducciones duplicadas, retrasos y ajustes fiscales legítimos.
- **Diferenciación frente a ideas fintech comunes:** Conciliación documento-a-depósito y recurso de reclamación, no categorización de presupuesto.
- **Potencial de demo e impacto medible:** Métricas: precisión/recuperación de discrepancias, tiempo de conciliación, cobertura de fuentes trazables y cero acusaciones de fraude sin respaldo.
- **Etiqueta de evidencia:** La mecánica legal y de débitos de nómina son **hechos**; la prevalencia de discrepancias es **desconocida**.

### 9. Pasaporte de evidencia de flujo de efectivo para solicitantes sin score

- **Segmento principal:** Solicitantes nuevos en crédito o sin score, con historial transaccional consentido de bancos, wallets, plataformas o comercios.
- **Pista relevante del reto:** Autonomía financiera del consumidor y creación de historial crediticio.
- **Problema mexicano específico:** El crédito formal activo alcanza solo a una parte de la población adulta, mientras que la profundidad convencional en sociedades de información crediticia puede ser insuficiente aun cuando el historial transaccional sea informativo. Se desconoce la población nacional sin expediente o con expediente limitado.
- **Evidencia/citas:** La tenencia de productos y crédito proviene de [ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/enif2024_RR.pdf). El valor predictivo de las transacciones de una plataforma para un prestamista/muestra mexicana proviene de [Chioda et al., 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf).
- **Por qué importa:** La evidencia portable y explicable podría ayudar a un consumidor a llegar a una precalificación revisada por una persona sin vigilancia invasiva de redes sociales o dispositivos.
- **Alternativas existentes y limitaciones:** Las sociedades de información crediticia y los emisores de tarjetas accesibles ya atienden partes del mercado; los modelos propietarios de datos alternativos mantienen la evidencia dentro de una plataforma y pueden ser opacos.
- **Dirección de producto propuesta:** Producir regularidad del ingreso, concentración, consistencia de pagos esenciales, rango de flujo residual, suficiencia de datos, incertidumbre y códigos de motivo, no un score universal de “merecimiento”.
- **Datos transaccionales/conductuales continuos usados:** Depósitos consentidos, cobros SPEI, pagos de plataformas, servicios, aproximaciones de renta, alimentos/transporte, depósitos en efectivo e historial comercial verificado opcional. Excluir contactos, mensajes, grafos sociales, ubicación precisa y precio del dispositivo.
- **Acciones agénticas/automatizadas potenciales:** Esperar evidencia suficiente, solicitar solo datos faltantes materiales, simular un límite pequeño y seguro con fecha de pago alineada y enviar casos limítrofes/adversos a revisión humana. No rechazar automáticamente.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Es la oportunidad de consumidor de mayor riesgo. Probar calibración y error por sexo, localidad, ruralidad, discapacidad y otros grupos relevantes; evitar discriminación por variables proxy; ofrecer corrección, eliminación, revocación, apelación y uso compartido limitado por propósito.
- **Viabilidad para el hackatón:** **Media-alta** para una demostración sintética transparente; baja para afirmar validez de otorgamiento en producción.
- **Diferenciación frente a ideas fintech comunes:** Portabilidad de evidencia controlada por el usuario y un filtro de suficiencia de datos, no una puntuación alternativa opaca.
- **Potencial de demo e impacto medible:** Sobre etiquetas explícitamente sintéticas, reportar la mejora del modelo frente a una línea base sin transacciones, calibración, aprobación con morosidad simulada fija, brechas entre subgrupos y estabilidad de códigos de motivo. No afirmar desempeño crediticio real.
- **Etiqueta de evidencia:** El estudio de un solo prestamista es un **hecho** para su muestra; la generalización nacional y aceptación por prestamistas son **hipótesis**.

### 10. ReconcileMX: monitor de liquidación y fugas multicanal

- **Segmento principal:** Pequeños comercios y negocios de servicios que usan dos o más canales de POS, wallet, marketplace, SPEI/CoDi y efectivo.
- **Pista relevante del reto:** Inteligencia sobre flujo de efectivo y capital de trabajo para PYMES, con conexión con el centinela de seguridad.
- **Problema mexicano específico:** Las ventas, comisiones, retenciones, reembolsos, contracargos, cierres de efectivo y depósitos bancarios están fragmentados; el problema es la conciliación y la visibilidad del efectivo disponible, no afirmar que todos los canales digitales liquidan lentamente.
- **Evidencia/citas:** El Censo Económico encontró que los negocios usan efectivo, transferencias y tarjetas, con respuestas múltiples permitidas ([INEGI, métodos de pago del CE 2024](https://inegi.org.mx/contenidos/programas/ce/2024/doc/ro_infmpn_ce24.pdf)). Las características operativas de SPEI y CoDi están documentadas por [Banco de México](https://www.banxico.org.mx/services/spei_-transfers-banco-mexico.html) y [CoDi](https://www.banxico.org.mx/sistemas-de-pago/codi-cobro-digital-banco-me.html).
- **Por qué importa:** Las liquidaciones faltantes o incompletas distorsionan directamente el efectivo disponible hoy y la capacidad de pagar a proveedores o la nómina mañana.
- **Alternativas existentes y limitaciones:** Clip y Mercado Pago documentan ofertas de proveedores, pero las páginas citadas no establecen la ausencia de funciones entre proveedores. **Hipótesis:** la conciliación entre proveedores que incluye efectivo sigue sin resolverse. **TODO: Verify** las exportaciones, API y cobertura actual de competidores ([Clip](https://www.clip.mx/soluciones); [Mercado Pago](https://www.mercadopago.com.mx/blog/mercado-pago-para-negocios)).
- **Dirección de producto propuesta:** Pronosticar la liquidación neta esperada por proveedor y mostrar ventas no conciliadas, depósitos incompletos, reembolsos duplicados, comisiones inesperadas o variaciones del cierre de efectivo.
- **Datos transaccionales/conductuales continuos usados:** Ventas de POS/adquirente, comisiones, reembolsos, contracargos, saldos de wallets, recibos SPEI/CoDi, depósitos bancarios, cierre de efectivo y CFDI cuando estén disponibles.
- **Acciones agénticas/automatizadas potenciales:** Armar un paquete de evidencia, redactar mensajes de soporte al proveedor y pedir al propietario resolver una variación de efectivo. No ejecutar contracargos, congelar ni acusar de forma autónoma.
- **Consideraciones de IA responsable, privacidad, seguridad y regulación:** Tokenizar referencias de tarjetas; nunca conservar PAN/CVV; etiquetar los eventos como “requiere revisión”; exigir aprobación humana antes de contactar al proveedor o cliente; distinguir la liquidación del proveedor del tiempo del canal de Banxico.
- **Viabilidad para el hackatón:** **Media-alta.** Los CSV y feeds sintéticos pueden producir una demo creíble sin API de proveedores en vivo.
- **Diferenciación frente a ideas fintech comunes:** Inteligencia del efectivo disponible entre canales y empaquetado de evidencia, no otro dashboard de ventas.
- **Potencial de demo e impacto medible:** Métricas: tasa de coincidencia de liquidaciones, precisión/recuperación de anomalías, tiempo de preparación del paquete de disputa y pesos simulados de fugas detectados.
- **Etiqueta de evidencia:** El uso de múltiples canales es un **hecho**; la prevalencia de errores de liquidación y la adopción del producto son **desconocidas**.

---

## D. Matriz de puntuación transparente

### Escala y método

Cada criterio tiene el mismo peso porque el reto exige tanto calidad del problema como demostrabilidad, y no había pesos de evaluación verificados disponibles. Cada oportunidad recibe **1 a 5 puntos** en nueve criterios, para un máximo de **45**:

- **1:** débil, ausente o materialmente restringida
- **2:** por debajo del promedio; brecha importante de evidencia, seguridad o viabilidad
- **3:** creíble, pero mixta
- **4:** sólida
- **5:** excepcional y respaldada directamente

**Protocolo de puntuación:** Cada puntuación debe citar la evidencia que la respalda y aplicar la interpretación específica del criterio anterior. Una puntuación de **5** en Evidencia requiere evidencia directa del problema acotado de la oportunidad, no solo evidencia de la población o área problemática más amplia. Los totales iguales se resuelven, en orden, por solidez de la Evidencia, viabilidad de seguridad/privacidad/regulación, demostración de datos a salida en tiempo real y ventaja de datos específicos de México. Si todos los desempates permanecen iguales, las oportunidades conservan el mismo rango en lugar de forzar un orden sin respaldo.

Criterios:

1. **Magnitud/urgencia**
2. **Solidez de la evidencia**
3. **Población afectada**
4. **Relevancia para la pista del reto**
5. **Diferenciación**
6. **Demostración de datos a salida en tiempo real**
7. **Viabilidad técnica con datos sintéticos/públicos**
8. **Viabilidad de seguridad/privacidad/regulación**
9. **Escalabilidad**

| Rango | Oportunidad | Magn. | Evidencia | Población | Pista | Dif. | Demo en tiempo real | Técnica | Seguridad | Escala | Total /45 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | SPEI Intent & Recipient Guard | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **43** |
| 2 | Quincena Collision Guard | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | **41** |
| 3 | Cobro-30 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | **41** |
| 4 | Autopiloto de fondo consciente de la volatilidad | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | **41** |
| 5 | RemesaGuard Sur | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | **39** |
| 6 | Dimo Rebinding Guard | 3 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | **38** |
| 7 | IVA Guard | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 4 | **38** |
| 8 | Integridad de pago neto y deducciones | 3 | 4 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | **37** |
| 9 | Pasaporte de evidencia de flujo de efectivo | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 2 | 5 | **37** |
| 10 | ReconcileMX | 3 | 3 | 4 | 5 | 4 | 5 | 4 | 4 | 4 | **36** |

### Incertidumbre de las puntuaciones

- Las puntuaciones son juicios ordinales, no valores de mercado medidos. Una diferencia de un punto no es decisiva.
- La evidencia de estafas APP es sólida en escala de pagos, contexto de fraude y lógica previa a la transferencia, pero débil en incidencia APP nacional y verdad fundamental pública; por eso su puntuación de evidencia es 4, no 5.
- Quincena Guard tiene evidencia poblacional sólida, pero la prevalencia específica de colisiones en el día de pago no se ha medido directamente; por eso su puntuación de Evidencia es 4, no 5.
- La accionabilidad de Cobro-30 es sólida porque existen CFDI y complementos de pago, pero la mejor estimación reciente de morosidad B2B es comercial y no representa a todas las PYMES.
- Quincena Guard, Cobro-30 y el Autopiloto de fondo consciente de la volatilidad empatan con 41. Quincena queda en segundo lugar porque su puntuación de seguridad es 5; Cobro-30 queda en tercero porque su diferenciación es 5 frente a 4 del autopiloto. Son desempates documentados, no evidencia de una superioridad significativa de un punto.
- Dimo Rebinding Guard e IVA Guard empatan con 38. Dimo queda en sexto lugar porque sus puntuaciones de demostración en tiempo real y seguridad son mayores.
- Integridad de pago neto y deducciones y Pasaporte de evidencia de flujo de efectivo empatan con 37. Pago neto queda en octavo lugar porque su puntuación de seguridad es mayor.
- El Pasaporte de evidencia de flujo de efectivo obtiene una puntuación baja en viabilidad de seguridad porque un hackatón no puede validar la equidad del otorgamiento en producción ni el cumplimiento regulatorio.
- La puntuación de población afectada de RemesaGuard es 3 porque los datos agregados de remesas no identifican el nicho receptor más acotado de usuarios rurales y que requieren accesibilidad.
- Una rúbrica verificada del hackatón, acceso a datos de socios y entre cinco y diez entrevistas con usuarios objetivo podrían cambiar los rangos varios puntos. **TODO: Verify** los pesos oficiales de evaluación y los datos disponibles del sandbox antes de implementar.

---

## E. Tres nichos más sólidos y sus compensaciones

### 1. Primera opción: SPEI Intent & Recipient Guard

**Por qué gana:** Tiene el flujo continuo de eventos más claro, la ventana de intervención más corta y valiosa, una salvaguarda muy visible y un modo de falla acotado que la autenticación existente puede pasar por alto. Puede demostrarse de forma creíble con datos sintéticos sin afirmar que un modelo de hackatón está listo para producción.

**Compensaciones:** Los datos públicos mexicanos no separan estafas APP, víctimas únicas, pérdidas exitosas ni recuperación. Los datos de la red receptora requerirían un socio institucional. Los falsos positivos podrían retrasar pagos esenciales. Por lo tanto, el MVP debe demostrar fricción dirigida y reversible —no bloqueo de cuentas— y reportar la tasa de desafíos con la misma visibilidad que la detección.

### 2. Alternativa de consumo: Quincena Collision Guard

**Por qué es sólida:** La evidencia oficial sobre liquidez insuficiente, atrasos, límites del fondo de emergencia y alcance de las cuentas de nómina es más sólida que la evidencia de prevalencia de la mayoría de los conceptos fintech para consumidores. El prototipo es fácil de entender y puede medir la prevención de faltantes sin ampliar el crédito.

**Compensaciones:** La investigación no verificó un efecto mexicano amplio de “gastar inmediatamente después del día de pago” entre trabajadores asalariados. La tesis debe mantenerse como desajuste de tiempos más impactos inesperados, no como culpabilización del comportamiento. Es menos novedosa que la detección de intención APP a menos que incluya conciliación de CFDI de nómina/deducciones.

### 3. Alternativa B2B: Cobro-30

**Por qué es sólida:** Tiene la mayor ventaja de datos específicos de México en la pista de PYMES: los CFDI y complementos de pago exponen el estado de facturación y cobranza. También permite varias acciones acotadas antes del financiamiento y crea una métrica empresarial directa.

**Compensaciones:** Excluye intencionalmente a muchas empresas informales que solo operan en efectivo. La evidencia comercial de pagos tardíos es menos representativa que las encuestas nacionales de hogares. La ingestión en producción, la autenticación, el historial por pagador y el manejo de credenciales requieren validación con socios.

### Disposición de conceptos para inversionistas minoristas

Se revisaron conceptos específicos para inversionistas, pero no se clasificaron por separado. La investigación encontró que un guardia contra transferencias relacionadas con estafas de inversión era el único encaje fuerte con las pistas, y ese escenario está incluido en **SPEI Intent & Recipient Guard**. La evaluación de idoneidad, las recomendaciones personalizadas de valores, la gestión de carteras y la operación bursátil quedan fuera de alcance a la espera de **TODO: Verify** sobre requisitos de licenciamiento, idoneidad, conservación de registros e integración con corredores.

### Comparación explícita de los tres candidatos nombrados

| Candidato | Evaluación de evidencia | ¿Más sólido que las alternativas? | Decisión |
|---|---|---|---|
| **Centinela de estafas/coerción APP** | Evidencia sólida sobre escala y velocidad de SPEI, daño general por fraude, suplantación/ingeniería social y una brecha entre autorización e intención; no hay prevalencia APP nacional ni etiquetas públicas. | **Sí, en general.** Es más sólido que herramientas genéricas de toma de control de cuenta, anomalías de tarjeta, desviación de comercios o estafas exclusivamente de inversión porque aborda una brecha de control distinta en un momento preciso de intervención. | **Primera opción**, acotada a beneficiarios SPEI nuevos o recientemente riesgosos y fricción reversible antes del envío. |
| **Autopiloto de flujo de efectivo consciente de la quincena** | Evidencia oficial sólida sobre fragilidad, atrasos, límites del ahorro de emergencia, alcance de cuentas de nómina y débitos de créditos de nómina; no existe una estimación directa de la frecuencia de colisiones en el día de pago. | **Sí, para la Pista 1.** Es más sólido que la detección de suscripciones, el presupuesto genérico, la planeación anual del aguinaldo o un asesor general. La oportunidad es más defendible cuando se formula como pronóstico de colisiones y no como supuesto de gasto excesivo. | **Mejor alternativa de consumo.** |
| **Centinela fiscal/de cuentas por pagar/liquidez para PYMES** | Evidencia oficial sólida sobre escala de microempresas y mecánica de CFDI/impuestos; evidencia media sobre pagos B2B tardíos; no hay una estadística nacional verificada de “30 días de efectivo”. | **Sí, para la Pista 2, si se acota a cuentas por cobrar.** Cobro-30 es más sólido que un centinela general de impuestos/cuentas por pagar/liquidez porque el estado y la acción de la cuenta por cobrar son más claros. IVA Guard es un módulo o segundo producto, no el punto de entrada inicial. | **Mejor alternativa B2B: Cobro-30 primero; reserva fiscal después.** |

La clasificación se basa en evidencia, no en la suposición de que el fraude siempre es el problema más grande. Quincena Guard tiene la evidencia directa más sólida sobre hogares, y Cobro-30 tiene la estructura de datos B2B más específica de México. El centinela APP sigue en primer lugar porque la urgencia, el encaje con la pista, el momento de intervención, la diferenciación y la claridad de la demo compensan su medición de prevalencia más débil.

---

## F. Decisión final

1. **Nicho recomendado y razón de la primera elección:** Construir un **SPEI Intent & Recipient Guard** previo al envío para estafas/coerción APP que involucren beneficiarios nuevos o recientemente riesgosos; es acotado, funciona en tiempo real, se diferencia de la autenticación y permite una intervención humana medible.
2. **Dos nichos alternativos creíbles:** **Quincena Collision Guard** para hogares asalariados y **Cobro-30** para pequeños proveedores B2B.
3. **Usuario objetivo y enunciado central del problema:** Un cliente mexicano de banco o wallet está a punto de autenticar una transferencia SPEI inusual a un beneficiario nuevo mientras es engañado; las comprobaciones normales de identidad pueden pasar y la liquidación puede ocurrir antes de que una advertencia genérica ayude.
4. **Tesis de producto en una frase:** Combinar anomalías de intención del ordenante con riesgo de la red receptora puede activar una advertencia específica y reversible antes del envío por SPEI, permitiendo que continúen los pagos legítimos inusuales.
5. **Prototipo mínimo viable:** Generador de eventos sintéticos, servicio de riesgo en streaming con puntuaciones separadas de toma de control/intención/receptor, explicación y salvaguarda de políticas, interfaz de confirmación en vivo, llamada verificada/pausa de enfriamiento simulada y dashboard de auditoría/equidad.
6. **Flujo de datos, salidas en tiempo real y acciones automatizadas:** Transmitir historial del ordenante, continuidad de sesión/dispositivo, proporción monto/saldo, antigüedad del beneficiario, comportamiento de entrada, estado aproximado y autorizado de llamada/acceso remoto y grafo receptor sintético; producir tipo de riesgo, motivos, latencia y fricción recomendada; automatizar únicamente explicación, orquestación de autenticación reforzada y preparación de casos, no el pago, bloqueo, congelamiento, reversión ni reporte.
7. **Mejor métrica de éxito de la demo:** Recuperación ponderada por valor de estafas APP inyectadas **antes del envío** con una tasa fija de desafíos a pagos genuinos, mostrando al lado la latencia mediana de decisión y las tasas de falsos positivos por subgrupo.
8. **Decisiones siguientes antes de implementar:** Verificar la rúbrica oficial y el sandbox; elegir el supuesto de despliegue institucional; definir presupuestos aceptables de desafío y latencia; aprobar la metodología de escenarios/etiquetas sintéticas; obtener revisión de privacidad/legal para señales de dispositivo/llamada/receptor; decidir si se incluirán datos del grafo receptor; realizar entrevistas con usuarios objetivo y operaciones de fraude; y asignar responsables para el flujo de eventos, puntuación, salvaguarda, interfaz y evaluación.

---

## G. Fuentes

### Oficiales y gubernamentales

- [INEGI/CNBV — resultados ENIF 2024, publicado en marzo de 2025](https://inegi.org.mx/contenidos/programas/enif/2024/doc/enif_2024_resultados.pdf)
- [INEGI — ENIF 2024 Reporte de Resultados, 13 de marzo de 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/enif2024_RR.pdf)
- [INEGI/CONDUSEF — presentación ENSAFI 2023, publicada el 25 de junio de 2024](https://www.inegi.org.mx/contenidos/programas/ensafi/2023/doc/ensafi_2023_presentacion_resultados.pdf)
- [INEGI — ENOE julio de 2026, publicada el 27 de agosto de 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/iooe/IOE2026_08.pdf)
- [INEGI — ENDUTIH 2025, publicada el 16 de junio de 2026](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25.pdf)
- [INEGI — informe definitivo de micro y PYMES de los Censos Económicos 2024, actualizado en 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/rd_infmpmg_ce24.pdf)
- [INEGI — minimonografía nacional de los Censos Económicos 2024, actualizada en septiembre de 2025](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/ce2024_mn00.pdf)
- [INEGI — informe de métodos de pago de los Censos Económicos 2024, 2025](https://inegi.org.mx/contenidos/programas/ce/2024/doc/ro_infmpn_ce24.pdf)
- [INEGI — EDN 2023, publicada el 31 de enero de 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2024/EDN/EDN2023.pdf)
- [INEGI — ENVIPE 2026, publicada el 10 de septiembre de 2026](https://www.inegi.org.mx/contenidos/programas/envipe/2026/doc/envipe2026_presentacion_nacional.pdf)
- [Banco de México — Informe sobre las Infraestructuras de los Mercados Financieros 2025, publicado el 11 de septiembre de 2026](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BDF8FE964-F97C-1B2D-777B-B026EF74C9CF%7D.pdf)
- [Banco de México — Informe sobre las Infraestructuras de los Mercados Financieros 2024, publicado el 23 de mayo de 2025](https://www.banxico.org.mx/publicaciones-y-prensa/informe-anual-sobre-las-infraestructuras-de-los-me/%7BE0085475-B1D7-DED0-60AF-05ED88153BDC%7D.pdf)
- [Banco de México — Circular 14/2017 compilada hasta la Circular 9/2026](https://www.banxico.org.mx/marco-normativo/normativa-emitida-por-el-banco-de-mexico/circular-14-2017/%7BA06FBFEE-06BB-F249-32FC-25B334B2A744%7D.pdf)
- [Banco de México — descripción general de SPEI](https://www.banxico.org.mx/services/spei_-transfers-banco-mexico.html) — **TODO: Verify** la fecha de publicación de la página.
- [Banco de México — CoDi](https://www.banxico.org.mx/sistemas-de-pago/codi-cobro-digital-banco-me.html) — **TODO: Verify** la fecha de publicación de la página.
- [Banco de México — remesas de 2025, publicado el 3 de febrero de 2026](https://www.banxico.org.mx/publicaciones-y-prensa/remesas/%7BED06F2CB-06BA-2EC6-D145-73FF4579BADA%7D.pdf)
- [Banco de México — Indicadores básicos de crédito de nómina, datos hasta diciembre de 2024](https://www.banxico.org.mx/publicaciones-y-prensa/rib-creditos-de-nomina/%7B6516C649-47B0-F483-F574-EEEB18FB3E81%7D.pdf) — **TODO: Verify** la fecha de publicación del PDF.
- [CONDUSEF — informe de autoevaluación del primer semestre de 2025, metadatos del PDF del 26 de agosto de 2025](https://www.condusef.gob.mx/documentos/transparencia/IA-ENE-JUN-2025.pdf)
- [CNBV/GIZ — inclusión financiera de las personas con discapacidad, 3 de mayo de 2023](https://www.gob.mx/cnbv/articulos/inclusion-financiera-de-las-personas-con-discapacidad?idiom=es)
- [SAT — Complemento de Pago 2.0](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/recepcion_de_pagos.htm) — obligatorio desde el 1 de abril de 2023; **TODO: Verify** la fecha de publicación de la página.
- [Cámara de Diputados — Ley Federal del Trabajo, vigente hasta el 14 de mayo de 2026](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf)
- [Cámara de Diputados — Ley Fintech, vigente hasta el 14 de noviembre de 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LRITF.pdf)
- [Cámara de Diputados — LFPDPPP, promulgada el 20 de marzo de 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)
- [Cámara de Diputados — Ley del Impuesto al Valor Agregado](https://www.diputados.gob.mx/LeyesBiblio/pdf_mov/Ley_del_Impuesto_al_Valor_Agregado.pdf) — **TODO: Verify** la fecha exacta de consolidación antes de usarla en producción.
- [NAFIN — Cadenas Productivas](https://nafin.com/portalnf/content/cadenas-productivas/cadenas_productivas.html) — **TODO: Verify** la fecha de publicación de la página y la elegibilidad actual.

### Académicas y de industria

- [Chioda, Gertler, Higgins y Medina — *FinTech Lending to Borrowers with No Credit History*, 28 de febrero de 2026](https://seankhiggins.com/assets/pdf/ChiodaGertlerHigginsMedina_FinTechLendingToBorrowersWithNoCreditHistory.pdf)
- [Atradius — Tendencias de prácticas de pago B2B, México 2024, 28 de octubre de 2024](https://atradius.in/knowledge-and-research/reports/b2b-payment-practices-trends-mexico-2024)
- [Smyth — *Gender and Remittances: Lived Experiences of Women in Oaxaca, Mexico*, 2022](https://uknowledge.uky.edu/geography_etds/83/)
- [BBVA México — Apartados](https://www.bbva.mx/personas/productos/cuentas/apartados.html) — **TODO: Verify** la fecha de publicación de la página y la funcionalidad actual.
- [Minu — Salario bajo demanda](https://www.minu.mx/salario-on-demand) — **TODO: Verify** la fecha de publicación de la página y sus términos.
- [Cetesdirecto — Ahorro recurrente](https://www.cetesdirecto.com/sites/portal/invertir-en-cetes.ahorro-recurrente) — **TODO: Verify** la fecha de publicación de la página y los términos actuales del producto.
- [Clip — Soluciones para negocios](https://www.clip.mx/soluciones) — **TODO: Verify** la disponibilidad actual de exportaciones/API.
- [Mercado Pago — descripción general del producto para negocios](https://www.mercadopago.com.mx/blog/mercado-pago-para-negocios) — **TODO: Verify** la disponibilidad actual de exportaciones/API y la fecha de publicación.

### Periodismo y comunidades

No se usa ninguna fuente periodística o de comunidades/foros como evidencia cuantitativa ni como base para la clasificación. Los informes de investigación contenían pocas anécdotas de prensa y proveedores, pero la recomendación final no depende de ellas. No se presenta ninguna anécdota comunitaria sin respaldo.

### Incertidumbres transversales antes de implementar

- **TODO: Verify** la disponibilidad y cobertura actuales en producción de API transaccionales consentidas, institución por institución.
- **TODO: Verify** la autoridad y política del socio para retrasar, desafiar o revisar una transferencia autorizada por el cliente.
- **TODO: Verify** la incidencia nacional de estafas APP, eventos intentados frente a completados, víctimas únicas, pérdida, recuperación y tiempo hasta vaciar los fondos.
- **TODO: Verify** el acceso a inteligencia de la red receptora o de beneficiarios confirmados como fraudulentos mediante acuerdos interinstitucionales lícitos.
- **TODO: Verify** los objetivos aceptables de falsos positivos, abandono, latencia y accesibilidad con usuarios y operaciones de fraude.
- **TODO: Verify** los requisitos actuales del SAT para acceso delegado, descargas masivas y manejo de credenciales antes de cualquier integración fiscal en producción.
- **TODO: Verify** si el hackatón proporciona un sandbox transaccional, créditos de nube o API específicas de los patrocinadores.
