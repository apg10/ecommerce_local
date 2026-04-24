# Project Context (fuente de verdad compartida)

Este archivo guarda decisiones estables del proyecto para sincronizar trabajo entre cloud/local.
Actualizar solo cuando cambie arquitectura, convenciones o reglas de negocio.

## 1) Producto y alcance
- Proyecto: ecommerce_local
- Stack principal: Django + DRF (backend), frontend separado.
- Alcance actual: estabilizar backend (carrito, órdenes, pagos, inventario).

## 2) Arquitectura acordada
- Backend en `backend/`.
- Apps principales:
  - `core`: modelos y utilidades de dominio.
  - `api`: serializers, views, rutas.
- Regla: separar serializers de lectura/escritura cuando el endpoint lo requiera.

## 3) Convenciones de desarrollo
- Trabajar por micro-tareas enfocadas (1 tarea = 1 commit).
- No mezclar backend/frontend/tests en una misma iteración.
- Commits con prefijos: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`.

## 4) Reglas de calidad backend
- Validar integridad de datos en modelos/serializers.
- Evitar N+1 con `select_related` / `prefetch_related` en listados.
- Mantener permisos explícitos por endpoint.
- Mantener mensajes de error claros y consistentes.

## 5) Entornos y configuración
- `settings.py` orientado a variables de entorno para valores sensibles y hosts.
- Validación final siempre en local antes de merge.

## 6) Decisiones abiertas (pendientes)
- Política de creación de órdenes anónimas (forzar auth vs guest checkout formal).
- Modelo final de inventario y decremento de stock.

## 7) Cómo usar este archivo
- Cloud y local deben leer este archivo al iniciar una tarea.
- Si una decisión cambia, actualizar este archivo en el mismo PR donde se implementa.
