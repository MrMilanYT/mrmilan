Sprite = game.create_sprite(2, 2)
input.on_button_pressed(Button.A, on_button_pressed_a1)
def on_button_pressed_a1():
    pass
    Sprite.turn(Direction.LEFT, 90)

input.on_button_pressed(Button.B, on_button_pressed_b1)
def on_button_pressed_b1():
    pass
    Sprite.turn(Direction.RIGHT, 90)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
def on_gesture_shake():
    pass
    Sprite.move(1)
