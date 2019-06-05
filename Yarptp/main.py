import RPi.GPIO as GPIO
from Yarptp.controllers import movement_controller as m_ctl
from Yarptp.controllers import validate

class Yarptp:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.__enableA = 0
        self.__input1 = 0
        self.__input2 = 0

        self.__enableB = 0
        self.__input3 = 0
        self.__input4 = 0

        self.__frequency = 500
        self.__pwm_a = None
        self.__pwm_b = None

        self.TIME_X_STEP = 0.3
        self.TIME_X_TURNNING = 0.3

        self.__movements_ctl = m_ctl(GPIO, self)

        self.setPinsLeftMotor(18, 23, 24)
        self.setPinsRightMotor(19, 6, 5)

    def setPinsLeftMotor(self, enA, in1, in2):
        """
        Personalizar los pines GPIO usados por el motor izquierdo.

        :param int enA: Código BCM del pin conectado a la entrada enA del controlador L298N.
        :param int in1: Código BCM del pin conectado a la entrada in1 del controlador L298N.
        :param int in2: Código BCM del pin conectado a la entrada in2 del controlador L298N.
        """
        is_not_valid, (
            self.__enableA,
            self.__input1, 
            self.__input2
        ) = validate(int_params=(enA, in1, in2))
        pin_list = (self.__enableA, self.__input1, self.__input2)        
        setLeftMotor = True
        self.__movements_ctl.enable_pins(pin_list, setLeftMotor)

    def setPinsRightMotor(self, enB, in3, in4):
        """
        Personalizar los pines GPIO usados por el motor derecho.

        :param int enB: Código BCM del pin conectado a la entrada enB del controlador L298N.
        :param int in3: Código BCM del pin conectado a la entrada in3 del controlador L298N.
        :param int in4: Código BCM del pin conectado a la entrada in4 del controlador L298N.
        """
        self.__enableB, self.__input3, self.__input4 = enB, in3, in4
        pin_list = (self.__enableB, self.__input3, self.__input4)
        setLeftMotor = False
        self.__movements_ctl.enable_pins(pin_list, setLeftMotor)

    def ForwardMotorL(self, time=0.0, speed=50):
        """Mover el motor izquierdo del robot hacia delante.

        :param time: (opcional) Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: (opcional) Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input1,self.__input2)
        signal_list = (GPIO.LOW, GPIO.HIGH)
        motor = 'left'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def ForwardMotorR(self, time=0.0, speed=50):
        """
        Mover el motor derecho hacia delante.

        :param time:  Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input3,self.__input4)
        signal_list = (GPIO.LOW, GPIO.HIGH)
        motor = 'right'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def ReverseMotorL(self, time=0.0, speed=50):
        """
        Mover el motor izquierdo hacia atrás.

        :param time:  Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input1,self.__input2)
        signal_list = (GPIO.HIGH, GPIO.LOW)
        motor = 'left'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def ReverseMotorR(self, time=0.0, speed=50):
        """
        Mover el motor derecho hacia atrás.

        :param time:  Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input3,self.__input4)
        signal_list = (GPIO.HIGH, GPIO.LOW)
        motor = 'right'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def Forward(self, time=0.0, speed=50):
        """
        Mover ambos motores hacia delante.

        :param time:  Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input1,self.__input2,self.__input3,self.__input4)
        signal_list = (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        motor = 'both'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def Reverse(self, time=0.0, speed=50):
        """
        Mover ambos motores hacia atrás.

        :param time:  Tiempo que durará el movimiento ejecutado.
        :type time: float
        :param speed: Velocidad del movimiento.
        :type speed: int
        """
        pin_list = (self.__input1,self.__input2,self.__input3,self.__input4)
        signal_list = (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        motor = 'both'
        self.__movements_ctl.execute_movements(pin_list, signal_list, motor, time, speed)

    def ForwardStep(self):
        """
        Mueve el robot 1 paso hacia delante.
        """
        signal_list = (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        self.__movements_ctl.move_step_or_turn(signal_list, self.TIME_X_STEP)

    def ReverseStep(self):
        """
        Mueve el robot 1 paso hacia atrás.
        """
        signal_list = (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        self.__movements_ctl.move_step_or_turn(signal_list, self.TIME_X_STEP)

    def TurnLeft(self):
        """
        Gira el robot hacia la izquierda en un ángulo de 90°.
        """
        signal_list = (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        self.__movements_ctl.move_step_or_turn(signal_list, self.TIME_X_TURNNING)

    def TurnRight(self):
        """
        Gira el robot hacia la derecha en un ángulo de 90°.
        """
        signal_list = (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        self.__movements_ctl.move_step_or_turn(signal_list, self.TIME_X_TURNNING)

    def Stop(self):
        """
        Detiene ambos motores.
        """
        pin_list = (self.__input1, self.__input2, self.__input3, self.__input4)
        self.__movements_ctl.power_off(pin_list)

    def TurnOffMotors(self):
        """
        Desactiva el control de los pines del robot.
        """
        GPIO.cleanup()
