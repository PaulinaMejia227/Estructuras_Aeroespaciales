"""
=============================================================
ESTRUCTURAS AEROESPACIALES — UNII  |  Clase 1  |  07 Julio 2026
ACTIVIDAD PARA ENTREGA (sube tu solución a NEOLMS)
Tema: Envolvente V-n — Acrobática, Altitud y Esfuerzo de Aro
=============================================================
INSTRUCCIONES GENERALES
  1. Completa CADA sección marcada con TODO:
  2. No borres los comentarios de orientación.
  3. Guarda el archivo como:  actividad1_TuNombre.py
  4. Súbelo a NEOLMS en la tarea "Actividad 1".

LIBRERÍAS NECESARIAS:  numpy  matplotlib
Activar entorno:  .venv  (VS Code selecciona el intérprete correcto)
=============================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# PARÁMETROS BASE — NO MODIFICAR
# ─────────────────────────────────────────────
m, g   = 1100.0, 9.81   # masa [kg], gravedad [m/s^2]
S      = 16.0           # superficie alar [m^2]
rho0   = 1.225          # densidad a nivel del mar [kg/m^3]
CLmax  = 1.4
CLmin  = -1.0
VD     = 85.0           # velocidad de picado [m/s]

W = m * g               # peso [N]

def n_aero(V, CL, rho):
    """Factor de carga aerodinamico a velocidad V"""
    return 0.5 * rho * V**2 * S * CL / W


# ─────────────────────────────────────────────
# EJERCICIO 1 — Categoría ACROBÁTICA (n = +6.0 / -3.0)
# ─────────────────────────────────────────────
# En la práctica usamos categoría utilitaria (n = +4.4 / -1.76).
# Repite el cálculo de velocidades características para acrobática.
# ─────────────────────────────────────────────
n_pos_a, n_neg_a = 6.0, -3.0

# TODO 1a: Calcula VS (pérdida con n=1, no cambia con la categoría)
VS = np.sqrt(2*W / (rho0*S*CLmax))

# TODO 1b: Calcula VA para la categoría acrobática
VA_acro = VS * np.sqrt(n_pos_a)

# TODO 1c: Calcula VG (esquina negativa) con CLmin y n_neg_a
VSi     = np.sqrt(2*W / (rho0*S*abs(CLmin)))
VG_acro = VSi * np.sqrt(abs(n_neg_a))

print("--- EJERCICIO 1: Categoria acrobatica ---")
print(f"  VS       = {VS:6.1f} m/s")
print(f"  VA acro  = {VA_acro:6.1f} m/s   (utilitario era 58.8 m/s)")
print(f"  VG acro  = {VG_acro:6.1f} m/s")

# TODO 1d: Grafica la envolvente acrobática (puedes copiar el bloque
#          de gráfica de practica_clase1.py cambiando n_pos y n_neg).
#          Guarda como "vn_acrobatico.png".
# Velocidades para la envolvente V-n
V = np.linspace(0, VD, 500)

# Factores de carga aerodinámicos
n_positivo = n_aero(V, CLmax, rho0)
n_negativo = n_aero(V, CLmin, rho0)

# Límites estructurales acrobáticos
n_superior = np.minimum(n_positivo, n_pos_a)
n_inferior = np.maximum(n_negativo, n_neg_a)

# Gráfica de la envolvente
plt.figure(figsize=(10, 6))

plt.plot(V, n_superior, color="blue", label="Límite positivo")
plt.plot(V, n_inferior, color="red", label="Límite negativo")

plt.axhline(0, color="black", linewidth=0.8)
plt.axhline(n_pos_a, color="blue", linestyle="--")
plt.axhline(n_neg_a, color="red", linestyle="--")

plt.axvline(VD, color="gray", linestyle="--", label="VD")

plt.scatter(VA_acro, n_pos_a, color="blue")
plt.scatter(VG_acro, n_neg_a, color="red")

plt.xlabel("Velocidad V (m/s)")
plt.ylabel("Factor de carga n")
plt.title("Envolvente V-n - Categoría acrobática")

plt.grid(True)
plt.legend()

plt.savefig("vn_acrobatico.png", dpi=300)
plt.show()

# TODO 1e: Responde en un comentario:
#   ¿Cuánto subió VA respecto al utilitario y qué le exige eso
#   a la estructura (masa, rigidez, factores de seguridad)?
# RESPUESTA:  La velocidad de maniobra aumenta de 58.8 m/s a
# aproximadamente 68.7 m/s, es decir, 9.9 m/s más.
# Esto significa que la estructura debe resistir mayores
# factores de carga durante las maniobras acrobáticas.
# Para soportarlos, puede necesitar refuerzos estructurales,
# mayor rigidez y resistencia, lo que también puede aumentar
# la masa de la aeronave. Además, debe cumplir con los
# factores de seguridad establecidos para su categoría.

# ─────────────────────────────────────────────
# EJERCICIO 2 — Efecto de la ALTITUD (h = 3000 m)
# ─────────────────────────────────────────────
# A 3000 m la densidad baja a rho = 0.909 kg/m^3.
# Recalcula VS y VA (categoría utilitaria n=+4.4) en velocidad
# verdadera (TAS).
# ─────────────────────────────────────────────
rho_h = 0.909

# TODO 2a: VS a 3000 m
VS_h = np.sqrt(2*W / (rho_h*S*CLmax))

# TODO 2b: VA a 3000 m (n_lim = 4.4)
VA_h = VS_h * np.sqrt(4.4)

print("\n--- EJERCICIO 2: Altitud 3000 m ---")
print(f"  VS(3000 m) = {VS_h:6.1f} m/s   (nivel del mar: 28.0 m/s)")
print(f"  VA(3000 m) = {VA_h:6.1f} m/s   (nivel del mar: 58.8 m/s)")

# TODO 2c: Responde en un comentario:
#   ¿Por qué las velocidades verdaderas SUBEN con la altitud si
#   el avión es el mismo? ¿Qué velocidad (indicada o verdadera)
#   "siente" realmente la estructura?
# RESPUESTA: Al aumentar la altitud, la densidad del aire disminuye.
# Por eso, el avión necesita una mayor velocidad verdadera para
# generar la misma sustentación. La estructura responde a la
# presión dinámica del aire, que depende de la densidad y de la
# velocidad al cuadrado. Por esta razón, la velocidad indicada
# representa mejor las cargas aerodinámicas que la velocidad
# verdadera.


# ─────────────────────────────────────────────
# EJERCICIO 3 — Esfuerzo de ARO del fuselaje presurizado
# ─────────────────────────────────────────────
# Fórmula del esfuerzo circunferencial (aro):  sigma = p*r/t
# Datos: p = 0.04 MPa, r = 1.4 m, t = 1.5 mm
# Material: Al 2024-T3 con sigma_y = 345 MPa, factor FS = 1.5
# ─────────────────────────────────────────────
p  = 0.04e6    # Pa
r  = 1.4       # m
t  = 1.5e-3    # m
sigma_y = 345e6
FS = 1.5

# TODO 3a: Calcula el esfuerzo de aro
sigma_aro = p * r / t

# TODO 3b: Calcula el esfuerzo admisible (sigma_y / FS)
sigma_adm = sigma_y / FS

# TODO 3c: Calcula el margen  (sigma_adm / sigma_aro)
margen = sigma_adm / sigma_aro

print("\n--- EJERCICIO 3: Esfuerzo de aro ---")
print(f"  sigma_aro = {sigma_aro/1e6:6.1f} MPa")
print(f"  sigma_adm = {sigma_adm/1e6:6.1f} MPa")
print(f"  margen    = {margen:5.2f}x")

# TODO 3d: Responde en un comentario:
#   ¿El diseño va sobrado? ¿Por qué en fuselajes reales el espesor
#   no se decide solo por presurización? (piensa en fatiga y daño)
# RESPUESTA: El esfuerzo de aro es de 37.3 MPa y el esfuerzo
# admisible es de 230 MPa, por lo que existe una reserva
# considerable de resistencia frente a la presurización.
# Sin embargo, el espesor del fuselaje también debe considerar
# la fatiga por ciclos de presurización, las cargas de vuelo,
# la corrosión y la propagación de grietas.
# Por eso, el diseño debe garantizar resistencia y tolerancia
# al daño durante la vida útil de la aeronave.
