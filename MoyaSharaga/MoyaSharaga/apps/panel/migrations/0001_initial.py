# Generated by Django 3.0.4 on 2020-03-11 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_short_title', models.CharField(max_length=20, verbose_name='Название Кафедры(Сокращенно)')),
                ('department_title', models.CharField(max_length=200, verbose_name='Название Кафедры')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty_title', models.CharField(max_length=200, verbose_name='Название Специальности')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Department')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('teacher_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('teacher_patronymic', models.CharField(max_length=200, verbose_name='Отчество')),
                ('teacher_sex', models.CharField(max_length=1, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Преподователь',
                'verbose_name_plural': 'Преподователи',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_short_title', models.CharField(max_length=20, verbose_name='Название Вуза(Сокращенно)')),
                ('university_title', models.CharField(max_length=200, verbose_name='Название Вуза')),
            ],
            options={
                'verbose_name': 'ВУЗ',
                'verbose_name_plural': 'ВУЗЫ',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('student_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('student_patronymic', models.CharField(max_length=200, verbose_name='Отчество')),
                ('student_group', models.CharField(max_length=20, verbose_name='Группа')),
                ('student_sex', models.CharField(max_length=1, verbose_name='Пол')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Specialty')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_short_title', models.CharField(max_length=20, verbose_name='Название Факультета(Сокращенно)')),
                ('faculty_title', models.CharField(max_length=200, verbose_name='Название Факультета')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.University')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Faculty'),
        ),
    ]