class Translation:
    def __init__(self, original, translated, creatorUserId=None):
        self._original = original
        self._translated = translated
        self._creatorId = creatorUserId

    @property
    def sourceWord(self):
        return self._original
    
    @property
    def translatedWord(self):
        return self._translated

    @property
    def userId(self):
        return self._creatorId
    