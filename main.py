from pygame import*

back_color = (200, 255, 255)
window = display.set_mode((800, 500))
display.set_caption("Pong Time")

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if (keys[K_UP]) and self.rect.y > -10:
            self.rect.y -= self.speed
        if (keys[K_DOWN]) and self.rect.y < 440 - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if (keys[K_w]) and self.rect.y > -10:
            self.rect.y -= self.speed
        if (keys[K_s]) and self.rect.y < 440 - 80:
            self.rect.y += self.speed

clock = time.Clock()

player_l = Player("images/paddle.png", 10, 200, 70 , 180 ,5)
player_r = Player("images/paddle.png", 700, 200, 70 , 180 ,5)
ball = GameSprite("images/ball.png", 400, 200, 35, 35, 3)

font_game = font.Font(None, 30)
player_l_lose = font_game.render(
    "Player 1 Loses!", 1, (255, 0, 0)
    )

player_r_lose = font_game.render(
    "Player 2 Loses!", 1, (255, 0, 0)
    )

ball_speed_x = ball.speed
ball_speed_y = ball.speed

def reset(player: Player):
    window.blit(player.image, (player.rect.x, player.rect.y))

running = True
finish = False
while running:
    if not finish:
        
        window.fill(back_color)
        reset(player_l)
        reset(player_r)
        reset(ball)

        player_l.update_l()
        player_r.update_r()

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.y < 0 or ball.rect.y >= 450:
            ball_speed_y *= -1

        if sprite.collide_rect(ball, player_l) or sprite.collide_rect(ball, player_r):
            ball_speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(player_l_lose, [350, 220])

        if ball.rect.x >= 800:
            finish = True
            window.blit(player_r_lose, [350, 220])

    for ev in event.get():
            if ev.type == QUIT:
                running = False


    clock.tick(60)
    display.update()