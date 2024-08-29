class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == "__main__":

    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)
    remote_control = RemoteControl()


    remote_control.set_command(light_on_command)
    remote_control.execute_command()

    remote_control.set_command(light_off_command)
    remote_control.execute_command()
