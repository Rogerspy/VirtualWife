# Generated by Django 4.2.1 on 2024-01-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='background/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomRoleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('persona', models.TextField()),
                ('personality', models.TextField()),
                ('scenario', models.TextField()),
                ('examples_of_dialogue', models.TextField()),
                ('custom_role_template_type', models.CharField(max_length=50)),
                ('role_package_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocalMemoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tags', models.TextField()),
                ('sender', models.CharField(default='null', max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PortalUser',
            fields=[
                ('id', models.BigIntegerField(db_comment='门户用户唯一ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_comment='门户用户名称', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RolePackageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=10)),
                ('dataset_json_path', models.CharField(max_length=10)),
                ('embed_index_idx_path', models.CharField(max_length=10)),
                ('system_prompt_txt_path', models.CharField(max_length=10)),
                ('role_package', models.FileField(upload_to='role_package/')),
            ],
        ),
        migrations.CreateModel(
            name='SysConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('config', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VrmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('original_name', models.CharField(max_length=50)),
                ('vrm', models.FileField(upload_to='vrm/')),
            ],
        ),
    ]
