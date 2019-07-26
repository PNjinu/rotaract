from django.db import models
 
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePageCarouselImages(Orderable):
    """ Three Images for the Three slides that introduce the club """

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image  = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )


    carousel_title = models.CharField(max_length=100, blank=True, null=True)
    carousel_sub_title = models.CharField(max_length=350, blank=True, null=True)
    carousel_button_text = models.CharField(max_length=100, blank=True, null=True)



    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("carousel_title"),
        FieldPanel("carousel_sub_title"),
        FieldPanel("carousel_button_text"),
        ]


class HomePage(Page):
    """ Home Page model. """
    templates = "home/home_page.html"
    max_count=1

    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Carousel")],
            heading="Carousel Details"
        )
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

