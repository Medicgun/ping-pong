from pygame import*

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Pong Time")

clock = time.Clock()

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    window.fill(back_color)
    clock.tick(60)
    display.update()