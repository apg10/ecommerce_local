# proyecto_context.md

## 1. Resumen del proyecto

Este proyecto es un e-commerce para una tienda física de perfumes y productos similares en Colombia.

Actualmente el negocio vende principalmente por WhatsApp. El objetivo del sistema es transformar esa operación manual en una experiencia de compra digital rápida, confiable y fácil de operar internamente.

El sistema debe permitir que el cliente:
- descubra productos rápido;
- compre sin fricción;
- pague en línea;
- elija entrega o recogida;
- reciba confirmación clara de su pedido.

El sistema también debe permitir que el negocio:
- gestione pedidos desde un panel administrativo;
- controle inventario;
- procese pagos;
- prepare órdenes rápido;
- gestione despachos;
- reduzca dependencia de WhatsApp como canal operativo.

Este no es solo un catálogo web. Es una plataforma de venta + operación para una tienda de perfumes.

---

## 2. Objetivo principal del producto

Construir una tienda online mobile-first para perfumes que permita vender de forma rápida y profesional, con foco en:

1. compra rápida desde celular;
2. checkout simple;
3. integración con PayU;
4. integración futura con mensajería en Colombia;
5. panel administrativo sólido;
6. operación interna clara y trazable.

---

## 3. Contexto de negocio

### Situación actual
- La tienda existe físicamente.
- Gran parte de las ventas se gestionan por WhatsApp.
- El proceso actual probablemente depende de conversaciones manuales, confirmaciones manuales y coordinación manual de pedidos.

### Problema actual
- vender por WhatsApp no escala bien;
- genera fricción para el cliente;
- consume tiempo del negocio;
- dificulta trazabilidad;
- puede generar errores en pedidos, pagos y entregas.

### Oportunidad
Un e-commerce bien diseñado puede:
- profesionalizar la marca;
- aumentar conversión;
- reducir carga operativa;
- centralizar pedidos;
- permitir crecimiento ordenado.

---

## 4. Tipo de experiencia que se quiere construir

La experiencia debe ser:

- **mobile-first**;
- **rápida**;
- **limpia**;
- **premium pero simple**;
- **orientada a conversión**;
- **con baja fricción**;
- **fácil de operar desde el admin**.

El usuario no debe sentirse “llenando un sistema”.
Debe sentir que entra, encuentra, compra y listo.

---

## 5. Perfil del cliente final

### Cliente principal
Persona que quiere comprar perfumes o productos relacionados desde su celular, normalmente llegando desde:
- WhatsApp;
- Instagram;
- recomendación directa;
- tráfico local o de marca.

### Qué espera
- ver productos rápido;
- identificar precio, tamaño y disponibilidad;
- confiar en que el producto es original;
- pagar fácil;
- saber cuándo llega;
- no perder tiempo.

### Qué lo frena
- procesos largos;
- registro obligatorio;
- formularios pesados;
- páginas lentas;
- información incompleta;
- checkout confuso;
- desconfianza en el pago.

---

## 6. Objetivos UX/UI

El diseño debe priorizar:

1. **descubrimiento rápido de producto**
   - búsqueda visible;
   - categorías claras;
   - filtros útiles;
   - productos destacados bien presentados.

2. **página de producto fuerte**
   - imágenes limpias;
   - precio claro;
   - tamaño/variantes;
   - stock;
   - beneficios;
   - confianza.

3. **checkout sin fricción**
   - guest checkout;
   - pocos pasos;
   - datos mínimos;
   - costos claros;
   - botón de pago visible.

4. **confianza**
   - producto original;
   - pagos seguros;
   - tiempos de entrega;
   - políticas claras;
   - soporte visible.

5. **operación rápida**
   - pedido entra al admin listo para ser procesado;
   - estado de pago claro;
   - estado del pedido claro;
   - integración de despacho desacoplada.

---

## 7. Alcance del MVP

### Incluido en MVP

#### Storefront / cliente
- home page
- listado de productos
- categorías
- búsqueda
- filtros básicos
- página de producto
- carrito
- checkout como invitado
- selección de método de entrega
- integración con PayU
- confirmación de orden
- página básica de seguimiento del pedido
- páginas informativas básicas (contacto, envíos, cambios, privacidad)

#### Administrativo
- login admin
- dashboard básico
- gestión de pedidos
- gestión de productos
- gestión de categorías
- gestión de marcas
- gestión de inventario
- gestión de clientes
- visualización de pagos
- visualización de envíos
- actualización de estados de pedido
- cupones/promociones básicas
- reportes básicos

