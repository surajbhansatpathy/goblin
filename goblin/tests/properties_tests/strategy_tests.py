from __future__ import unicode_literals
from goblin.tests import BaseGoblinTestCase
from goblin.properties.strategy import *
from nose.plugins.attrib import attr


@attr('unit', 'strategy')
class StrategyBaseClassTestCase(BaseGoblinTestCase):
    """ Test Base Strategy Callable Object """

    def setUp(self):
        super(StrategyBaseClassTestCase, self).setUp()
        self.klass = Strategy

    def test_callable(self):
        """ Test that the strategy is callable """
        self.assertTrue(callable(self.klass.condition))

    def test_strategy(self):
        """ Test Base Strategy Callable Object """
        self.assertRaises(NotImplementedError, self.klass.condition, 0, 1, True, False)


@attr('unit', 'strategy')
class SaveOnceStrategyTestCase(StrategyBaseClassTestCase):
    """ Test SaveOnce Strategy """

    def setUp(self):
        super(SaveOnceStrategyTestCase, self).setUp()
        self.klass = SaveOnce

    def test_strategy(self):
        """ Test SaveOnce Strategy """
        self.assertTrue(self.klass.condition(previous_value=None,
                                             value=1,
                                             has_changed=False,
                                             first_save=True))
        self.assertRaises(SaveStrategyException, self.klass.condition, 0, 1, True, False)


@attr('unit', 'strategy')
class SaveAlwaysStrategyTestCase(StrategyBaseClassTestCase):
    """ Test SaveAlways Strategy """

    def setUp(self):
        super(SaveAlwaysStrategyTestCase, self).setUp()
        self.klass = SaveAlways

    def test_strategy(self):
        """ Test SaveAlways Strategy """
        self.assertTrue(self.klass.condition(previous_value=None,
                                             value=1,
                                             has_changed=False,
                                             first_save=True))


@attr('unit', 'strategy')
class SaveOnChangeStrategyTestCase(StrategyBaseClassTestCase):
    """ Test SaveOnChange Strategy """

    def setUp(self):
        super(SaveOnChangeStrategyTestCase, self).setUp()
        self.klass = SaveOnChange

    def test_strategy(self):
        """ Test SaveOnChange Strategy """
        self.assertTrue(self.klass.condition(previous_value=None,
                                             value=1,
                                             has_changed=True,
                                             first_save=True))
        self.assertFalse(self.klass.condition(previous_value=1,
                                              value=1,
                                              has_changed=False,
                                              first_save=False))


@attr('unit', 'strategy')
class SaveOnIncreaseStrategyTestCase(StrategyBaseClassTestCase):
    """ Test SaveIncrease Strategy """

    def setUp(self):
        super(SaveOnIncreaseStrategyTestCase, self).setUp()
        self.klass = SaveOnIncrease

    def test_strategy(self):
        """ Test SaveIncrease Strategy """
        self.assertTrue(self.klass.condition(previous_value=None,
                                             value=1,
                                             has_changed=True,
                                             first_save=True))
        self.assertFalse(self.klass.condition(previous_value=1,
                                              value=1,
                                              has_changed=False,
                                              first_save=False))
        self.assertFalse(self.klass.condition(previous_value=2,
                                              value=1,
                                              has_changed=True,
                                              first_save=False))


@attr('unit', 'strategy')
class SaveOnDecreaseStrategyTestCase(StrategyBaseClassTestCase):
    """ Test SaveOnDecrease Strategy """

    def setUp(self):
        super(SaveOnDecreaseStrategyTestCase, self).setUp()
        self.klass = SaveOnDecrease

    def test_strategy(self):
        """ Test SaveOnChange Strategy """
        self.assertTrue(self.klass.condition(previous_value=None,
                                              value=1,
                                              has_changed=True,
                                              first_save=True))
        self.assertFalse(self.klass.condition(previous_value=1,
                                              value=1,
                                              has_changed=False,
                                              first_save=False))
        self.assertTrue(self.klass.condition(previous_value=2,
                                             value=1,
                                             has_changed=True,
                                             first_save=False))
