from django.db.models import fields
from rest_framework import serializers
from .models import Competition, CompetitionImage, CompetitionTicket


class CompetitionTicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompetitionTicket
        fields = [
            'id',
            'ticket',
            'customer',
            'status'
        ]


class CompetitionImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompetitionImage
        fields = [
            'image',
        ]


class CompetitionSerializers(serializers.ModelSerializer):
    tickets = CompetitionTicketSerializers(read_only=True, many=True)
    images = CompetitionImageSerializers(read_only=True, many=True)

    class Meta:
        model = Competition
        fields = [
            'id',
            'title',
            'price',
            'numbers_from',
            'total_tickets',
            'total_winners',
            'actual_closing_date',
            'description',
            'group_title',
            'discount_price',
            'discount_text',
            'discount_active',
            'product_price',
            'tickets',
            'images',
        ]
