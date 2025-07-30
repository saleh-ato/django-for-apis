# from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer
# from rest_framework import serializers

# class RegisterSerializer(DefaultRegisterSerializer):
#     # اگر واقعاً می‌خواید phone_number هم داشته باشید:
#     # phone_number = serializers.CharField(required=False, allow_blank=True)

#     @property
#     def _has_phone_field(self):
#         # اگر phone_number تعریف شده باشه True برمی‌گردونه
#         # وگرنه False (یا همیشه False)
#         return False
