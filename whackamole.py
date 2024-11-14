import pygame
import random

GRID_WIDTH, GRID_HEIGHT = 20, 16
SQUARE_SIZE = 32

def main():
	try:
		pygame.init()
		#You can draw the mole with this snippet:
		#screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
		mole_image = pygame.image.load("mole.png")
		screen = pygame.display.set_mode((GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE))
		clock = pygame.time.Clock()

		mole_x, mole_y = 0, 0

		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_x, mouse_y = event.pos

					if (mouse_x // SQUARE_SIZE == mole_x) and (mouse_y // SQUARE_SIZE == mole_y):
						mole_x = random.randrange(GRID_WIDTH)
						mole_y = random.randrange(GRID_HEIGHT)

			screen.fill("light green")

			for x in range(0, GRID_WIDTH * SQUARE_SIZE, SQUARE_SIZE):
				pygame.draw.line(screen, "black", (x, 0), (x, GRID_HEIGHT * SQUARE_SIZE))
			for y in range(0, GRID_HEIGHT * SQUARE_SIZE, SQUARE_SIZE):
				pygame.draw.line(screen, "black", (0, y), (GRID_WIDTH * SQUARE_SIZE, y))

			screen.blit(mole_image, (mole_x * SQUARE_SIZE, mole_y * SQUARE_SIZE))

			pygame.display.flip()
			clock.tick(60)

	finally:
		pygame.quit()


if __name__== "__main__":
	main()
