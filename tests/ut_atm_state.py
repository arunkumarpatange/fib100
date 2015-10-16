
import unittest

from collections import namedtuple
from pyd.atm_state import (
	AtmMachine,
	State,
	Event as Transition,
)

for state in State.__subclasses__():
	''' for testing only '''
	setattr(State, state.__name__, state.__name__)

class AtmStateTest(unittest.TestCase):

	def test_valid_pin(self):
		''' test happy path '''

		atm = AtmMachine(start='Idle')
		states = ( _state for _state in (State.Auth, State.Balance, State.Idle) )
		for state in [
			Transition.Swipe,
			Transition.ValidPin,
			Transition.Exit
		]:
			self.assertEqual(next(states), atm.next_state(state).state.name)
		print 'test_valid_pin'
		print atm._transitions

	def test_invalid_pin(self):
		''' test for invalid pin attempts '''
		atm = AtmMachine(start='Idle')
		states = ( _state for _state in (State.Auth, State.Auth, State.Auth, State.Idle) )
		for state in [
			Transition.Swipe,
			Transition.InvalidPin,
			Transition.InvalidPin,
			Transition.InvalidPin,
		]:
			self.assertEqual(next(states), atm.next_state(state).state.name)
		print 'test_invalid_pin'
		print atm._transitions


	def test_invalid_transition(self):
		atm = AtmMachine(start='Idle')
		states = ( _state for _state in (State.Idle, State.Auth, State.Auth, State.Auth) )
		for state in [
			Transition.Exit,
			Transition.Swipe,
			Transition.Swipe,
			Transition.Swipe,
		]:
			self.assertEqual(next(states), atm.next_state(state).state.name)
		print 'test_invalid_transition'
		print atm._transitions

	def test_inject_duplicate_transition(self):
		atm = AtmMachine()
		states = ( _state for _state in (State.Auth, State.Auth, State.Balance) )
		for state in [
			Transition.Swipe,
			Transition.Swipe,
			Transition.ValidPin,
		]:
			self.assertEqual(next(states), atm.next_state(state).state.name)
		print 'test_inject_duplicate_transition'
		print atm._transitions


if __name__ == '__main__':
	unittest.main()
