from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("workflows", "0017_teamworkflowsconfig_ses_tenant_state"),
    ]

    # Phase 2 of the two-phase table drop (safe-django-migrations.md, "Dropping Tables").
    # 0015 removed EmailReputationSnapshot from Django state and 0016 dropped its FK to
    # posthog_hogflow; the physical table has been dead ever since. This drops it now that the
    # state removal has shipped. Irreversible by nature — the reverse is a no-op rather than a
    # bogus CREATE TABLE, so a rollback past this point simply leaves the table absent (nothing
    # reads or writes it).
    operations = [
        migrations.RunSQL(
            sql='DROP TABLE IF EXISTS "posthog_emailreputationsnapshot";',
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
