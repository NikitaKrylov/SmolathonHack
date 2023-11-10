from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from account.models import UserAccount

admin.site.unregister(User)


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    readonly_fields = (
        'reward_points',
    )

    def reward_points(self, user: UserAccount):
        return mark_safe(f"<p>{user.reward_points}</p>")

    reward_points.short_description = 'Очки'
#
#
# @admin.register(CheckInURL)
# class CheckInURLAdmin(admin.ModelAdmin):
#     readonly_fields = (
#         # 'qr_code',
#         'url_path',
#     )
#
#     def url_path(self, obj: CheckInURL):
#         return mark_safe(f"<p>{obj.build_url}</p>")
#
#     url_path.short_description = "Ссылка"
#
#
# @admin.register(RewardPointTransaction)
# class RewardPointTransactionAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(TravelRoute)
# admin.site.register(TravelRouteDay)
#
#
#
#
#
#
