from pygame import*

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Pong Time")

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_LEFT] or keys[K_a]) and self.rect.x > 10:
            self.rect.x -= self.speed
        if (keys[K_RIGHT] or keys[K_d]) and self.rect.x < 700 - 80:
            self.rect.x += self.speed

clock = time.Clock()

player_l = Player("images/paddle.png", 10, 200, 120 , 150 ,5)
player_r = Player("images/paddle.png", 700, 200, 120 , 150 ,5)
ball = GameSprite("images/ball.png", 400, 200, 35, 35, 5)

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    window.fill(back_color)
    reset(player_l)
    reset(player_r)
    reset(ball)


    clock.tick(60)
    display.update()