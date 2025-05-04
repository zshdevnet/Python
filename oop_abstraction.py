from abc import ABC, abstractmethod

class SoundDevice(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # no logic here — just a rule

class Phone(SoundDevice):
    def make_sound(self):
        print("Phone rings: 🎵 Ring Ring!")

class AlarmClock(SoundDevice):
    def make_sound(self):
        print("Alarm goes: ⏰ Beep Beep!")

class FireAlarm(SoundDevice):
    def make_sound(self):
        print("Fire Alarm: 🚨 WEE-WOO WEE-WOO!")


phone = Phone()
phone.make_sound()
# Output: Phone rings: 🎵 Ring Ring!

alarm = AlarmClock()
alarm.make_sound()
# Output: Alarm goes: ⏰ Beep Beep!

fire = FireAlarm()
fire.make_sound()
# Output: Fire Alarm: 🚨 WEE-WOO WEE-WOO!
