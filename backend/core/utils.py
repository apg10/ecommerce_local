"""Utility helpers for core models.
+
+Currently only a stock validation helper is needed.
+The function returns ``True`` if the requested quantity is
+available for the given product, otherwise ``False``.
+"""
+
+from .models import Product
+
+
+def has_sufficient_stock(product: Product, requested_qty: int) -> bool:
+    """Check if *product* has at least *requested_qty* available.
+
+    The ``Product`` model currently does not expose an explicit
+    inventory field; we assume a ``stock`` integer field exists.
+    If the field is missing a ``False`` value is returned.
+    """
+
+    # ``getattr`` is used to avoid attribute errors if ``stock`` is missing.
+    current_stock = getattr(product, "stock", 0)
+    return requested_qty <= current_stock
