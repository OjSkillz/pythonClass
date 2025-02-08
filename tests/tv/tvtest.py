import unittest
from tv.tv import TV


class TestClassTv(unittest.TestCase):

    def test_that_tv_can_be_turned_on(self):
        tv = TV()
        tv.turn_on()
        self.assertTrue(tv._is_on)

    def test_that_tv_can_be_turned_off(self):
        tv = TV()
        tv.turn_on()
        self.assertTrue(tv._is_on)
        tv.turn_off()
        self.assertFalse(tv._is_on)

    def test_that_tv_volume_can_be_turned_up(self):
        tv = TV()
        tv.turn_on()
        self.assertEqual(1, tv.volume)
        tv.increase_volume()
        self.assertEqual(2, tv.volume)

    def test_that_tv_volume_can_be_turned_down(self):
        tv = TV()
        tv.turn_on()
        self.assertEqual(1, tv.volume)
        tv.increase_volume()
        self.assertEqual(2, tv.volume)
        tv.decrease_volume()
        self.assertEqual(1, tv.volume)

    def test_that_tv_volume_cannot_be_increased_when_tv_is_off(self):
        tv = TV()
        self.assertEqual(1, tv.volume)
        tv.increase_volume()
        self.assertEqual(1, tv.volume)

    def test_that_tv_volume_cannot_be_decreased_when_tv_is_off(self):
        tv = TV()
        self.assertEqual(1, tv.volume)
        tv.decrease_volume()
        self.assertEqual(1, tv.volume)

    def test_that_tv_volume_cannot_go_beyond_max_volume_20(self):
        tv = TV()
        tv.turn_on()
        for count in range(20):
            tv.increase_volume()
        self.assertEqual(20, tv.volume)




    def test_that_volume_cannot_be_decreased_below_min_volume_1(self):
        tv = TV()
        tv.turn_on()
        tv.decrease_volume()
        self.assertEqual(1, tv.volume)

    def test_that_tv_can_set_channel(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 45
        self.assertEqual(45, tv.channel_number)

    def test_that_tv_cannot_set_channel_when_is_off(self):
        tv = TV()
        tv.channel_number = 20
        self.assertEqual(1, tv.channel_number)

    def test_that_tv_channel_can_be_changed_upwards(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 30
        tv.channel_up()
        self.assertEqual(31, tv.channel_number)

    def test_that_tv_channel_cannot_be_changed_upwards_when_is_off(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 20
        tv.turn_off()
        tv.channel_up()
        self.assertEqual(20, tv.channel_number)

    def test_that_tv_channel_cannot_be_set_above_max_channel_level_100(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 98
        tv.channel_number = 101
        self.assertEqual(98, tv.channel_number)

    def test_that_tv_channel_cannot_be_set_below_min_channel_level_1(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 100
        tv.channel_number = 0
        self.assertEqual(100, tv.channel_number)

    def test_that_channel_can_be_changed_downwards(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 100
        tv.channel_down()
        self.assertEqual(99, tv.channel_number)

    def test_that_channel_cannot_be_changed_downwards_when_tv_is_off(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 55
        tv.turn_off()
        tv.channel_down()
        self.assertEqual(55, tv.channel_number)

    def test_that_channel_cannot_be_changed_downwards_below_min_channel_level_1(self):
        tv = TV()
        tv.turn_on()
        tv.channel_number = 100
        for count in range(100):
            tv.channel_down()
        self.assertEqual(1, tv.channel_number)

    def test_that_tv_can_be_muted(self):
        tv = TV()
        tv.turn_on()
        for count in range(17):
            tv.increase_volume()
        tv.mute()
        self.assertEqual(0, tv.volume)

    def test_that_tv_reverts_to_volume_before_mute_when_unmute(self):
        tv = TV()
        tv.turn_on()
        for count in range(15):
            tv.increase_volume()
        self.assertEqual(16, tv.volume)
        tv.mute()
        self.assertEqual(0, tv.volume)
        tv.unmute()
        self.assertEqual(16, tv.volume)

    def test_that_volume_cannot_be_increased_when_tv_is_muted(self):
        tv = TV()
        tv.turn_on()
        for count in range(10):
            tv.increase_volume()
        tv.mute()
        self.assertRaises(NotImplementedError, tv.increase_volume)

    def test_that_volume_cannot_be_decreased_when_tv_is_muted(self):
        tv = TV()
        tv.turn_on()
        for count in range(10):
            tv.increase_volume()
        tv.mute()
        self.assertRaises(NotImplementedError, tv.decrease_volume)
