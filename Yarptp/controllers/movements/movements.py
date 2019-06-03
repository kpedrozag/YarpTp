from Yarptp.controllers.movements.configs import Configs
from time import sleep as sleep_from_time


def movement_controller(GPIO_module, yarptp_instance):

    class Movements:

        def __init__(self, GPIO, yarptp_instance):
            self.all_input_pins = (
                yarptp_instance.__input1,
                yarptp_instance.__input2,
                yarptp_instance.__input3,
                yarptp_instance.__input4
            )
            self.config_methods = Configs(GPIO, yarptp_instance)
            self.enable_pins = self.config_methods.enable_pins
            self.power_off = self.config_methods.power_off


        def execute_movements(pin_list, signal_list, motor, time, speed):
            
            indefined_time = time == 0.0

            if indefined_time:
                self.config_methods.set_signals(pin_list, signal_list, motor, speed)
            else:
                self.config_methods.set_signals(pin_list, signal_list, motor, speed)
                sleep(tm)
                self.config_methods.power_off(pin_list)


        def move_step_or_turn(signal_list, time):

            self.config_methods.set_signals(self.all_input_pins, signal_list, 2, 50)
            sleep_from_time(time)
            self.config_methods.power_off(self.all_input_pins)
    
    instance = Movements(GPIO_module, yarptp_instance)
    return instance