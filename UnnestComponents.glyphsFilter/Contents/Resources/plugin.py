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
		self._processedGlyphs = {}

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		glyph = layer.parent
		if not glyph:
			layersToProcess = [layer]
		else:
			font = glyph.parent
			if not font:
				layersToProcess = [layer]
			else:
				if len(font.masters) > 1:
					fontId = id(font)
					if fontId not in self._processedGlyphs:
						self._processedGlyphs[fontId] = set()
					if glyph.name in self._processedGlyphs[fontId]:
						return
					self._processedGlyphs[fontId].add(glyph.name)
					layersToProcess = [glyph.layers[m.id] for m in font.masters]
				else:
					layersToProcess = glyph.layers

		for currLayer in layersToProcess:
			if not currLayer:
				continue
			while nestedComponents(currLayer):
				for c in currLayer.components:
					if c.componentLayer.components:
						c.decompose()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
