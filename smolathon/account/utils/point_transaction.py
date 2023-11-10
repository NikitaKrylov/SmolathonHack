from django.contrib.auth.models import User
from django.utils import timezone

from account.exceptions import CheckInUrlError, TransactionError
from account.models import CheckInURL, RewardPointTransaction


def add_points_to_user(user: User, check_in_url: CheckInURL):
    now = timezone.now().date()
    if not (check_in_url.from_date <= now <= check_in_url.to_date):
        raise CheckInUrlError(check_in_url)

    if user.transactions.filter(check_in_url=check_in_url).exists():
        raise TransactionError()

    return create_points_transaction(user, check_in_url)


def create_points_transaction(user: User, check_in_url: CheckInURL) -> RewardPointTransaction:
    transaction = RewardPointTransaction(
        check_in_url=check_in_url,
        points=check_in_url.reward_points,
        user=user
    )
    transaction.save()
    return transaction
