# Tabla comparativa: modelos y plataformas de voz por IA

Comparativa por **costo y utilidad** para sistemas conversacionales en tiempo real (ASR + diálogo + TTS), orientada a un proyecto que integra **Reconocimiento de Voz + IoT + Sistema Operativo**.

El enfoque cambia según prioricen: rapidez de desarrollo, bajo presupuesto o ejecución local (Raspberry Pi / servidor propio).

---

## Tabla principal

| Plataforma / Modelo | Tipo | Costo aproximado | Latencia | Calidad / expresividad | Hardware | Mejor para |
|---|---|---|---|---|---|---|
| **ElevenLabs** (Flash v2.5 / Turbo) | Comercial (API) | Free: ~10k chars/mes. Planes desde ~$5/mes. ~$0.10–$0.20 / 1k chars | ~75 ms (Flash) | Máxima naturalidad y emoción | Solo internet (cloud) | Demo final con máxima calidad |
| **Deepgram Aura** | Comercial (API) | ~$0.015–$0.030 / 1k chars. Suele incluir ~$200 crédito inicial | Mínima (prioriza TTFA) | Muy buena; menos expresiva que ElevenLabs | Solo internet (cloud) | Prototipos y producción con buen costo-beneficio |
| **Cartesia** (Sonic) | Comercial (API) | Free: ~10k créditos/mes. Desde ~$5/mes. ~$0.03–$0.05 / 1k chars | Muy alta + turn-taking | Alta, optimizada para streaming | Solo internet (cloud) | Diálogo en tiempo real con pocos tiempos muertos |
| **OpenAI Realtime** (GPT-4o Audio) | Comercial (nativo audio) | ~$0.06/min entrada + ~$0.24/min salida | Fluida (pipeline unificado) | Muy natural; entiende tono | Solo internet (cloud) | Arquitectura simple (ASR+LLM+TTS en un solo API) |
| **Piper TTS** | Open source | $0 (local) | Casi instantánea en CPU | Buena / funcional (no “actor”) | Raspberry Pi 4/5, CPU | IoT y placas sin GPU |
| **Kokoro** (v1.0 / 82M) | Open source (Apache 2.0) | $0 (local) | Baja con pocos recursos | Casi comercial, modelo compacto | CPU / poca VRAM | PC local sin presupuesto de API |
| **Fish Speech** (v1.5) | Open source | $0 local o arriendo de GPU | Baja con GPU | Muy alta, multilingüe | GPU ≥4–8 GB VRAM | Calidad comercial en despliegue propio |
| **CosyVoice** (FunAudioLLM) | Open source | $0 local o arriendo de GPU | Ultrabaja en streaming | Alta + control de estilo con muestras cortas | GPU recomendada | Clonado / estilo y streaming local |

---

## 1. Soluciones comerciales (pago por uso)

Las más fáciles y rápidas de integrar (solo consumen una API). Ideales si no quieren preocuparse por la potencia de hardware del equipo donde corre el sistema.

### ElevenLabs (Flash v2.5 / Turbo)

- **Costo:** Capa gratuita limitada (~10,000 caracteres al mes). Planes desde ~$5 USD/mes hasta empresariales (~$0.10–$0.20 USD por cada 1,000 caracteres).
- **Utilidad:** Máxima calidad de voz y emociones. Flash ~75 ms de latencia; la conversación se siente muy humana. En alto volumen o pruebas constantes el costo sube rápido.

### Deepgram (Aura)

- **Costo:** ~$0.015 a $0.030 USD por cada 1,000 caracteres. Suele incluir ~$200 USD de crédito inicial (muy útil para proyectos universitarios o prototipos).
- **Utilidad:** Excelente relación costo-beneficio para agentes de voz. Un poco menos expresiva que ElevenLabs, pero con velocidad de respuesta en tiempo real superior. El crédito gratuito permite probar sin gastar.

### Cartesia (Sonic)

