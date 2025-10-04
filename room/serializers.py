from rest_framework import serializers
from .models import Property, Room, Availability

class PropertyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ("id", "hotel_name", "city", "type", "country")

class RoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "title", "slug", "price", "capacity")

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            "id", "hotel_name", "type", "country", "province", "city",
            "address", "tell", "email",
            "default_checkin_time", "default_checkout_time",
        ]

class RoomSerializer(serializers.ModelSerializer):
    hotel = PropertyMiniSerializer(source="hotel_name", read_only=True)

    class Meta:
        model = Room
        fields = [
            "id", "hotel_name", "hotel",
            "title", "slug",
            "capacity", "number_of_room", "size",
            "rating", "price",
            "description", "is_active", "amenity",
        ]

class AvailabilitySerializer(serializers.ModelSerializer):
    room_detail = RoomMiniSerializer(source="room", read_only=True)
    available_units = serializers.SerializerMethodField()
    effective_price = serializers.SerializerMethodField()

    class Meta:
        model = Availability
        fields = [
            "id", "room", "room_detail",
            "date",
            "units_total", "units_reserves",
            "is_close",
            "price_override", "min_nights",
            "create_or_update_at",
            "available_units", "effective_price",
        ]
        read_only_fields = ("create_or_update_at",)

    def get_available_units(self, obj):
        # موجودی لحظه‌ای
        try:
            return max((obj.units_total or 0) - (obj.units_reserves or 0), 0)
        except Exception:
            return None

    def get_effective_price(self, obj):
        # اگر price_override بود، همونو؛ وگرنه قیمت Room
        if obj.price_override is not None:
            return obj.price_override
        return getattr(obj.room, "price", None)

    def validate(self, attrs):
        # تضمین: units_reserves <= units_total
        total = attrs.get("units_total", getattr(self.instance, "units_total", None))
        reserved = attrs.get("units_reserves", getattr(self.instance, "units_reserves", 0))
        if total is not None and reserved is not None and reserved > total:
            raise serializers.ValidationError("تعداد رزرو شده نمی‌تواند بیشتر از ظرفیت کل باشد.")
        return attrs
