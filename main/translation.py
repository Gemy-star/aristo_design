from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider , Announcement , Project

class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'heading', 'subheading', 'button_text')

class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)
translator.register(Project, ProjectTranslationOptions)