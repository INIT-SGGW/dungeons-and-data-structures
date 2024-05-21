import jsonplus
from .game import Recorder, GameEvent, GameSysAction, PlayerMove

class FileRecorder(Recorder):
	""" A game recording that saves the game into a file
	"""
	def __init__(self, file_name:str):
		self.buffer = []
		self.file = file_name

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		with open(self.file, 'wt') as f:
			for msg in self.buffer:
				f.write(str(msg))

	def record(self, tick:int, event: GameEvent):
		message = f"{tick}: "
		if isinstance(event, GameSysAction):
			message += f"{event.action.value} "
			message += jsonplus.dumps(event.payload)

		elif isinstance(event, PlayerMove):
			message += f"{event.pid} {event.action.value}"
		
		message += "\n"
		self.buffer.append(message)

