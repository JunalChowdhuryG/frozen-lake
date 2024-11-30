#Reglas del juego
import random

class FrozenLake:
    def __init__(self, map_desc=None, is_slippery=True):
        self.map_desc = map_desc or [
            "SFFF",
            "FHFH",
            "FFFH",
            "HFFG"
        ]
        self.is_slippery = is_slippery
        self.n_rows = len(self.map_desc)
        self.n_cols = len(self.map_desc[0])
        self.start_state = self._find_start()
        self.state = self.start_state
        self.terminated = False

        # Diccionario de movimientos (acciones) corregido
        self.actions = {
            0: (0, -1),  # Izquierda
            1: (1, 0),   # Abajo
            2: (0, 1),   # Derecha
            3: (-1, 0)   # Arriba
        }

    def _find_start(self):
        """Encuentra la posición inicial (S) en el mapa."""
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if self.map_desc[row][col] == "S":
                    return (row, col)
        raise ValueError("Mapa no contiene estado inicial 'S'.")

    def reset(self):
        """Reinicia el juego al estado inicial."""
        self.state = self.start_state
        self.terminated = False
        return self.state

    def _inside_bounds(self, row, col):
        """Verifica si la posición está dentro del mapa."""
        return 0 <= row < self.n_rows and 0 <= col < self.n_cols

    def step(self, action):
        """Aplica una acción y devuelve el nuevo estado, recompensa, y si terminó."""
        if self.terminated:
            raise ValueError("El episodio ya terminó. Reinicia el juego con reset().")

        # Probabilidad de resbalar
        if self.is_slippery:
            action = random.choice(list(self.actions.keys()))

        # Determinar la nueva posición
        move = self.actions[action]
        new_row = self.state[0] + move[0]
        new_col = self.state[1] + move[1]

        # Si la nueva posición está fuera de los límites, el agente no se mueve
        if not self._inside_bounds(new_row, new_col):
            new_row, new_col = self.state

        # Actualizar estado
        new_state = (new_row, new_col)
        tile = self.map_desc[new_row][new_col]

        # Determinar recompensa y si terminó el episodio
        reward = 0
        if tile == "H":  # Agujero
            self.terminated = True
        elif tile == "G":  # Meta
            reward = 1
            self.terminated = True

        self.state = new_state
        return new_state, reward, self.terminated

    def render(self):
        """Muestra el mapa actual con la posición del agente."""
        for row in range(self.n_rows):
            row_str = ""
            for col in range(self.n_cols):
                if (row, col) == self.state:
                    row_str += "A"  # Agente
                else:
                    row_str += self.map_desc[row][col]
            print(row_str)
        print()
