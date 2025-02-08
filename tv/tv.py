

class TV:
    def __init__(self):
        self._channel_number = 1
        self._volume_level = 1
        self._temporary_volume = 0
        self._is_muted = False
        self._is_on = False
        self._MAX_VOLUME = 20
        self._MIN_VOLUME = 1
        self._MAX_CHANNEL_NUMBER = 100
        self._MIN_CHANNEL_NUMBER = 1
    def turn_on(self):
        self._is_on = True


    def turn_off(self):
        self._is_on = False

    @property
    def volume(self):
        return self._volume_level

    def increase_volume(self):
        tv_is_on = self._is_on
        volume_is_valid = self._volume_level < self._MAX_VOLUME
        tv_is_muted = self._is_muted
        if tv_is_muted : raise NotImplementedError("TV is muted!")
        if tv_is_on and volume_is_valid:
            self._volume_level += 1


    def decrease_volume(self):
        tv_is_on = self._is_on
        volume_is_valid = self._volume_level > self._MIN_VOLUME
        tv_is_muted = self._is_muted
        if tv_is_muted: raise NotImplementedError("TV is muted!")
        if tv_is_on and volume_is_valid:
            self._volume_level -= 1


    @property
    def channel_number(self):
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number: int):
        tv_is_on = self._is_on
        channel_number_is_valid = self._MAX_CHANNEL_NUMBER >= channel_number >= self._MIN_CHANNEL_NUMBER
        if tv_is_on and channel_number_is_valid:
            self._channel_number = channel_number

    def channel_up(self):
        if self._is_on:
            self._channel_number += 1



    def channel_down(self):
        tv_is_on = self._is_on
        channel_number_is_greater_than_min_channel_number = self._channel_number > self._MIN_CHANNEL_NUMBER
        if tv_is_on and channel_number_is_greater_than_min_channel_number:
            self._channel_number -= 1


    def mute(self):
        self._temporary_volume = self._volume_level
        self._volume_level = 0
        self._is_muted = True

    def unmute(self):
        self._volume_level = self._temporary_volume
        self._is_muted = False


