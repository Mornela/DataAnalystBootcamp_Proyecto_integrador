# Analizador de Embudo de Conversión

## Problema de negocio

Una tienda online quiere saber cuántos usuarios completan el recorrido desde la
visita hasta la compra. El objetivo es identificar dónde pierde más clientes.

## Métricas calculadas

- Usuarios únicos por etapa.
- Porcentaje de avance entre cada par de etapas consecutivas.
- Paso o pasos con mayor caída de conversión.

## Flujo del programa

1. Normaliza las etapas con `strip()` y `lower()`.
2. Deduplica con un conjunto que combina `user_id` y etapa.
3. Cuenta usuarios únicos para cada etapa.
4. Calcula el porcentaje de conversión entre etapas consecutivas.
5. Busca la conversión más baja y determina la mayor pérdida.

## Ejecución

Desde VS Code, abre una terminal en esta carpeta y ejecuta:

```powershell
python Proyecto_integrador_Olena.py
```
