""" Uncomment line 90 on particles.py to implement gravity """

import pygame
import particles

pygame.display.set_caption('Physics simulation')
width, height = 400, 400
window = pygame.display.set_mode((width, height))

""" Create universe and set what functions the environment would have """
env = particles.Environment((width, height))
env.addFunctions(['move', 'accelerate', 'bounce', 'drag', 'collide'])

""" Add 5 particles """
env.addParticles(5)
env.addParticles(x=200, y=250, size=10, speed=4, angle=0)
for p in env.particles:
    p.colour = (255 - 255 * (p.mass / p.size / 1000), 255 - 255 * (p.mass / p.size / 1000), 255)

def main():
    selected_particle = None
    running = True
    while running:
        window.fill(env.bg_colour)

        for event in pygame.event.get():
            """ Events """
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                selected_particle = env.findParticle(mouseX, mouseY)
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_particle = None

        """ User control of a particle """
        if selected_particle:
            mouseX, mouseY = pygame.mouse.get_pos()
            selected_particle.mouseMove(mouseX, mouseY)
            pygame.draw.line(window, (255,0,0), (selected_particle.x, selected_particle.y), (mouseX, mouseY), 1)
            pygame.display.flip()

        env.update()

        """ Drawing all the particles after every update """
        for p in env.particles:
            pygame.draw.circle(window, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)

        pygame.display.flip()

if __name__ == '__main__':
    main()
