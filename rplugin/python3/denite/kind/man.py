from .openable import Kind as Openable
import re
import subprocess

class Kind(Openable):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'man'
        self.default_action = 'open'
        self._pattern = re.compile('^(\S+) \((\S+)\).*$')

    def action_open(self, context):
        target = context['targets'][0]

        match = self._pattern.match(target['word'])
        if match is None:
            return

        word = match[1]
        section = match[2]
        vim_command = "r! man -P cat {section} {word}"
        self.vim.command(vim_command.format(section=section, word=word))
