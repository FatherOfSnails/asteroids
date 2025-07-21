import circleshape, pygame

class Asteroid(circleshape.Circleshape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (1,1,1), 
            (self.x, self.y), 
            self.radius,
            2
        )
    
    def update(self, dt):
        pass