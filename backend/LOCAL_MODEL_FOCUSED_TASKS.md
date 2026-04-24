# Tareas ultra-enfocadas para modelo local (backend)

Objetivo: maximizar calidad del output dividiendo el trabajo en micro-tareas con alcance estricto.

## Reglas para cada iteración
- 1 tarea = 1 commit.
- Máximo 2 archivos tocados por tarea (salvo migraciones).
- No mezclar: bugfix + refactor + tests en la misma iteración.
- Siempre incluir criterio de éxito verificable.

---

## Tarea 1 — Desbloquear sintaxis de `core/utils.py`
**Alcance:** solo `backend/core/utils.py`.

**Prompt para tu modelo local:**
"Corregí únicamente errores de sintaxis en backend/core/utils.py.
No cambies comportamiento funcional.
No toques ningún otro archivo."

**Éxito:**
- `python -m compileall backend/core/utils.py` pasa.

---

## Tarea 2 — Corregir import de stock helper
**Alcance:** solo `backend/api/views.py`.

**Prompt para tu modelo local:**
"En backend/api/views.py, corregí el import de has_sufficient_stock para que apunte al módulo existente.
No hagas cambios adicionales."

**Éxito:**
- `python -m compileall backend/api/views.py` pasa.

---

## Tarea 3 — Agregar `stock` al modelo `Product`
**Alcance:**
- `backend/core/models.py`
- nueva migración en `backend/core/migrations/`

**Prompt para tu modelo local:**
"Agregá campo stock no negativo a Product en backend/core/models.py y creá migración.
No toques views ni serializers en esta tarea."

**Éxito:**
- `python manage.py makemigrations --check` no reporta cambios pendientes.
- `python manage.py migrate` ejecuta sin errores.

---

## Tarea 4 — Alinear helper de stock con campo real
**Alcance:** solo `backend/core/utils.py`.

**Prompt para tu modelo local:**
"Actualizá has_sufficient_stock para usar explícitamente Product.stock (sin getattr fallback por campo faltante).
No toques otros módulos."

**Éxito:**
- helper usa campo real y compila.

---

## Tarea 5 — Ajustar tests de carrito a inventario real
**Alcance:** solo `backend/api/tests.py`.

**Prompt para tu modelo local:**
"En backend/api/tests.py, ajustá/creá tests de carrito para validar stock real.
Incluir: caso suficiente, caso insuficiente y borde exacto."

**Éxito:**
- `python manage.py test api.tests.CartViewTests` verde.

---

## Tarea 6 — Serializer de escritura para Payment
**Alcance:**
- `backend/api/serializers.py`
- `backend/api/views.py`

**Prompt para tu modelo local:**
"Implementá serializer de escritura para crear Payment aceptando order por PK.
Usá ese serializer en PaymentCreateView sin romper el serializer de lectura actual."

**Éxito:**
- Crear payment por API con `order` ID funciona (201).
- payload inválido devuelve 400.

---

## Tarea 7 — Definir política de orden anónima
**Alcance:**
- `backend/api/views.py`
- `backend/api/serializers.py` (si aplica)

**Prompt para tu modelo local:**
"Elegí y aplicá una política explícita para OrderCreateView:
A) exigir autenticación, o
B) soportar guest checkout de forma consistente con el modelo.
No mezclar optimizaciones de performance en esta tarea."

**Éxito:**
- comportamiento documentado y consistente con modelo.
- tests de creación de orden pasan.

---

## Tarea 8 — Validación de cantidad en carrito
**Alcance:**
- `backend/api/views.py`
- `backend/api/tests.py`

**Prompt para tu modelo local:**
"En CartView.post, validar quantity inválida (0, negativa, no numérica) con 400.
Agregar tests exactos para esos tres casos."

**Éxito:**
- tests de inputs inválidos verdes.

---

## Tarea 9 — Validar stock acumulado en carrito
**Alcance:**
- `backend/api/views.py`
- `backend/api/tests.py`

**Prompt para tu modelo local:**
"En CartView.post, validar contra cantidad acumulada (existente + nueva), no solo nueva.
Agregar test de doble agregado que excede en segundo paso."

**Éxito:**
- caso acumulado bloquea correctamente con 400.

---

## Tarea 10 — Optimización de listados (N+1)
**Alcance:** solo querysets en `backend/api/views.py`.

**Prompt para tu modelo local:**
"Aplicá select_related/prefetch_related en endpoints de listado con serializers anidados.
No cambies contratos de respuesta."

**Éxito:**
- respuesta igual funcionalmente.
- menor cantidad de queries en listados.

---

## Orden recomendado
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

No avanzar de tarea sin validar la anterior.