#### Operación
- flujo de pedido trazable
- control de stock por variante/SKU
- separación de estados de pago y estados de pedido
- soporte para entrega o recogida en tienda
- estructura preparada para integración con mensajería

---

## 8. Fuera de alcance por ahora

No construir en la primera fase:
- app nativa móvil;
- programa de puntos complejo;
- recomendaciones con IA;
- reseñas avanzadas;
- marketplace multi-vendedor;
- personalización compleja de producto;
- automatizaciones muy avanzadas de CRM;
- multi-warehouse complejo;
- internacionalización multi-país.

El enfoque es un **MVP sólido y vendible**, no una plataforma infinita desde el día uno.

---

## 9. Stack propuesto

### Backend
- Python
- Django
- Django REST Framework

### Frontend
- React
- Vite
- TypeScript

### UI
- Tailwind CSS
- componentes reutilizables y consistentes
- diseño responsive mobile-first

### Base de datos
- PostgreSQL

### Tareas asíncronas / background jobs
- Celery
- Redis

### Almacenamiento de imágenes
- S3 compatible o almacenamiento equivalente

### Autenticación
- admin con autenticación segura
- storefront sin login obligatorio para comprar
- cuenta de cliente opcional, no obligatoria en MVP

### Pagos
- PayU

### Envíos
- integrar mediante una capa abstracta de shipping para poder cambiar proveedor sin reescribir la lógica del sistema

### Infraestructura
- Docker
- variables de entorno bien separadas
- entornos local / staging / production

---

## 10. Justificación de stack

Se elige esta arquitectura porque:
- Django acelera el desarrollo del backend administrativo y reglas de negocio;
- DRF permite exponer una API limpia para frontend y futuras integraciones;
- React + Vite permite construir un frontend moderno, rápido y mantenible;
- PostgreSQL ofrece estructura robusta para catálogo, pedidos, pagos e inventario;
- Celery + Redis permiten manejar webhooks, notificaciones y procesos desacoplados;
- el sistema queda preparado para escalar sin sobrecomplicar el MVP.

---

## 11. Principios de arquitectura

1. **Backend como fuente de verdad**
   - pagos, stock, pedidos, envíos y estados se validan en backend.

2. **Frontend desacoplado**
   - el frontend consume API y no debe contener lógica crítica de negocio.

3. **Integraciones desacopladas**
   - PayU y shipping deben implementarse detrás de servicios/adapters.

4. **Estados explícitos**
   - pago y pedido no son lo mismo.
   - no mezclar estados operativos con estados financieros.

5. **Diseño para operación real**
   - cada flujo debe pensarse también desde el admin, no solo desde el cliente.

---

## 12. Módulos principales del sistema

### 12.1 Storefront
Responsable de la experiencia de compra del cliente.

Debe incluir:
- home
- catálogo
- búsqueda
- filtros
- página de producto
- carrito
- checkout
- confirmación
- tracking básico

### 12.2 Catálogo
Responsable de:
- productos
- categorías
- marcas
- variantes
- imágenes
- atributos
- precios
- promociones

### 12.3 Checkout
Responsable de:
- datos del cliente
- dirección o recogida
- resumen de compra
- costos
- creación de orden
- conexión con pago

### 12.4 Pagos
Responsable de:
- iniciar pago
- registrar transacción
- recibir confirmación
- actualizar estado de pago
- manejar errores o rechazos
- mantener trazabilidad

### 12.5 Pedidos
Responsable de:
- crear la orden
- almacenar items
- asociar cliente y dirección
- separar estado de pago y estado operativo
- permitir seguimiento interno

### 12.6 Inventario
Responsable de:
- stock por SKU/variante
- disponibilidad
- alertas de bajo stock
- evitar venta sin inventario

### 12.7 Envíos
Responsable de:
- tipo de entrega
- costo de envío
- guía
- tracking
- actualización de estado
- integración desacoplada con proveedor logístico

### 12.8 Administrativo
Responsable de:
- pedidos
- productos
- inventario
- clientes
- pagos
- promociones
- envíos
- reportes

---

## 13. Modelo conceptual de entidades

Entidades principales esperadas:

- Brand
- Category
- Product
- ProductVariant
- ProductImage
- InventoryItem
- Customer
- Address
- Cart
- CartItem
- Order
- OrderItem
- Payment
- PaymentAttempt
- Shipment
- ShipmentTrackingEvent
- Coupon
- PromoBanner
- AdminUser
- AuditLog

---

## 14. Estados del sistema

