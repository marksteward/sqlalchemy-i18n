import sqlalchemy as sa
from sqlalchemy_i18n import Translatable
from tests import TestCase


class TestCurrentTranslation(TestCase):
    def test_as_object_property_with_force_locale(self):
        article = self.Article()
        article.name = u'Some article'
        article.content = u'Some content'
        self.session.add(article)
        self.session.commit()
        with article.force_locale('fi'):
            assert article.current_translation == article._translation_fi

    def test_as_class_property(self):
        assert self.Article.current_translation

    def test_setter(self):
        article = self.Article()
        article.current_translation = self.Article.__translatable__['class'](
            name=u'Something'
        )
        self.session.add(article)
        self.session.commit()
        assert article.name == u'Something'



class TestCurrentTranslationWithLocaleObject(TestCase):
    def create_models(self):
        class Locale(object):
            def __init__(self, value):
                self.value = value

            def __str__(self):
                return self.value

            def __unicode__(self):
                return self.value

        class Article(self.Model, Translatable):
            __tablename__ = 'article'
            __translated_columns__ = [
                sa.Column('name', sa.Unicode(255), nullable=False),
                sa.Column('content', sa.UnicodeText)
            ]
            __translatable__ = {
                'base_classes': (self.Model, ),
                'locales': ['en', 'fi'],
                'default_locale': 'en'
            }

            def get_locale(self):
                return Locale('en')

            id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
            description = sa.Column(sa.UnicodeText)

        self.Article = Article

    def test_converts_locale_object_to_unicode(self):
        article = self.Article()
        article.name = u'Some article'
        assert article.name == u'Some article'