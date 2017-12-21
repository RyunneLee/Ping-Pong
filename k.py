import sys
import pygame

DARKCOLOR = (170, 220, 255)

GREEN = (230, 255, 245)
PINK = (255, 230, 255)
WHITE = (255, 255, 255)
pygame.init()


def main():
    WIN_W = 920
    WIN_H = 570
    p_width = 40
    p_height = 150
    p_speed = 15

    # BALL SECTION
    b_height = 30
    b_width = 30

    pygame.display.set_caption("Ping Pong")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    pl_y = WIN_H / 2 - (p_height / 2)
    pl_x = p_width + (WIN_W / 20)
    moveUP1 = False
    moveDOWN1 = False
    pr_y = WIN_H / 2 - (p_height / 2)
    pr_x = WIN_W - p_width - (WIN_W / 20)
    moveUP2 = False
    moveDOWN2 = False
    y = WIN_W / 2 - WIN_H / 2

    paddle_left = pygame.Surface((p_width, p_height)).convert()
    paddle_left_rect = pygame.Rect(pl_x - p_width, pl_y, p_width, p_height)
    paddle_left.fill(GREEN)

    paddle_right = pygame.Surface((p_width, p_height)).convert()
    paddle_right_rect = pygame.Rect(pr_x, pr_y, p_width, p_height)
    paddle_right.fill(PINK)

    # BALL SECTION

    ball = pygame.Surface((b_width, b_height)).convert()
    ball_rect = pygame.Rect(WIN_W / 2 - (b_width / 2), WIN_H / 2 - (b_height / 2), b_width, b_height)
    ball.fill(WHITE)
    b_speed = (6, 6)

    screen.fill(DARKCOLOR)

    while True:

        if ball_rect.bottom >= WIN_H:
            b_speed = (b_speed[0], -b_speed[1])

        if ball_rect.top <= 0:
            b_speed = (b_speed[0], -b_speed[1])

        if ball_rect.right >= paddle_right_rect.x and ball_rect.left <= paddle_right_rect.x and ball_rect.bottom > paddle_right_rect.y and ball_rect.top < paddle_right_rect.y + p_height:
            b_speed = (-b_speed[0], b_speed[1])

        if ball_rect.left <= paddle_left_rect.x + p_width and ball_rect.right >= paddle_left_rect.x + p_width and ball_rect.bottom > paddle_left_rect.y and ball_rect.top < paddle_left_rect.y + p_height:
            b_speed = (-b_speed[0], b_speed[1])

        elif ball_rect.right >= WIN_W + 5:
            print "The winner is: Green!"
            break
        elif ball_rect.left <= -5:
            print "The winner is: Pink!"
            break
        # BALL MOVEMENT
        ball_rect = ball_rect.move(b_speed)

        if moveUP1 or moveDOWN1 or moveUP2 or moveDOWN2:
            if moveUP1:
                if paddle_left_rect.y - p_speed <= 0:
                    paddle_left_rect = paddle_left_rect.move((0, -paddle_left_rect.y))
                else:
                    paddle_left_rect = paddle_left_rect.move((0, -p_speed))

            if moveDOWN1:
                if paddle_left_rect.y + p_height >= WIN_H:
                    paddle_left_rect = paddle_left_rect.move((0, (WIN_H - p_height) - paddle_left_rect.y))
                else:
                    paddle_left_rect = paddle_left_rect.move((0, p_speed))

            if moveUP2:
                if paddle_right_rect.y - p_speed <= 0:
                    paddle_right_rect = paddle_right_rect.move((0, -paddle_right_rect.y))
                else:
                    paddle_right_rect = paddle_right_rect.move((0, -p_speed))
            if moveDOWN2:
                if paddle_right_rect.y + p_height >= WIN_H:
                    paddle_right_rect = paddle_right_rect.move((0, (WIN_H - p_height) - paddle_right_rect.y))
                else:
                    paddle_right_rect = paddle_right_rect.move((0, p_speed))

        # keystrokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    moveUP1 = True
                    moveDOWN1 = False
                elif event.key == pygame.K_DOWN:
                    moveUP2 = False
                    moveDOWN2 = True
                elif event.key == pygame.K_s:
                    moveUP1 = False
                    moveDOWN1 = True
                elif event.key == pygame.K_UP:
                    moveUP2 = True
                    moveDOWN2 = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    moveUP1 = False
                elif event.key == pygame.K_DOWN:
                    moveDOWN2 = False
                elif event.key == pygame.K_s:
                    moveDOWN1 = False
                elif event.key == pygame.K_UP:
                    moveUP2 = False

        # Sprites on screen
        screen.fill(DARKCOLOR)
        screen.blit(paddle_left, paddle_left_rect)
        screen.blit(paddle_right, paddle_right_rect)
        screen.blit(ball, ball_rect)

        pygame.display.flip()
if __name__ == "__main__":
    main()
