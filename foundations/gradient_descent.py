class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = float(init)
        for _ in range(iterations):
            f_x = x * x
            f_x_slash = float(2) * x
            x -= learning_rate * f_x_slash
        
        if iterations == 0:
            return init
        return round(x, 5)