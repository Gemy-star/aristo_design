from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider , Announcement

class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'heading', 'subheading', 'button_text')

class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)