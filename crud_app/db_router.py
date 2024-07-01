class ExpenseRouter:
    """
    note lable should be a app name = crud_app
    A router to control all database operations on models in the expense application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read expense models go to expense_db_dev.
        """
        if model._meta.app_label == 'crud_app':
            return 'expense_db_dev'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write expense models go to expense_db_dev.
        """
        if model._meta.app_label == 'crud_app':
            return 'expense_db_dev'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the expense app is involved.
        """
        if obj1._meta.app_label == 'crud_app' or obj2._meta.app_label == 'crud_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the expense app only appears in the 'expense_db_dev' database.
        """
        if app_label == 'crud_app':
            return db == 'expense_db_dev'
        return None
    

    #after everything spesify in settings.py
#     DATABASE_ROUTERS = [
#     'crud_app.db_router.ExpenseRouter',
# ]
