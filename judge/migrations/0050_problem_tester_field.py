# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import judge.models
import judge.utils.problem_data


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0049_contest_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='testers',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to view a private problem, but not edit it.', related_name='tested_problems', to='judge.Profile', verbose_name='testers'),
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='generator',
            field=models.FileField(blank=True, null=True, storage=judge.utils.problem_data.ProblemDataStorage(), upload_to=judge.models.problem_directory_file, verbose_name='generator file'),
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='zipfile',
            field=models.FileField(blank=True, null=True, storage=judge.utils.problem_data.ProblemDataStorage(), upload_to=judge.models.problem_directory_file, verbose_name='data zip file'),
        ),
    ]
