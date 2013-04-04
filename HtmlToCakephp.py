import sublime
import sublime_plugin
import os
import subprocess


def syntax_name(view):
	syntax = os.path.basename(view.settings().get('syntax'))
	syntax = os.path.splitext(syntax)[0]
	return syntax


def docset_prefix(view, settings):
	syntax_docset_map = settings.get('syntax_docset_map', {})
	syntax = syntax_name(view)

	if syntax in syntax_docset_map:
		return syntax_docset_map[syntax] + ':'

	return None


class HtmlToCakephpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()[0]
		if len(selection) == 0:
			selection = self.view.word(selection)
		word = self.view.substr(selection)
		print word
		subprocess.call(["open"])