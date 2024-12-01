# **Laboratorio de aprendizaje por refuerzo**
## **Introducción**

El aprendizaje por refuerzo es un enfoque general para aprender una política de control en sistemas dinámicos estocásticos a través de la interacción. En este paradigma, un agente aprende a optimizar su comportamiento acumulando recompensas con el tiempo. A diferencia de la optimización local, el aprendizaje por refuerzo se enfoca en descubrir el control óptimo incluso cuando las recompensas están diferidas en el tiempo.

En este laboratorio, exploraremos dos algoritmos clave:
1. **SARSA** (*State-Action-Reward-State-Action*): Un algoritmo *on-policy* que actualiza los valores de las acciones en función de la política que sigue el agente.
2. **Q-Learning**: Un algoritmo *off-policy* que estima el valor de la política óptima independientemente de la política actual del agente.

Además, abordaremos el dilema de **exploración-explotación**, donde el agente debe balancear entre:
- **Explorar**: Probar nuevas acciones para descubrir más sobre el entorno.
- **Explotar**: Utilizar lo aprendido para maximizar las recompensas conocidas.

Para simplificar el aprendizaje de los algoritmos, utilizaremos el entorno **FrozenLake-v0** de OpenAI Gym, un problema sencillo que permite ilustrar los conceptos básicos del aprendizaje por refuerzo.

---

## **Marco Teórico**

### **Elementos del Aprendizaje por Refuerzo**
1. **Agente**: Entidad que toma decisiones.
2. **Entorno**: Sistema en el que opera el agente.
3. **Estados ($S$)**: Configuraciones posibles del entorno.
4. **Acciones ($A$)**: Conjunto de decisiones posibles para el agente.
5. **Recompensas ($R$)**: Retroalimentación numérica que guía al agente.
6. **Política ($\pi$)**: Estrategia que sigue el agente para tomar decisiones.

### **Algoritmos de Aprendizaje**

1. **SARSA**:
   - SARSA es un algoritmo *on-policy*, lo que significa que actualiza los valores$Q(s, a)$basándose en la política actual.
   - Ecuación de actualización:
   $$
     Q_{t+1}(s_t, a_t) \leftarrow Q_t(s_t, a_t) + \alpha \left[ r_t + \gamma Q_t(s_{t+1}, a_{t+1}) - Q_t(s_t, a_t) \right]
   $$
     Donde:
     -$\alpha$: Tasa de aprendizaje.
     -$\gamma$: Factor de descuento.
     -$r_t$: Recompensa en el paso$t$.

2. **Q-Learning**:
   - Q-Learning es un algoritmo *off-policy* que busca la política óptima sin seguir necesariamente la política actual.
   - Ecuación de actualización:
   $$
     Q_{t+1}(s_t, a_t) \leftarrow Q_t(s_t, a_t) + \alpha \left[ r_t + \gamma \max_b Q_t(s_{t+1}, b) - Q_t(s_t, a_t) \right]
   $$

### **Estrategias de Exploración**
1. **ε-greedy**:
   - Con probabilidad$1-\epsilon$, el agente elige la mejor acción conocida.
   - Con probabilidad$\epsilon$, selecciona una acción aleatoria para explorar.
2. **Softmax**:
   - Asigna probabilidades a cada acción según sus valores$Q(s, a)$:
   $$
     P(a_i|s) = \frac{e^{\frac{Q(s, a_i)}{\tau}}}{\sum_j e^{\frac{Q(s, a_j)}{\tau}}}
   $$
     Donde$\tau$controla el nivel de exploración.

### **Evaluación y Rendimiento**
1. Para evaluar el aprendizaje, es esencial contar los éxitos en ventanas de episodios (por ejemplo, 100).
2. Las políticas aprendidas deben evaluarse repetidamente para obtener un promedio confiable, especialmente en entornos estocásticos.

---

## **Ejercicios**

### **Ejercicio 1: Familiarización con OpenAI Gym**
- **Objetivo**:
  - Usar el entorno FrozenLake-v1.
  - Aplicar acciones aleatorias para observar cómo interactúan el agente y el entorno.
  - Experimentar con políticas constantes para comprender el impacto de las acciones en el entorno.

---

### **Ejercicio 2: SARSA**
- **Objetivo**:
  - Implementar el algoritmo SARSA con exploración **ε-greedy**.
  - Actualizar una tabla$Q$de valores para cada estado y acción.
  - Medir el rendimiento contando los episodios exitosos en ventanas de 100 episodios.
  - Considerar el problema resuelto si la tasa de éxito supera el 76%.

---

### **Ejercicio 3: Q-Learning**
- **Objetivo**:
  - Sustituir la regla de actualización de SARSA por la de Q-Learning.
  - Comparar el rendimiento entre SARSA y Q-Learning para analizar sus diferencias.

---

### **Ejercicio 4: Exploración Softmax**
- **Objetivo**:
  - Implementar una estrategia de exploración Softmax.
  - Asignar probabilidades de selección de acciones proporcionalmente a sus valores$Q(s, a)$.

---

### **Ejercicio 5: Decaimiento de ε**
- **Objetivo**:
  - Diseñar un esquema para reducir$\epsilon$con el tiempo.
  - Evaluar cómo mejora la política aprendida en comparación con la política de exploración.

---

### **Ejercicio 6: Evaluación Apropiada**
- **Objetivo**:
  - Implementar un bucle interno para evaluar las políticas aprendidas repetidamente.
  - Comparar el rendimiento promedio entre SARSA y Q-Learning.
  - Concluir en qué circunstancias un algoritmo es mejor que el otro.

