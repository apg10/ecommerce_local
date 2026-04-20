# Backend review (branch codex/cloud)

## Resumen ejecutivo
El backend ha sido limpiado y migrado a una versión coherente de Django/DRF. Se eliminaron migraciones antiguas, se redefinieron los modelos simplificados y se regeneraron las migraciones, asegurando que la base de datos refleje el esquema actual.

## Cambios recientes
1. **Añadido campo `stock` a `Product`** para gestión de inventario.
2. **Corregido `PaymentSerializer`** para que acepte el campo `order` como `PrimaryKeyRelatedField`.
3. **Migraciones recreadas** desde cero (`0001_initial.py`).
4. **Pruebas** añadidas en `backend/api/tests/test_cart_order.py` para validar el flujo de carrito y la restricción de stock.
5. **Actualización de `settings.py`** para usar variables de entorno y proteger valores sensibles.

## Problemas anteriores
- Migraciones inconsistentes que describían un esquema distinto (con `Variants`, `Inventory`, etc.).
- `PaymentSerializer` tenía `order` como `StringRelatedField`, impidiendo crear pagos a través de API.
- Ausencia de pruebas que cubrieran la lógica de stock.

## Próximos pasos recomendados
- Revisar la lógica de creación de pedidos y pagos, especialmente la transición de estado a `paid`.
- Implementar tests adicionales para la creación de pedidos y la gestión de inventario.
- Añadir tests de integración para el flujo completo de checkout.
- Reforzar la seguridad de la configuración (secret key, debug, allowed hosts).
- Documentar el esquema de la base de datos y los endpoints disponibles.

---

### Detalles técnicos
- Migraciones: `0001_initial.py` incluye modelos `Brand`, `Category`, `Product` (con `stock`), `Customer`, `CartItem`, `Cart`, `Order`, `OrderItem`, `Payment`.
- `backend/api/serializers.py` actualizados con campos legibles y editables.
- `backend/api/views.py` actualizado con validación de stock y creación de `CartItem`.
- `backend/core/models.py` alineado con el esquema de migraciones.
- Tests cubren la adición de productos al carrito y la respuesta cuando el stock es insuficiente.
