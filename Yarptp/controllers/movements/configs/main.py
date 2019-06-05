class PrivateMethods:
    def __init__(self, GPIO, yarptp_instance):
        self.GPIO = GPIO
        self.yarptp_instance = yarptp_instance

    def enable_pins(pin_list, setMotorLeft):
        self.GPIO.setup(pin_list, self.GPIO.OUT)
        PWM_pin = pin_list[0]

        if setMotorLeft:
            self.yarptp_instance.__pwm_a = self.GPIO.PWM(
                PWM_pin,
                self.yarptp_instance.__frequency
            )
            self.yarptp_instance.__pwm_a.start(0)
        else:
            self.yarptp_instance.__pwm_b = self.GPIO.PWM(
                PWM_pin,
                self.yarptp_instance.__frequency
            )
            self.yarptp_instance.__pwm_b.start(0)


    def set_signals(pin_list, signal_list, motor, speed):
        self.GPIO.output(pin_list, signal_list)
        if motor == 'left':
            self.yarptp_instance.__pwm_a.ChangeDutyCycle(speed)
        elif motor == 'right':
            self.yarptp_instance.__pwm_b.ChangeDutyCycle(speed)
        elif motor == 'both':
            self.yarptp_instance.__pwm_a.ChangeDutyCycle(speed)
            self.yarptp_instance.__pwm_b.ChangeDutyCycle(speed)

    def power_off(pin):
        self.GPIO.output(pin, self.GPIO.LOW)