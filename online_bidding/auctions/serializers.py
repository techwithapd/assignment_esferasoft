from rest_framework import serializers
from .models import Product, Bid
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['owner', 'current_price']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'
        read_only_fields = ['bidder']

    def validate(self, data):
        product = data['product']
        amount = data['amount']
        bidder = self.context['request'].user

        if bidder == product.owner:
            raise serializers.ValidationError("Cannot bid on your own product!")
        
        if not product.is_active():
            raise serializers.ValidationError("Auction has expired!")
        
        highest_bid = product.bids.first()
        min_bid = highest_bid.amount if highest_bid else product.starting_price

        if amount <= min_bid:
            raise serializers.ValidationError("Bid amount must be higher than the current highest bid!")


        return data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