### Estados de pago
- pending
- approved
- rejected
- failed
- cancelled
- refunded
- partially_refunded

### Estados del pedido
- draft
- created
- payment_pending
- paid
- preparing
- ready_for_pickup
- ready_for_shipping
- shipped
- delivered
- cancelled
- returned

### Importante
Nunca asumir que un redirect del frontend significa pago exitoso.
La confirmación real del pago debe venir desde backend / webhook / validación del proveedor.

---

## 15. Reglas funcionales importantes

1. El checkout debe funcionar sin crear cuenta.
2. El stock debe validarse en backend antes de confirmar orden.
3. El pago no debe marcarse como exitoso por confianza en el frontend.
4. El pedido debe registrar snapshot del producto al momento de compra.
5. El admin debe poder procesar pedidos rápido sin navegar pantallas innecesarias.
6. Debe existir trazabilidad de cambios importantes.
7. La experiencia móvil tiene prioridad sobre desktop.
8. El sistema debe estar preparado para crecimiento, pero sin sobreingeniería innecesaria.

---

## 16. Reglas UX/UI importantes

1. Priorizar velocidad y claridad.
2. Menos pasos = mejor.
3. Los CTA principales deben ser obvios.
4. El usuario siempre debe saber:
   - qué está comprando,
   - cuánto cuesta,
   - cuánto cuesta el envío,
   - qué sigue después.
5. El diseño debe verse premium pero no recargado.
6. La página de producto debe inspirar confianza.
7. El carrito y checkout deben ser extremadamente claros.
8. No esconder información crítica detrás de demasiados clics.

---

## 17. Estructura visual recomendada

### Home
- hero simple
- categorías destacadas
- marcas
- productos destacados
- ofertas
- beneficios / confianza
- footer claro

### Listado de productos
- grid limpio
- filtros simples
- ordenamiento
- tarjetas claras con imagen, nombre, precio y CTA

### Página de producto
- galería
- nombre
- marca
- precio
- variante / tamaño
- disponibilidad
- descripción
- atributos
- CTA comprar
- CTA agregar al carrito
- soporte / confianza

### Carrito
- items
- cantidades
- subtotal
- envío estimado
- total
- CTA checkout

### Checkout
- datos personales mínimos
- dirección o recogida
- método de pago
- resumen de orden
- CTA final

---

## 18. Integraciones previstas

### PayU
El sistema debe quedar preparado para:
- iniciar transacciones;
- registrar intentos de pago;
- recibir confirmaciones;
- actualizar estado de pago;
- mantener logs de integración.

### Mensajería / logística en Colombia
El sistema no debe acoplarse a un proveedor único desde la raíz.
Debe existir una capa de abstracción tipo `shipping_provider` o `shipping_service`.

Objetivo:
- poder integrar un proveedor hoy;
- cambiarlo mañana sin romper la lógica central del sistema.

---

## 19. Convenciones de desarrollo

1. Todo el código debe escribirse con nombres claros.
2. Mantener separación de responsabilidades.
3. Evitar lógica de negocio duplicada.
4. Evitar componentes frontend gigantes.
5. Preferir servicios reutilizables.
6. Toda integración externa debe encapsularse.
7. Toda funcionalidad crítica debe tener tests.
8. No hacer refactors masivos innecesarios mientras se construye MVP.
9. Cambios pequeños, seguros y verificables.
10. Mantener consistencia antes que “brillar” técnicamente.

---

## 20. Testing esperado

### Backend
- tests de modelos
- tests de servicios
- tests de API
- tests de pagos
- tests de flujo de pedidos
- tests de stock

### Frontend
- tests de componentes críticos
- tests de flujos principales
- validación de estados de carrito y checkout

### End-to-end
Flujos mínimos:
1. cliente navega y compra;
2. orden se crea;
3. pago cambia estado;
4. admin ve la orden;
5. orden cambia de estado;
6. tracking refleja progreso.

---

## 21. Roadmap sugerido

### Fase 0
- definir arquitectura base
- crear estructura del repo
- configurar backend/frontend
- definir modelos principales
- definir sistema de diseño base

### Fase 1
- catálogo
- home
- listado
- PDP
- carrito

### Fase 2
- checkout
- creación de orden
- PayU
- confirmación de compra

### Fase 3
- panel admin
- gestión de pedidos
- inventario
- clientes
- promociones

### Fase 4
- integración de envíos
- tracking
- reportes básicos
- hardening operativo

### Fase 5
- optimización UX/UI
- performance
- SEO básico
- mejoras de conversión

