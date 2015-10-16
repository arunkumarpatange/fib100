#
#	__author__: ArunKumar
#	simple state machine implementation for ATM machine
#


class State(object):
	abstract = True

	classes = {}
	@classmethod
	def get_subclasses_dict(cls):
		return dict(
			(state.__name__, state) for state in cls.__subclasses__()
			# if not getattr(cls, 'abstract', False)
		)

	@classmethod
	def get_valid_events(cls): return getattr(cls, 'events', ())

	@classmethod
	def get_by_name(cls, name):
		if name not in cls.classes:
			cls.classes = cls.get_subclasses_dict()
		return cls.classes.get(name, cls)()

	def __init__(self):
		self.name = self.__class__.__name__

	def __str__(self):
		return self.name

	def get_next_state_on_event(self, event):
		return next(( 
			self.get_by_name(_state)
			for _event, _state in self.get_valid_events() if event == _event and self.name != _state),
			self
		)


class Event(object):
	''' Transition Events '''

	Swipe = 'swipe'
	ValidPin = 'pin'
	InvalidPin = 'invalid_pin'
	Exit = 'exit'

	@classmethod
	def get_by_name(cls, name): return cls(name)

	def __init__(self, name):
		self.name = name

	def trigger(self, state):
		return state.get_next_state_on_event(self.name)


class Idle(State):
	# all valid events
	events = (
		(Event.Swipe, 'Auth'),
		(Event.Exit, 'Idle')
	)


class Balance(State):
	events = (
		(Event.Exit, 'Idle'),
	)


class Auth(State):
	ATTEMPTS = 3

	events = (
		(Event.ValidPin, 'Balance'),
		(Event.InvalidPin, 'Auth'),
		(Event.Exit, 'Idle')
	)

	def __init__(self):
		super(self.__class__, self).__init__()
		self.count = 0

	def get_next_state_on_event(self, event):

		if Event.ValidPin == event:
			self.count = 0 

		if Event.InvalidPin == event:
			self.count = self.count + 1

		if self.count == self.ATTEMPTS:
			self.count = 0
			event = Event.Exit

		return super(self.__class__, self).get_next_state_on_event(event)


class StateMachine(object):
	abstract = True

	def __init__(self, start):
		self.state = State.get_by_name(start)
		self._event = None
		self._transitions = str(self)

	def __str__(self):
		return "Event: %s => State: %s \n" % (self._event, self.state.name)

	def next_state(self, *args, **kwargs):
		self._transitions = self._transitions + str(self)


class AtmMachine(StateMachine):

	def __init__(self, start=None):
		super(self.__class__, self).__init__(start or 'Idle')
		self._event = None

	def next_state(self, event):
		self.state = Event.get_by_name(event).trigger(self.state)
		self._event = event
		super(self.__class__, self).next_state()
		return self

