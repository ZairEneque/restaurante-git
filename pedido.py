def calcular_total(subtotal):
    descuento_cliente = subtotal * 0.10
    total = subtotal - descuento_cliente
    return total

subtotal = 50.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")
