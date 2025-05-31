from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider , Announcement , Project , AboutPage

class HomeSliderTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'heading', 'subheading', 'button_text')

class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(AboutPage, AboutTranslationOptions)