import pygame

# inicializar Pygame
pygame.init()

# configurar la pantalla
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# cargar las imágenes de la animación
num_frames = 6446
frames = [pygame.image.load(f"C:/Users/uripe/Documents/python/appe bad/badapple/frame_{i:04d}.jpg") for i in range(1, num_frames+1)]

# cargar la canción de Bad Apple
pygame.mixer.music.load("bad_apple.mp3")


# configurar el reloj para actualizar la pantalla
clock = pygame.time.Clock()



# reproducir la canción y mostrar la animación
pygame.mixer.music.play()
frame_idx = 0
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                quit()
    # obtener el cuadro actual de la animación
    frame = frames[frame_idx]
    
    # mostrar el cuadro en la pantalla
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    
    # actualizar el índice del cuadro
    frame_idx += 1
    if frame_idx >= num_frames:
        frame_idx = 0
    
    # ajustar el tempo de la canción al FPS de la animación
    clock.tick(30)

    
# detener Pygame
pygame.quit()