---

## 22. Prioridades absolutas del proyecto

Orden de prioridad:

1. compra rápida en móvil
2. catálogo claro y confiable
3. checkout simple
4. pagos sólidos
5. admin operativo
6. stock correcto
7. envío trazable
8. pulido visual fino

El sistema debe vender y operar bien antes de buscar sofisticación extra.

---

## 23. Instrucciones para Codex / agente

Usa este archivo como contexto global del proyecto.

Cuando implementes:
- respeta el alcance MVP;
- no agregues features fuera de scope sin motivo claro;
- prioriza consistencia y seguridad;
- evita complejidad innecesaria;
- mantén el enfoque en conversión + operación;
- piensa siempre tanto en cliente como en admin.

Si una decisión no está especificada:
- elegir la opción más simple;
- elegir la opción más mantenible;
- elegir la opción más segura;
- elegir la opción que favorezca velocidad de implementación sin comprometer la base del sistema.

Cada vez que se tome una decisión importante de producto o arquitectura, este archivo debe actualizarse.

---

## 24. Estado actual del proyecto

Estado actual:
- fase de planeación UX/UI y arquitectura funcional;
- aún no se ha cerrado implementación completa;
- este documento representa la fuente de verdad inicial para alinear diseño, frontend, backend y operación.

---

## 25. Decisiones abiertas por confirmar

Estas decisiones aún pueden ajustarse:
- nombre final de la marca/proyecto;
- proveedor logístico exacto;
- reglas exactas de cobertura y tarifas;
- políticas de cambios/devoluciones;
- reglas fiscales/facturación;
- si habrá login de cliente en V1 o se deja para más adelante;
- si se implementa wishlist en una segunda fase.

Hasta que se definan, Codex debe asumir la opción más simple compatible con el MVP.

## Shell Writing Rules

- Avoid bash heredocs inside single-quoted bash -lc strings.
- Do not use cat <<'EOF' through nested shell quoting unless strictly necessary.
- Prefer one of these approaches:
  1. write files with Python
  2. use apply_patch if it works
  3. output the full file content in chat if shell writing fails
- If a shell file-write command fails once due to quoting, do not retry the same strategy.

## Shell / File Writing Rules

- Use `python3`, never `python`
- Before writing nested files, create parent directories with `mkdir -p`
- Prefer `python3` + `Path(...).write_text(...)` for multiline file creation
- Do not use bash heredocs unless strictly necessary

# Apply_patch
 Quick example
{
"cmd": [
"apply_patch",
"*** Begin Patch\n*** Update File: src/main.rs\n@@\n- transformation: String,\n+ transformation: TransformMode,\n*** End Patch"
]
}

This will replace the transformation: String line with transformation: TransformMode.

That’s all you need to know! Feel free to give me a patch and I’ll apply it.

› use apply_patch tool to apply the following patch:
*** Begin Patch
*** Update File: src/main.rs
@@
- transformation: String,
+ transformation: TransformMode,
*** End Patch

26. Codex Execution Rules (CRITICAL)

The purpose of these rules is to ensure stable, incremental and high-quality development.

Scope control
Work on ONE module at a time.
Do NOT implement multiple domains in the same iteration.
Do NOT jump ahead in the roadmap.

Allowed scopes:

catalog
checkout
payments
orders
inventory
admin
frontend UI
Implementation strategy

When implementing features:

Understand existing code first
Identify minimal required changes
Implement incrementally
Validate before continuing

Do NOT:

rewrite large parts of the system unnecessarily
introduce new abstractions without need
mix unrelated changes
File editing rules
Use apply_patch ONLY for small edits
If apply_patch fails once → switch strategy immediately
For full file creation or large changes → use python3 + Path.write_text()
Avoid shell heredoc for multiline content
Always ensure directories exist before writing files
Git workflow
Never commit directly to main
Always use feature branches
Before commit:
show git status
show git diff --stat
Ask for confirmation before push
Backend discipline
Backend is the source of truth
Validate stock in backend
Never trust frontend for payment status
Keep payment logic separate from order logic
Frontend discipline
No business logic in frontend
Keep UI simple and fast
Optimize for mobile-first experience
Error handling

If something fails:

Do not retry blindly
Diagnose the cause
Change strategy
Continue execution
Performance awareness
Use select_related / prefetch_related when needed
Avoid unnecessary queries
Keep API responses efficient
Final rule
Prioritize stability over speed
Prioritize clarity over complexity
Think like a production engineer, not a code generator