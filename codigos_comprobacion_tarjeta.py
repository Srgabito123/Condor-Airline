def has_16_characters(s):
    return len(s) == 16

tarjeta = has_16_characters("1234567890123456")

if tarjeta:
    print("La tarjeta tiene 16 caracteres")
else:
    print("La tarjeta no tiene 16 caracteres")

def has_3_characters(s):
    return len(s) == 3

tarjeta = has_3_characters("1234567890123456")

if tarjeta:
    print("El CVV tiene 3 caracteres")
else:
    print("El CVV no tiene 3 caracteres")
