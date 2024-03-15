# encoding: utf-8

###########################################################################################################
#
#
# Filter without dialog plug-in
#
# Read the docs:
# https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import Glyphs
from GlyphsApp.plugins import FilterWithoutDialog


def nestedComponents(layer):
	componentsInComponents = [c.componentLayer.components for c in layer.components]
	return any(componentsInComponents)


class UnnestComponents(FilterWithoutDialog):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Unnest Components',
			'de': 'Komponenten entpacken',
			# 'fr': 'Mon filtre',
			# 'es': 'Mi filtro',
			# 'pt': 'Meu filtro',
			# 'jp': '私のフィルター',
			# 'ko': '내 필터',
			# 'zh': '我的过滤器',
		})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		for currLayer in layer.parent.layers:
			while nestedComponents(currLayer):
				for c in currLayer.components:
					if c.componentLayer.components:
						c.automaticAlignment = False
						c.decompose()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
