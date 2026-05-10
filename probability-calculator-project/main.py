import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        # If num_balls exceeds available balls, return all balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        # Draw balls randomly without replacement
        drawn_balls = []
        for _ in range(num_balls):
            # Choose a random index
            ball_index = random.randint(0, len(self.contents) - 1)
            # Remove and add to drawn balls
            drawn_balls.append(self.contents.pop(ball_index))
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw balls from the hat copy
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the drawn balls
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        # Check if we got at least the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    # Calculate and return probability
    return successful_experiments / num_experiments