from .base import Base
import subprocess

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'man'
        self.kind = 'man'

        self.man_cmd = ['man', '--apropos']

    def on_init(self, context):
        pass

    def gather_candidates(self, context):
        candidates = []
        additional_opt = []
        command = self.man_cmd
        if context['input'].startswith('/') and context['input'].endswith('/'):
            additional_opt.append("--regex")

        word = context['input']
        word_len = len(word)
        if word_len == 0:
            word = "."

        command.extend(additional_opt)
        command.append(word)

        return [{'word': result, 'addr': result, 'kind': 'man'}
                for result
                in subprocess.run(command,
                                  check=True,
                                  universal_newlines=True,
                                  stdout=subprocess.PIPE
                                  ).stdout.split("\n")]