- **Costo:** Similar a Deepgram: capa gratuita ~10,000 créditos/mes y planes desde ~$5 USD/mes (~$0.03–$0.05 USD por cada 1,000 caracteres).
- **Utilidad:** Muy útil cuando importa detectar rápido cuándo el usuario dejó de hablar (*turn-taking*) para responder al instante.

### OpenAI Realtime API (GPT-4o Audio / Realtime)

- **Costo:** La opción más cara (~$0.06 USD/minuto de entrada y ~$0.24 USD/minuto de salida).
- **Utilidad:** Une reconocimiento de voz + LLM + TTS en un solo paso y entiende el tono. Ideal por simplicidad de arquitectura; costosa si queda escuchando todo el tiempo.

---

## 2. Modelos open source / locales ($0 en API)

Si el equipo de **SO** e **IoT** monta todo en una PC dedicada, servidor propio o Raspberry Pi, eliminan el pago por suscripción. Requieren buen hardware (sobre todo GPU) si buscan velocidad.

### Piper TTS (IoT / Linux)

- **Costo:** Totalmente gratis (open source).
- **Utilidad:** Extremadamente ligero y rápido. Corre solo con CPU incluso en Raspberry Pi 4 o 5, con latencia casi instantánea. No suena como “actor de doblaje”, pero para un asistente IoT de comandos en tiempo real es la opción más práctica y estable.

### Kokoro (v1.0 / 82M)

- **Costo:** Totalmente gratis (Apache 2.0).
- **Utilidad:** Modelo ultracompacto (82M parámetros) que suena casi al nivel de modelos comerciales pesados, con pocos recursos y baja latencia.

### Fish Speech (v1.5) / CosyVoice

- **Costo:** $0 en máquina propia, o barato si arriendan GPU en la nube.
- **Utilidad:** Calidad comercial en código abierto. Necesitan GPU con al menos ~4–8 GB VRAM (p. ej. RTX 3050+) para responder en tiempo real sin esperas largas.

---

## Comparativa por criterio

### Costo

| Opción | Nivel de gasto | Nota |
|---|---|---|
| Piper, Kokoro, Fish Speech, CosyVoice | $0 en API | Pagan en hardware / tiempo de setup |
| Deepgram Aura | Bajo–medio | Mejor relación costo-beneficio + crédito inicial |
| Cartesia | Bajo–medio | Similar a Deepgram |
| ElevenLabs | Medio–alto | Sube rápido con alto volumen |
| OpenAI Realtime | Alto | Ideal por simplicidad; caro si queda escuchando |

### Utilidad en IoT + SO + voz

| Escenario | Recomendación | Motivo |
|---|---|---|
| Raspberry Pi / Jetson / mini PC sin GPU | **Piper TTS** | Ligero, CPU-only, sin dependencia de internet |
| PC/laptop con GPU (RTX) o servidor propio | **Kokoro** o **Fish Speech** | Calidad alta sin pagar API |
| Prototipo universitario con internet y poco tiempo | **Deepgram** (crédito ~$200) | Rápido de integrar y barato de probar |
| Demo de presentación con voz “premium” | **ElevenLabs Flash** | Máxima naturalidad en poco tiempo |
| Quieren un solo API (ASR + cerebro + TTS) | **OpenAI Realtime** | Menos piezas que conectar; mayor costo |

---

## Resumen: ¿Cuál les conviene elegir?

1. **Presupuesto $0 y corre en PC con GPU (laptop RTX) o servidor:** Kokoro o Fish Speech.
2. **Placa limitada (Raspberry Pi / Jetson / mini PC sin GPU) para IoT:** Piper TTS — no se traba, no gasta internet y responde al milisegundo.
3. **Mejor calidad sin montar hardware, con internet:** Deepgram (~$200 de crédito gratis para desarrollo y presentación) o capa gratuita de ElevenLabs solo para la demo final.
