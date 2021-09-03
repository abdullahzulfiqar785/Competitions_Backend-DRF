from django.contrib import admin
from .models import CompetitionImage, Competition, CompetitionTicket


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

    # def save_model(self, request: Any, obj: _ModelT, form: Any, change: Any) -> None:
    #     return super().save_model(request, obj, form, change)\
    
    def save_model(self, request, obj, form, change):
        choices=[chr(i) for i in range(ord(obj.letter_choices[0].upper()),ord(obj.letter_choices[2].upper())+1)]
        num_choice=lst_int = [int(x) for x in obj.numbers_from.split("-")]

        for i in choices:
            for j in range(num_choice[0],num_choice[1]):
                ticket=i+j
                CompetitionTicket.objects.create(obj,ticket)



        pass
