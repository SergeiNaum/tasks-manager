from django.db import models
from django.utils.translation import gettext_lazy as _

from labels.models import Label
from users.models import User
from statuses.models import Status

# from labels.models import Label


class TimestampedModel(models.Model):
    """An abstract model with a pair of timestamps."""

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Creation date")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date to update"))

    class Meta:
        abstract = True


class Task(TimestampedModel):
    name = models.CharField(
        max_length=150, unique=True, blank=False, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=10000, unique=True, blank=True, verbose_name=_("Description")
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="author", verbose_name=_("Author")
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="statuses",
        verbose_name=_("Status"),
    )
    executor = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="executor",
        verbose_name=_("Executor"),
    )

    labels = models.ManyToManyField(
        Label,
        through="TaskLabelRelation",
        through_fields=("task", "label"),
        blank=True,
        related_name="labels",
        verbose_name=_("Labels"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
