from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider

class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'heading', 'subheading', 'button_text')

translator.register(HomeSlider, HomeSliderTranslationOptions)