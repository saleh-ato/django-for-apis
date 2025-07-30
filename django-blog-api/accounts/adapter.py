from allauth.account.adapter import DefaultAccountAdapter

class NoPhoneAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        #‌ از بررسی وجود شماره تلفن چشم‌پوشی کن
        form._has_phone_field = False
        return super().save_user(request, user, form, commit)
