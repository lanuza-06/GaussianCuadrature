# Explicación del método

La cuadratura Gaussiana consiste en aproximar una integral de la forma:

\[
\int_a^b f(x)\, dx \approx \sum_{k=1}^N w_k f(x_k)
\]

donde:
- \(x_k\) son las raíces de los polinomios de Legendre \(P_N(x)\).
- \(w_k\) son los pesos asociados.

**Propiedades importantes:**
- Exactitud para polinomios de grado hasta \(2N-1\).
- Los puntos de muestreo no son equidistantes.
- La convergencia es muy rápida.

En nuestro caso, usamos las funciones `np.polynomial.legendre.leggauss`
para obtener directamente \(x_k, w_k\).

