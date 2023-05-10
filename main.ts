let Sprite = game.createSprite(2, 2)
input.onButtonPressed(Button.A, function on_button_pressed_a1() {
    
    Sprite.turn(Direction.Left, 90)
})
input.onButtonPressed(Button.B, function on_button_pressed_b1() {
    
    Sprite.turn(Direction.Right, 90)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Sprite.move(1)
})
