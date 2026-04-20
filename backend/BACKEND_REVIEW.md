# Backend review (branch feature/backend-review-notes)

## Resumen ejecutivo
Se revisó el backend Django/DRF y se encontraron bloqueadores de ejecución y varios problemas de diseño en serialización/creación de recursos.

## Hallazgos críticos
1. Error de sintaxis en core/utils.py.
   El archivo contiene caracteres + al inicio de varias líneas (restos de diff), lo cual rompe la carga del módulo.

2. Import incorrecto en api/views.py.
   Se importa has_sufficient_stock desde .utils, pero no existe api/utils.py. El helper sí existe en core/utils.py.

3. Inconsistencia de inventario (stock).
   La lógica y tests usan product.stock, pero el modelo Product no define este campo. Resultado: la validación de stock es inconsistente y/o siempre falla.

## Hallazgos altos
4. Creación de órdenes no autenticadas falla por integridad.
   OrderCreateView intenta guardar customer=None para usuarios anónimos, pero Order.customer es obligatorio.

5. PaymentSerializer no es apto para escritura.
   El campo order es StringRelatedField (solo lectura), pero PaymentCreateView espera crear pagos desde request.data. Falta un campo writable para order (ej. PrimaryKeyRelatedField).

## Hallazgos medios
6. Posible N+1 en listados.
   Los listados de productos/órdenes serializan relaciones (brand, category, items) sin select_related/prefetch_related.

7. Configuración insegura de entorno.
   DEBUG=True y SECRET_KEY=dev están hardcodeados.

## Recomendaciones mínimas (orden sugerido)
1. Corregir core/utils.py y alinear import en api/views.py.
2. Definir estrategia real de inventario (stock en modelo + migración + serializer/tests).
3. Separar serializers de lectura/escritura para Order y Payment.
4. Ajustar reglas para orden anónima (guest checkout) o requerir autenticación explícita.
5. Optimizar querysets con select_related/prefetch_related.
6. Externalizar SECRET_KEY/DEBUG mediante variables de entorno.
