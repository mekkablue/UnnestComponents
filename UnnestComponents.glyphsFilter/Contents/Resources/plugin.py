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


def compatibleLayerGroups(glyph, font):
	"""
	One group per master: the master layer plus all brace and bracket layers
	that are compatible with it (same compareString). Brace layers are what
	makes up the virtual masters of a variable font.
	"""
	groups = []
	for master in font.masters:
		masterLayer = glyph.layers[master.id]
		if not masterLayer:
			continue
		compareString = masterLayer.compareString()
		group = [masterLayer]
		for currLayer in glyph.layers:
			if currLayer.layerId == masterLayer.layerId or not currLayer.isSpecialLayer:
				continue
			if currLayer.associatedMasterId == master.id and currLayer.compareString() == compareString:
				group.append(currLayer)
		groups.append(group)
	return groups


def unnestLayerGroup(layers):
	"""Decomposes the same components, by index, in all layers of a compatible group."""
	while any(nestedComponents(currLayer) for currLayer in layers):
		componentsPerLayer = [list(currLayer.components) for currLayer in layers]
		for componentGroup in zip(*componentsPerLayer):
			if any(c.componentLayer.components for c in componentGroup):
				for c in componentGroup:
					c.decompose()


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
					layersToProcess = compatibleLayerGroups(glyph, font)
				else:
					layersToProcess = [[currLayer] for currLayer in glyph.layers]

		for layerGroup in layersToProcess:
			unnestLayerGroup([currLayer for currLayer in layerGroup if currLayer])

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
