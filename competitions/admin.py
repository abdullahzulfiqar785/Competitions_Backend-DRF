from django.contrib import admin
from .models import CompetitionImage, Competition, CompetitionTicket
from .utils import char_Count


class CompetitionImageAdmin(admin.TabularInline):
    model = CompetitionImage
    extra = 1
    max_num = 5
    min_num = 1


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    # form = CompetitionForm
    inlines = [
        CompetitionImageAdmin,
    ]
    list_display = (
        'id',
        'title',
        'actual_closing_date',
        'price',
        'discount_price',
        'discount_active',
        'total_tickets',
        'group_title',
    )

    list_display_links = ('title',)
    # readonly_fields = ('date_increment_counter',)
    list_filter = (
        # ('move_section', custom_titled_filter('By Status')),
        'move_section',
    )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)
        obj.save()
        choices = char_Count(obj.letter_choices)
        starting_range, ending_range = obj.numbers_from.split("-")
        for choice in choices:
            for j in range(int(starting_range), int(ending_range)+1):
                ticket = choice+str(j)
                CompetitionTicket.objects.create(
                    competition=obj, ticket=ticket)


class CompetitionTicketAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    list_display = [
        'id',
        'competition',
        'customer',
        'ticket',
        'status'
    ]


admin.site.register(CompetitionTicket, CompetitionTicketAdmin)
