# Informe general backend (para ejecutar con tu modelo local paso a paso)

## Estado actual
El backend tiene bloqueadores de ejecución y problemas funcionales en flujo de carrito/pedido/pago.
La prioridad correcta es: primero desbloquear arranque/imports, luego consistencia de datos, luego creación de recursos y finalmente optimización/calidad.

## Fase 0 — Preparación local (antes de tocar código)
Objetivo: confirmar línea base.

1. Crear/activar entorno virtual.
2. Instalar dependencias: `pip install -r backend/requirements.txt`.
3. Ejecutar:
   - `python -m compileall backend/api backend/core backend/ecommerce`
   - `cd backend && python manage.py test`
4. Guardar salida en un archivo para comparar después.

Criterio de salida:
- Tienes un baseline de errores reproducible.

---

## Fase 1 — Bloqueadores de arranque
### Problema 1: `core/utils.py` tiene sintaxis inválida
- Hay símbolos `+` incrustados en el archivo.
- Impacto: rompe import/ejecución.

### Problema 2: import roto en `api/views.py`
- `from .utils import has_sufficient_stock` pero no existe `api/utils.py`.
- El helper está en `core/utils.py`.

### Tarea para tu modelo local
Prompt sugerido:
"Corregí solo errores de arranque en backend.
1) limpiá backend/core/utils.py (sin cambiar lógica, solo sintaxis válida).
2) en backend/api/views.py corregí el import de has_sufficient_stock para que apunte al módulo real.
No toques nada más."

Validación:
- `python -m compileall backend/api backend/core backend/ecommerce` debe pasar.

---

## Fase 2 — Consistencia de inventario
### Problema 3: se usa `stock` pero el modelo `Product` no lo define
- Tests crean `Product(..., stock=5)`.
- Helper de stock usa `getattr(product, "stock", 0)`.
- Modelo y migración no tienen campo `stock`.

### Tarea para tu modelo local
Prompt sugerido:
"Implementá consistencia de inventario.
- Agregá `stock` en `Product` (entero no negativo).
- Creá migración correspondiente.
- Exponé stock donde sea necesario para lectura interna/API según diseño actual.
- Ajustá helper/tests para usar el campo real (sin hacks con getattr por campo faltante).
Solo tocar archivos relacionados a inventario."

Validación:
- `python manage.py makemigrations --check`
- `python manage.py migrate`
- tests de carrito pasan.

---

## Fase 3 — Serializers de escritura (orders/payments)
### Problema 4: `OrderCreateView` + `OrderSerializer`
- `OrderSerializer` está orientado a lectura (`customer = StringRelatedField`, `items` readonly).
- En creación anónima se intenta `customer=None` pero `Order.customer` es obligatorio.

### Problema 5: `PaymentSerializer` no writable para `order`
- `order = StringRelatedField()` impide crear pagos desde payload con id de orden.

### Tarea para tu modelo local
Prompt sugerido:
"Separá serializers read/write para Order y Payment.
- Crear serializers de escritura con campos PK relacionados.
- Ajustar views de creación para usar serializer de escritura.
- Definir explícitamente política para usuario anónimo en creación de orden:
  a) requerir auth, o
  b) soportar guest checkout con modelo/campo consistente.
No optimices performance aún."

Validación:
- tests de create order/payment (happy path + errores de validación).
- status codes correctos (400/401/201 según caso).

---

## Fase 4 — Reglas de carrito y stock real
### Riesgo funcional
- Actualmente solo se valida stock contra `quantity` nueva, no necesariamente contra cantidad acumulada en carrito.

### Tarea para tu modelo local
Prompt sugerido:
"En CartView.post, validar stock contra cantidad total resultante (existente + nueva).
Si excede stock, devolver 400 claro.
Agregar tests para:
1) agregar en dos pasos y exceder en el segundo,
2) borde exacto de stock,
3) quantity inválida (0, negativa, no numérica)."

Validación:
- tests de edge cases de carrito verdes.

---

## Fase 5 — Performance y calidad
### Mejoras recomendadas
- `select_related`/`prefetch_related` en listados con relaciones.
- Endurecer permisos por endpoint (ahora default IsAuthenticated + overrides AllowAny).
- Manejo de errores y validaciones de entrada más explícitas en vistas.

### Tarea para tu modelo local
Prompt sugerido:
"Optimización y limpieza:
- aplicar select_related/prefetch_related en endpoints de listado con nested serializers,
- validar input en CartView con serializer de entrada,
- mantener compatibilidad de respuesta.
Sin cambiar contratos públicos salvo errores más claros."

Validación:
- tests existentes + nuevos pasan.
- revisar cantidad de queries en endpoints críticos (si usan django-debug-toolbar o assertNumQueries).

---

## Fase 6 — Cierre y hardening
1. Verificar settings por entorno (dev/test/prod).
2. Añadir `.env.example` backend con variables mínimas.
3. Ejecutar suite completa y smoke manual de endpoints.
4. Abrir PR final con changelog por fases.

---

## Orden estricto recomendado (no saltar)
1) Fase 1
2) Fase 2
3) Fase 3
4) Fase 4
5) Fase 5
6) Fase 6

---

## Checklist rápido de aceptación final
- [ ] compileall sin errores
- [ ] migraciones al día
- [ ] tests backend verdes
- [ ] create order/payment funcional
- [ ] cart + stock consistente
- [ ] sin regresiones en endpoints públicos
