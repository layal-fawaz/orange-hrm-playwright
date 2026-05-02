import functools
def pw_trace(label=None):                 
    def decorator(func):          
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            group_label = label or f"{type(self).__name__} > {func.__name__}"
            self.page.context.tracing.group(group_label)
            try:
                return func(self, *args, **kwargs)
            finally:
                self.page.context.tracing.group_end()
        return wrapper
    return decorator
