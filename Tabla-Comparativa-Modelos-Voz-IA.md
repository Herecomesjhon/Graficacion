# Tabla comparativa: modelos y plataformas de voz por IA

Comparativa para sistemas conversacionales en tiempo real (ASR + diálogo + TTS), orientada a un proyecto que integra **Reconocimiento de Voz + IoT + Sistema Operativo**.

---

## Tabla principal

| Plataforma / Modelo | Tipo | Costo aproximado | Latencia | Calidad / expresividad | Hardware | Mejor para |
|---|---|---|---|---|---|---|
| **ElevenLabs** (Flash / Turbo) | Comercial (API) | Free: ~10k chars/mes. Planes desde ~$5/mes. ~$0.10–$0.20 / 1k chars | Muy baja (~75 ms Flash) | Referencia en naturalidad y emoción | Solo internet (cloud) | Demo final con máxima calidad |
| **Deepgram Aura** | Comercial (API) | ~$0.015–$0.030 / 1k chars. Suele incluir ~$200 crédito inicial | Mínima (prioriza TTFA) | Muy buena; menos expresiva que ElevenLabs | Solo internet (cloud) | Prototipos y producción con buen costo-beneficio |
| **Cartesia** (Sonic / Ink) | Comercial (API) | Free: ~10k créditos/mes. Desde ~$5/mes. ~$0.03–$0.05 / 1k chars | Muy alta velocidad + turn-taking | Alta, optimizada para streaming | Solo internet (cloud) | Diálogo en tiempo real con pocos tiempos muertos |
| **OpenAI Realtime** (GPT-4o Audio) | Comercial (nativo audio) | ~$0.06/min entrada + ~$0.24/min salida | Fluida (pipeline unificado) | Muy natural; entiende tono | Solo internet (cloud) | Arquitectura simple (ASR+LLM+TTS en un solo API) |
| **Piper TTS** | Open source | $0 (local) | Casi instantánea en CPU | Buena / funcional (no “actor”) | Raspberry Pi 4/5, CPU | IoT y placas sin GPU |
| **Kokoro** (v1.0 / 82M) | Open source (Apache 2.0) | $0 (local) | Baja con pocos recursos | Casi comercial, modelo compacto | CPU / poca VRAM | PC local sin presupuesto de API |
| **Fish Speech** (v1.5) | Open source | $0 local o arriendo de GPU | Baja con GPU | Muy alta, multilingüe | GPU ≥4–8 GB VRAM | Calidad comercial en despliegue propio |
| **CosyVoice** (FunAudioLLM) | Open source | $0 local o arriendo de GPU | Ultrabaja en streaming | Alta + control de estilo con muestras cortas | GPU recomendada | Clonado / estilo y streaming local |

---

## Comparativa por criterio

### Costo

| Opción | Nivel de gasto | Nota |
|---|---|---|
| Piper, Kokoro, Fish Speech, CosyVoice | $0 en API | Pagan en hardware / tiempo de setup |
| Deepgram Aura | Bajo–medio | Mejor relación costo-beneficio + crédito inicial |
| Cartesia | Bajo–medio | Similar a Deepgram |
| ElevenLabs | Medio–alto | Sube rápido con alto volumen |
| OpenAI Realtime | Alto | Ideal por simplicidad, caro si queda escuchando |

### Utilidad en IoT + SO + voz

| Escenario | Recomendación | Motivo |
|---|---|---|
| Raspberry Pi / Jetson / mini PC sin GPU | **Piper TTS** | Ligero, CPU-only, sin dependencia de internet |
| PC/laptop con GPU (RTX) o servidor propio | **Kokoro** o **Fish Speech** | Calidad alta sin pagar API |
| Prototipo universitario con internet y poco tiempo | **Deepgram** (crédito ~$200) | Rápido de integrar y barato de probar |
| Demo de presentación con voz “premium” | **ElevenLabs Flash** | Máxima naturalidad en poco tiempo |
| Quieren un solo API (ASR + cerebro + TTS) | **OpenAI Realtime** | Menos piezas que conectar; mayor costo |

---

## Resumen de decisión

1. **Presupuesto $0 + GPU local** → Kokoro o Fish Speech  
2. **Placa limitada (Raspberry Pi / sin GPU) para IoT** → Piper TTS  
3. **Mejor calidad sin montar hardware, con internet** → Deepgram (crédito gratis) o ElevenLabs (capa free / demo final)

---

## Notas técnicas rápidas

- **ElevenLabs:** marcas en texto para pausas, énfasis y emoción; línea Flash pensada para agentes.
- **Deepgram Aura:** enfocada en call centers / agentes; prioridad en tiempo hasta el primer audio.
- **Cartesia:** predicción de fin de turno (*turn-taking*) nativa para reducir silencios.
- **OpenAI Realtime:** evita pipeline ASR → LLM → TTS separado; audio nativo de extremo a extremo.
- **Fish Speech / CosyVoice:** calidad open source de punta; necesitan GPU para latencia conversacional.
- **Piper / Kokoro:** opciones prácticas para edge e IoT cuando el costo de API o la red no son viables.
