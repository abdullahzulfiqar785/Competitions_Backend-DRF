from ckeditor.fields import RichTextField
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class MoveSectionEnum(models.IntegerChoices):
    PUBLISHEINPREPARECOMETITION = 1, 'Prepared Competitions'
    ONLINEINCOMETITION = 2, 'Ongoing Competitions'
    ARCHIEVEDCOMPETITION = 3, 'Archived Competitions'


class GroupTitleEnum(models.IntegerChoices):
    FEATUREDCOMPETITION = 1, 'Featured Competition'
    ACTIVECOMETITION = 2, 'Active Competition'
    # COUPONCOMETITION = 3, 'Coupon Competition'
    # SATURDAYSESH = 4, 'Saturday Sesh'


class Competition(models.Model):
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    letter_choices = models.CharField(
        max_length=3, help_text="Please Enter range as A-Z")
    numbers_from = models.CharField(
        help_text="Please Enter range as 00-99", max_length=7)
    total_tickets = models.PositiveIntegerField()
    total_winners = models.PositiveIntegerField(default=1)
    # date_increment_counter = models.PositiveIntegerField(default=0)
    actual_closing_date = models.DateTimeField(null=True)
    # ultimate_closing_date = models.DateTimeField(null=True)
    description = RichTextField()
    group_title = models.SmallIntegerField(choices=GroupTitleEnum.choices)
    # coupon_code_asked = models.BooleanField(default=False)
    move_section = models.SmallIntegerField(choices=MoveSectionEnum.choices)
    discount_price = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(1)])
    discount_text = models.CharField(max_length=255, null=True, blank=True)
    discount_active = models.BooleanField(default=False,)
    product_price = models.PositiveIntegerField(null=True, blank=True)

    @property
    def competition_image(self):
        return self.images.all().first()

    # def save(self, *args, **kwargs):
    #     if not self.actual_closing_date:
    #         week = datetime.timedelta(weeks=1)
    #         self.actual_closing_date = self.closing_date
    #         self.actual_closing_date = self.closing_date+week
    #     super(Competition, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CompetitionTicketStatusEnum(models.IntegerChoices):
    AVAILABALE = 1, "Available"
    SOLD = 2, "Sold"
    RESERVED = 3, "Reserved"


class CompetitionTicket(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='tickets')
    ticket = models.CharField(max_length=25)
    sold_time = models.DateTimeField(auto_now_add=False, null=True)
    status = models.SmallIntegerField(
        choices=CompetitionTicketStatusEnum.choices, default=CompetitionTicketStatusEnum.AVAILABALE)
    customer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        id = str(self.ticket)
        return self.ticket

class CompetitionImage(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="comititions", null=False, blank=False)

    def __str__(self):
        id = self.id
        return f"image:({str(id)})"
