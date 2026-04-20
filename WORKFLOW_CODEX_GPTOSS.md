# Workflow recomendado para trabajar con Codex/GPT-OSS en repo compartido (GitHub)

Este flujo está pensado para usar Codex como copiloto de ejecución en remoto, y ejecutar validaciones finales en local.

## 1) División clara de responsabilidades
- Codex (remoto):
  - lectura de código
  - propuestas y cambios acotados
  - refactors mecánicos
  - documentación técnica
  - preparación de commits/PR con contexto
- Equipo local:
  - correr app completa
  - pruebas E2E/integración
  - QA funcional
  - validaciones de entorno real (secrets, infra, despliegue)

## 2) Ciclo de trabajo por tarea (recomendado)
1. Crear issue corto en GitHub (objetivo + criterios de aceptación).
2. Abrir rama por tarea (`feature/...`, `fix/...`).
3. Pedir a Codex una sola cosa por iteración:
   - analizar
   - cambiar código
   - o escribir tests
4. Codex entrega commit pequeño + PR descriptivo.
5. En local: `pull`, correr tests/proyecto, validar funcionalidad.
6. Si falla algo: devolver feedback concreto (archivo, error, comportamiento esperado).
7. Repetir hasta verde, luego merge.

## 3) Prompting que mejor funciona
Usar siempre este formato:
- Contexto: qué módulo y por qué.
- Alcance: qué sí y qué no tocar.
- Restricciones: estilo, arquitectura, compatibilidad.
- Definición de terminado: comandos/checks esperados.

Ejemplo:
"Revisa backend/api/views.py. Solo corrige validación de stock en CartView.
No toques frontend ni settings. Entregado cuando pasen tests de api/tests.py::CartViewTests."

## 4) Estrategia de ramas y PRs
- PRs chicos (ideal: 1 problema = 1 PR).
- Commits atómicos con prefijos (`feat:`, `fix:`, `refactor:`, `docs:`).
- Evitar mezclar refactor + feature + tests grandes en el mismo PR.
- Plantilla de PR con:
  - problema
  - cambio realizado
  - riesgo/impacto
  - cómo validar localmente

## 5) Contrato de validación local
Definir un checklist fijo para cada PR:
- instalar deps
- migraciones
- tests unitarios relevantes
- smoke test manual

Plantilla sugerida de validación local:
1. `cd backend`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py test`
5. Probar endpoint(s) tocados con curl/Postman.

## 6) Cómo dar feedback para que Codex mejore rápido
Cuando algo no sirva, responder con:
- Qué esperabas exactamente.
- Qué ocurrió (error/log).
- Dónde ocurrió (archivo/línea/comando).
- Qué límite respetar en la próxima iteración.

## 7) Convenciones mínimas de equipo
- Un AGENTS.md vivo y corto con reglas reales del proyecto.
- Definition of Done por tipo de cambio (backend/frontend/docs).
- No mergear PR con checks rojos.
- Si el entorno remoto no tiene dependencias, marcarlo explícitamente en PR.

## 8) Recomendación práctica para su setup actual
Como ustedes dirigen en Codex y ejecutan en local:
- usen Codex para análisis + cambios + commits pequeños,
- y dejen la verificación final siempre al entorno local.

Eso les da velocidad sin sacrificar confianza en ejecución real.
