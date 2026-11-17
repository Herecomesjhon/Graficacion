# Quiz: Replicación en PostgreSQL

**Basado en:** Arquitectura de Datos — Replicación en PostgreSQL  
**Temas:** Alta disponibilidad, escalabilidad de lecturas y sincronización en tiempo real  
**Instrucciones:** Responde sin consultar la presentación. Al final encontrarás la clave de respuestas.

---

## Parte A — Opción múltiple (1 punto c/u)

**1.** ¿Cuál es el propósito central de la replicación en PostgreSQL?

- A) Sustituir por completo los respaldos (backups)
- B) Copiar datos del servidor principal a secundarios para evitar pérdidas y repartir consultas
- C) Convertir todas las tablas a solo lectura
- D) Eliminar la necesidad de Write-Ahead Logging

**2.** En la arquitectura básica, ¿qué componente recibe escrituras y genera registros WAL?

- A) Réplica Standby
- B) Replication Slot
- C) Servidor Primario
- D) Orquestador externo (Patroni)

**3.** ¿Qué significa WAL?

- A) Write-Ahead Logging
- B) Wide Access Layer
- C) Worker Allocation List
- D) Write-After Lock

**4.** En la replicación física (streaming), ¿qué se copia?

- A) Solo cambios a nivel de filas y tablas
- B) Únicamente índices y vistas
- C) Bloques exactos de disco byte a byte
- D) Solo metadatos del catálogo

**5.** Una ventaja de la replicación lógica frente a la física es que:

- A) Obliga a usar la misma versión de PostgreSQL
- B) Copia siempre el servidor completo
- C) Permite alcance selectivo por tablas o columnas
- D) Impide escribir en cualquier tabla de la réplica

**6.** ¿Cuál es el modo de sincronización por defecto?

- A) Replicación síncrona
- B) Replicación asíncrona
- C) Replicación bidireccional
- D) Replicación lógica exclusiva

**7.** En replicación síncrona, ¿qué se garantiza principalmente?

- A) Máximo rendimiento de escritura sin latencia
- B) Cero pérdida de datos (RPO = 0)
- C) Que no haga falta red entre nodos
- D) Que la réplica acepte escrituras libres

**8.** ¿Cuál NO es un caso de uso típico de producción mencionado?

- A) Alta disponibilidad
- B) Escalabilidad de lecturas
- C) Analítica pesada
- D) Sustituir el control de concurrencia (MVCC)

**9.** ¿Qué son los Replication Slots?

- A) Espacios de disco para índices temporales
- B) Mecanismos que retienen archivos WAL hasta confirmar descarga segura
- C) Puertos de red abiertos entre nodos
- D) Tablas auxiliares para estadísticas

**10.** PostgreSQL realiza failover automático nativo sin herramientas externas.

- A) Verdadero: basta con `standby.signal`
- B) Falso: requiere orquestadores como Patroni, repmgr o pg_auto_failover
- C) Verdadero: solo en modo síncrono
- D) Falso: solo es posible con replicación lógica

**11.** ¿Cuál es la diferencia entre Switchover y Failover?

- A) Switchover es emergencia; Failover es mantenimiento planeado
- B) Switchover es intercambio ordenado por mantenimiento; Failover es promoción tras caída inesperada
- C) Ambos son idénticos
- D) Switchover solo aplica a replicación lógica

**12.** En la configuración física, ¿qué se define al enlazar la conexión de la réplica?

- A) Solo `max_connections`
- B) `primary_conninfo` y el archivo `standby.signal`
- C) Únicamente `pg_hba.conf` en la réplica
- D) Un trigger PL/pgSQL de promoción

---

## Parte B — Verdadero / Falso (1 punto c/u)

**13.** Todo cambio pasa primero por el registro WAL antes de tocar las tablas.  
**V / F**

**14.** La réplica standby en streaming físico reproduce el WAL en modo solo lectura.  
**V / F**

**15.** La replicación física exige versión idéntica de PostgreSQL y sistema operativo compatible.  
**V / F**

**16.** La replicación asíncrona espera confirmación de la réplica antes de confirmar la transacción al cliente.  
**V / F**

**17.** El Replication Lag es el desfase temporal entre la escritura en el primario y su aplicación en la réplica.  
**V / F**

**18.** WAL Archiving permite respaldo continuo para recuperación exacta en el tiempo (PITR).  
**V / F**

**19.** `pg_basebackup` se ejecuta desde el servidor secundario para clonar la base.  
**V / F**

**20.** En el primario se configura `wal_level = replica` y permisos en `pg_hba.conf`.  
**V / F**

---

## Parte C — Respuesta corta (2 puntos c/u)

**21.** Menciona **dos** beneficios del propósito central de la replicación según la presentación.

**22.** Ordena los 3 pasos del motor WAL en la arquitectura básica.

**23.** Completa la tabla mental:

| Aspecto | Física (Streaming) | Lógica |
|---|---|---|
| ¿Qué copia? | _______________ | _______________ |
| Escrituras en réplica | _______________ | _______________ |

**24.** Nombra **tres** orquestadores externos usados para failover automático.

**25.** Lista los **4 pasos** de la configuración física de una réplica.

---

## Parte D — Análisis (3 puntos c/u)

**26.** Una aplicación financiera no puede perder ni una transacción confirmada. ¿Qué modo de sincronización elegirías y por qué? ¿Qué costo operativo implica?

**27.** Tienes reportes analíticos pesados que degradan el OLTP del primario. ¿Cómo usaría la replicación para resolverlo y qué tipo (física/lógica) encaja mejor en el escenario típico de solo lectura?

**28.** El primario cae de forma inesperada. Describe la diferencia operativa entre un **failover** y un **switchover**, y qué rol juegan las herramientas externas.

---

## Clave de respuestas

### Parte A
1. **B**  
2. **C**  
3. **A**  
4. **C**  
5. **C**  
6. **B**  
7. **B**  
8. **D**  
9. **B**  
10. **B**  
11. **B**  
12. **B**

### Parte B
13. **V**  
14. **V**  
15. **V**  
16. **F** (eso describe la síncrona; la asíncrona no espera)  
17. **V**  
18. **V**  
19. **V**  
20. **V**

### Parte C
21. Continuidad ante fallos y balanceo de carga (también: evitar pérdidas / repartir consultas).  
22. 1) Primario genera WAL → 2) Transmisión WAL por red → 3) Standby reproduce WAL en solo lectura.  
23. Física: bloques byte a byte / estrictamente solo lectura. Lógica: cambios a nivel filas-tablas / permite escribir en tablas externas.  
24. Patroni, repmgr, pg_auto_failover.  
25. Preparar primario (`wal_level=replica`, `pg_hba.conf`) → `pg_basebackup` → `primary_conninfo` + `standby.signal` → iniciar réplica en lectura continua.

### Parte D (criterio)
26. Síncrona: RPO=0 / integridad total; costo = mayor latencia dependiente de la red.  
27. Desviar SELECT/reportes a réplicas (escalabilidad de lecturas / analítica pesada); típicamente física en standby de solo lectura.  
28. Failover = promoción de emergencia tras caída; Switchover = cambio ordenado por mantenimiento. PostgreSQL necesita orquestadores externos para automatizar el failover.

---

**Puntaje total:** 40 puntos  
| Rango | Calificación orientativa |
|---|---|
| 36–40 | Excelente dominio |
| 28–35 | Buen dominio |
| 20–27 | Dominio parcial — repasar diapositivas 4, 5 y 8 |
| < 20 | Repasar toda la presentación |
